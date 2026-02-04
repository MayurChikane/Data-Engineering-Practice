print("----------------------------- Practice Day 37 ----------------------------")

# Flask Web Application with RESTful API
from flask import Flask, jsonify, request
def create_restful_app():
    app = Flask(__name__)
    items = []
    
    @app.route('/items', methods=['GET'])
    def get_items():
        return jsonify(items)
    
    @app.route('/items', methods=['POST'])
    def add_item():
        item = request.json['item']
        items.append(item)
        return jsonify({'message': 'Item added', 'items': items}), 201
    
    @app.route('/items/<int:index>', methods=['PUT'])
    def update_item(index):
        item = request.json['item']
        if 0 <= index < len(items):
            items[index] = item
            return jsonify({'message': 'Item updated', 'items': items})
        else:
            return jsonify({'error': 'Index out of range'}), 404
    
    @app.route('/items/<int:index>', methods=['DELETE'])
    def delete_item(index):
        if 0 <= index < len(items):
            items.pop(index)
            return jsonify({'message': 'Item deleted', 'items': items})
        else:
            return jsonify({'error': 'Index out of range'}), 404
    
    return app
if __name__ == "__main__":
    app = create_restful_app()
    print("🚀 Starting RESTful API on http://localhost:5000/")
    app.run(debug=True)
    
print("-------------------------- End of Practice Day 37 --------------------------")