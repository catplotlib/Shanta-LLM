import keras

def get_model():
    # Adjust the path as needed when deploying
    return keras.models.load_model('Gemma.keras', compile=False)

def generate_answer(model, question):
    prompt = f"Question: {question}\nAnswer:"
    # You might need to adjust the generate function based on your model's API
    answer = model.generate(prompt, max_length=128)
    return answer
