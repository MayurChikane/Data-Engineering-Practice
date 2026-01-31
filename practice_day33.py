print("----------------------------- Practice Day 33 ----------------------------")

# Flask app with file upload handling
from flask import Flask, request, render_template_string
def create_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template_string("""
            <html>
                <head><title>File Upload</title></head>
                <body>
                    <h1>Upload a File</h1>
                    <form action="/upload" method="post" enctype="multipart/form-data">
                        <input type="file" name="file" required>
                        <input type="submit" value="Upload">
                    </form>
                </body>
            </html>
        """)

    @app.route('/upload', methods=['POST'])
    def upload():
        uploaded_file = request.files.get('file')
        if uploaded_file:
            filename = uploaded_file.filename
            # Here you would normally save the file and process it
            return render_template_string(f"""
                <html>
                    <head><title>Upload Successful</title></head>
                    <body>
                        <h1>File Uploaded Successfully!</h1>
                        <p>Filename: {filename}</p>
                    </body>
                </html>
            """)
        else:
            return render_template_string("""
                <html>
                    <head><title>Upload Failed</title></head>
                    <body>
                        <h1>No file selected!</h1>
                    </body>
                </html>
            """)

    return app
if __name__ == "__main__":
    app = create_flask_app()
    print("🚀 Starting Flask app on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 33 --------------------------")