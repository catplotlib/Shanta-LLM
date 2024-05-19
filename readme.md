# Shanta: Medical Q&A Fine-Tuned Model

## Overview
This repository hosts a fine-tuned version of the GemmaCausalLM model, specifically tailored for generating answers to medical questions. The model is fine-tuned using a comprehensive dataset of medical questions and answers, aiming to assist researchers, medical students, and professionals by providing detailed, AI-generated responses to complex medical queries. The backend for serving model predictions is implemented using Flask.

## Model Training

### Environment Setup
The model is trained in a Google Colab environment, leveraging Keras with a JAX backend. The setup involves:
- Installing necessary libraries including `tf-keras`, `keras-nlp`, and Keras.
- Configuring Kaggle API for dataset access.
- Setting up the JAX backend and memory configurations for optimal performance.

### Training Process
- **Dataset**: Utilizes a comprehensive medical Q&A dataset from Kaggle.
https://www.kaggle.com/datasets/thedevastator/comprehensive-medical-q-a-dataset
- **Model Configuration**: Uses `GemmaCausalLM` from `keras_nlp.models`, initially with the "gemma_2b_en" preset.
- **Fine-Tuning**: The model employs LoRa Fine-Tuning to enhance specific parameters without altering the entire model structure.
- **Optimization**: Configured with AdamW optimizer, fine-tuned for handling sparse categorical crossentropy loss.

## Backend Setup
- Train the model as described in the training process.
- Save the trained model to the directory shanta-backend.
- Run the Flask application by navigating to the shanta-backend directory and executing 

```
python app.py
```

## Frontend Setup
Run the frontend application using the following command:

```
npm run dev
```

This will start the development server for the frontend, allowing users to interact with the Flask backend through a web interface.


### Contributions
Contributions to this project are welcome! Please consider the following ways to contribute:
- Improvements: Suggestions for improving model accuracy and efficiency.
- Expansion: Adding more medical questions and answers to the dataset.
- Testing: More rigorous testing with diverse medical scenarios.
# Shanta-LLM
