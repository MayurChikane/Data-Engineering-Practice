print("----------------------------- Practice Day 30 ----------------------------")

# Flask app with multiple routes
from flask import Flask, render_template_string
def create_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template_string("""
            <html>
                <head><title>Home Page</title></head>
                <body>
                    <h1>Welcome to the Home Page!</h1>
                    <p>This is the main page of the Flask application.</p>
                </body>
            </html>
        """)

    @app.route('/about')
    def about():
        return render_template_string("""
            <html>
                <head><title>About Page</title></head>
                <body>
                    <h1>About This App</h1>
                    <p>This Flask application demonstrates multiple routes.</p>
                </body>
            </html>
        """)

    return app
if __name__ == "__main__":
    app = create_flask_app()
    print("🚀 Starting Flask app on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 30 --------------------------")