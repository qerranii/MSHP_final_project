from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def learn():
    pass

@app.route('/getrec', methods = ["GET"])
def get_rec():
    data_str = request.args.get('data', '')
    data = json.loads(data_str)
    data["id_user"] += "a"
    data["id_item"] += 3
    data["rating"] += 2
    return jsonify(data)

@app.route('/')
def start():
    return  "<p>hello</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8081)
