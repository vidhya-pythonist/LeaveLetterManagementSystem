from flask import Flask, render_template

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')



@app.route('/write-data')
def write_name():
    name = request.args.get('name')
    if name:
        data = {"name": name}
        with open('result.json', 'a') as f:
            f.write(json.dumps(data))
            f.write('\n,')
        return f"Name {name} has been written to the file."
    else:
        return "Name parameter is missing in the URL."




@app.route('/get-data')
def get_data():
    with open('result.json', 'r') as f:
        data = f.readlines()

    # Concatenate all lines into a single string
    data_str = ''.join(data)

    # Remove trailing comma and newline characters
    data_str = data_str.rstrip(',\n')

    # Convert the string to a list of JSON objects
    data_list = json.loads('[' + data_str + ']')

    return jsonify(data_list)





if __name__ == '__main__':
    app.run(debug=True)
