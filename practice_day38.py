print("------------------------------ Practice Day 38 ----------------------------")

# Flask Web Application with User Authentication
from flask import Flask, jsonify, request, session
from werkzeug.security import generate_password_hash, check_password_hash
def create_auth_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'
    users = {}
    @app.route('/register', methods=['POST'])
    def register():
        username = request.json['username']
        password = request.json['password']
        if username in users:
            return jsonify({'error': 'User already exists'}), 400
        users[username] = generate_password_hash(password)
        return jsonify({'message': 'User registered successfully'}), 201
    @app.route('/login', methods=['POST'])
    def login():
        username = request.json['username']
        password = request.json['password']
        if username in users and check_password_hash(users[username], password):
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
    app = create_auth_app()
    print("🚀 Starting Authentication App on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 38 --------------------------")