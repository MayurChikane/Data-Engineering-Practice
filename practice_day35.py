print("----------------------------- Practice Day 35 ----------------------------")

# Simple REST API with Flask
from flask import Flask, jsonify, request
def create_rest_api():
    app = Flask(__name__)
    items = []
    @app.route('/items', methods=['GET'])
    def get_items():
        return jsonify(items)
    @app.route('/items', methods=['POST'])
    def add_item():
        item = request.json
        items.append(item)
        return jsonify(item), 201
    return app
if __name__ == "__main__":
    app = create_rest_api()
    print("🚀 Starting REST API on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 35 --------------------------")