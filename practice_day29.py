print("----------------------------- Practice Day 29 ----------------------------")

# Flask intro app
from flask import Flask, render_template_string
def create_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template_string("""
            <html>
                <head><title>Flask Intro App</title></head>
                <body>
                    <h1>Welcome to the Flask Intro App!</h1>
                    <p>This is a simple Flask application.</p>
                </body>
            </html>
        """)

    return app
if __name__ == "__main__":
    app = create_flask_app()
    print("🚀 Starting Flask app on http://localhost:5000/")
    app.run(debug=True)