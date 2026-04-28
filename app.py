from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Tic Tac Toe is ready!'}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
