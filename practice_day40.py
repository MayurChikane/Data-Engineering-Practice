print("---------------------------------- Practice Day 40 ----------------------------")

# Flask with jwt authentication and role-based access control
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

def create_jwt_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db = SQLAlchemy(app)
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password_hash = db.Column(db.String(120), nullable=False)
        role = db.Column(db.String(20), nullable=False)
    @app.before_request
    def create_tables():
        db.create_all()
    @app.route('/register', methods=['POST'])
    def register():
        username = request.json['username']
        password = request.json['password']
        role = request.json.get('role', 'user')
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'User already exists'}), 400
        new_user = User(username=username, password_hash=generate_password_hash(password), role=role)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    @app.route('/login', methods=['POST'])
    def login():
        username = request.json['username']
        password = request.json['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            token = jwt.encode({'username': username, 'role': user.role, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
            return jsonify({'token': token})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    def token_required(f):
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'error': 'Token is missing'}), 401
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = User.query.filter_by(username=data['username']).first()
            except:
                return jsonify({'error': 'Token is invalid'}), 401
            return f(current_user, *args, **kwargs)
        return decorated
    @app.route('/admin', methods=['GET'])
    @token_required
    def admin(current_user):
        if current_user.role != 'admin':
            return jsonify({'error': 'Access denied'}), 403
        return jsonify({'message': f"Welcome Admin {current_user.username}!"})
    return app
if __name__ == "__main__":
    app = create_jwt_app()
    print("🚀 Starting JWT Auth App on http://localhost:5000/")
    app.run(debug=True)