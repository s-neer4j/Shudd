from flask import Flask, request, render_template, jsonify
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import time

app = Flask(__name__)

# Load the tokenizer and model
tokenizer = BertTokenizer.from_pretrained("models")  # Directory with tokenizer files
model = BertForSequenceClassification.from_pretrained("models/offensive_model")  # Directory with model files
model.eval()  # Set model to evaluation mode

# Track users by IP
user_status = {}

def predict_offensive(text):
    # Tokenize and predict
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    return prediction == 1  # Return True if offensive, False if not

def manage_penalty(user_id):
    # Initialize or retrieve the user's penalty status
    if user_id not in user_status:
        user_status[user_id] = {"offense_count": 0, "penalty_time": None, "blocked": False}
    
    status = user_status[user_id]

    # Check if the user is blocked
    if status["blocked"]:
        return "blocked"
    
    # Check if the user is within the freeze period
    if status["penalty_time"] and time.time() < status["penalty_time"]:
        return "frozen"

    # Manage penalties based on offense count
    status["offense_count"] += 1
    if status["offense_count"] == 1:
        return "warning"
    elif status["offense_count"] == 2:
        status["penalty_time"] = time.time() + 300  # Freeze for 5 minutes
        return "frozen"
    else:
        status["blocked"] = True
        return "blocked"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_id = request.remote_addr  # Identify user by IP address
    message = request.json['message']

    # Check if the message is offensive
    if predict_offensive(message):
        penalty_status = manage_penalty(user_id)
        return jsonify({"status": penalty_status})
    else:
        return jsonify({"status": "clean"})

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)
