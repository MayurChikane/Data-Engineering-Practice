print("----------------------------- Practice Day 31 ----------------------------")

# Flask app with dynamic route and query parameters
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
                    <p>This is the main page of the Flask application.</p>
                </body>
            </html>
        """)

    @app.route('/greet/<name>')
    def greet(name):
        greeting = request.args.get('greeting', 'Hello')
        return render_template_string(f"""
            <html>
                <head><title>Greet Page</title></head>
                <body>
                    <h1>{greeting}, {name}!</h1>
                    <p>This page greets the user with a dynamic message.</p>
                </body>
            </html>
        """)

    return app
if __name__ == "__main__":
    app = create_flask_app()
    print("🚀 Starting Flask app on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 31 --------------------------")