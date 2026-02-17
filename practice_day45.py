print("------------------------------------------ Practice Day 45 ----------------------------")

# Flask advanced web app with templates
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)
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
    
def about():
    return render_template('about.html')

def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)