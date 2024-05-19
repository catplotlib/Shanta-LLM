from flask import Flask, request, jsonify
from model import get_model, generate_answer

app = Flask(__name__)

# Load the model when the app starts
model = get_model()

@app.route('/predict', methods=['POST'])
def predict():
    print("Generating Answer")
    content = request.json
    question = content['question']
    answer = generate_answer(model, question)
    return jsonify(answer=answer)

if __name__ == '__main__':
    print("Running on https://127.0.0.1:5000/")
    app.run(host='127.0.0.1', port=5000)
