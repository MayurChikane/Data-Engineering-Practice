print("----------------------------- Practice Day 34 ----------------------------")

# Flask app with session management
from flask import Flask, session, redirect, url_for, request, render_template_string
def create_flask_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # Needed for session management
    @app.route('/')
    def home():
        if 'username' in session:
            username = session['username']
            return render_template_string(f"""
                <html>
                    <head><title>Welcome</title></head>
                    <body>
                        <h1>Welcome back, {username}!</h1>
                        <a href="/logout">Logout</a>
                    </body>
                </html>
            """)
        return render_template_string("""
            <html>
                <head><title>Login</title></head>
                <body>
                    <h1>Please log in</h1>
                    <form action="/login" method="post">
                        <input type="text" name="username" placeholder="Username" required>
                        <input type="submit" value="Login">
                    </form>
                </body>
            </html>
        """)
    @app.route('/login', methods=['POST'])
    def login():
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('home'))
    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect(url_for('home'))
    return app
if __name__ == "__main__":
    app = create_flask_app()
    print("🚀 Starting Flask app on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 34 --------------------------")