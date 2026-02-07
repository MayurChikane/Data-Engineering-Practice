print("--------------------------------- Practice Day 39 ----------------------------")

# Flask Web Application with RESTful API with auth and database integration
from flask import Flask, jsonify, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
def create_restful_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db = SQLAlchemy(app)
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password_hash = db.Column(db.String(120), nullable=False)
    @app.before_first_request
    def create_tables():
        db.create_all()
    @app.route('/register', methods=['POST'])
    def register():
        username = request.json['username']
        password = request.json['password']
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'User already exists'}), 400
        new_user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    @app.route('/login', methods=['POST'])
    def login():
        username = request.json['username']
        password = request.json['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['username'] = username
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    @app.route('/logout', methods=['POST'])
    def logout():
        session.pop('username', None)
        return jsonify({'message': 'Logout successful'})
    @app.route('/profile', methods=['GET'])
    def profile():
        if 'username' in session:
            return jsonify({'message': f"Welcome {session['username']}!"})
        else:
            return jsonify({'error': 'Unauthorized'}), 401
    return app
if __name__ == "__main__":
    app = create_restful_app()
    print("🚀 Starting RESTful API App on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 39 --------------------------")