print("----------------------------------------- Practice Day 44 ----------------------------")

# Flask advanced web app
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Flask Advanced Web App!"
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to the Flask Advanced Web App!"
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({'error': 'Please provide both num1 and num2'}), 400
    try:
        result = float(num1) + float(num2)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide numbers.'}), 400
if __name__ == '__main__':
    app.run(debug=True)
    
print("---------------------------------------- Practice Day 44 ----------------------------")