from flask import Flask, request, jsonify,render_template
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from problems import problems

app = Flask(__name__)

vectorizer = TfidfVectorizer()
question_texts = list(problems.keys())
question_vectors = vectorizer.fit_transform(question_texts)
@app.route('/')
def home():
    return render_template("chat_bot.html")  # Отдаём HTML-страницу

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Введите ваш вопрос"}), 400

    user_question = data["question"].strip().lower()
    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vector, question_vectors).flatten()

    max_similarity = max(similarities)
    best_match_index = similarities.argmax()
    best_match_question = question_texts[best_match_index]

    if max_similarity > 0.5:
        response = problems[best_match_question]
    else:
        response = "Ваш вопрос передан администратору. Ожидайте ответа."

    return jsonify({
        "user_question": user_question,
        "matched_question": best_match_question,
        "similarity": round(max_similarity, 2),
        "response": response
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8081)
