from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/write_name', methods=['POST'])
def write_name():
    name = request.form.get('name')
    with open('data.txt', 'a') as f:
        f.write(name + '\n')
    return jsonify({'message': 'Name saved successfully'})

@app.route('/read_names', methods=['GET'])
def read_names():
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()
    return jsonify({'names': data})
