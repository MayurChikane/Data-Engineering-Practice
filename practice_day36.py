print("----------------------------- Practice Day 36 ----------------------------")

# Flask Web Application with Templating
from flask import Flask, render_template, request
def create_web_app():
    app = Flask(__name__)
    items = []
    @app.route('/')
    def index():
        return render_template('index.html', items=items)
    @app.route('/add', methods=['POST'])
    def add_item():
        item = request.form['item']
        items.append(item)
        return render_template('index.html', items=items)
    return app
    @app.route('/add', methods=['PUT'])
    def update_item():
        item = request.form['item']
        index = int(request.form['index'])
        items[index] = item
        return render_template('index.html', items=items)
    @app.route('/delete', methods=['DELETE'])
    def delete_item():
        index = int(request.form['index'])
        items.pop(index)
        return render_template('index.html', items=items)
    
if __name__ == "__main__":
    app = create_web_app()
    print("🚀 Starting Web App on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 36 --------------------------")