from flask import Flask, request, jsonify
import json
import pickle
import numpy as np #pip install numpy
from lightfm import LightFM #pip install lightfm
from lightfm.data import Dataset

app = Flask(__name__)


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

#сделать запрос к джанго для доступа к бд
# items_db = (запрос к джанго)

@app.route('/getrec', methods = ["GET"])
def get_rec():
    user_id = int(request.args.get('id_user', -1))
    if (user_id == -1):
        return jsonify({"error": "id_user is required"}), 400
    item_ids = np.array(list(items_db.keys()))
    scores = model.predict(user_id, item_ids)
    top_items = item_ids[np.argsort(-scores)][:10] # :10 - кол-во выдачи
    recommendations = [{"item_id": int(item_id), "item_name": items_db[item_id]} for item_id in top_items]
    return jsonify({"user_id": user_id, "recommendations": recommendations})

@app.route('/')
def start():
    return  "<p>hello</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8081)
