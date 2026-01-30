print("----------------------------- Practice Day 32 ----------------------------")

# Flask app with form handling and POST request
from flask import Flask, request, render_template_string
def create_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template_string("""
            <html>
                <head><title>Home Page</title></head>
                <body>
                    <h1>Welcome to the Home Page!</h1>
                    <form action="/submit" method="post">
                        <label for="username">Enter your name:</label>
                        <input type="text" id="username" name="username" required>
                        <input type="submit" value="Submit">
                    </form>
                </body>
            </html>
        """)

    @app.route('/submit', methods=['POST'])
    def submit():
        username = request.form.get('username', 'Guest')
        return render_template_string(f"""
            <html>
                <head><title>Submission Page</title></head>
                <body>
                    <h1>Thank you, {username}!</h1>
                    <p>Your form has been submitted successfully.</p>
                </body>
            </html>
        """)

    return app
if __name__ == "__main__":
    app = create_flask_app()
    print("🚀 Starting Flask app on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 32 --------------------------")