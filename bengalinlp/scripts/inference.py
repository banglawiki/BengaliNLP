"""
Script for Bengali LLM inference (HuggingFace Transformers example).
"""
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def predict(text, model_dir):
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = outputs.logits.softmax(dim=-1)
    return probs.detach().numpy()

if __name__ == "__main__":
    sample = "বাংলা ভাষা বিশ্বের অন্যতম সমৃদ্ধ ভাষা।"
    probs = predict(sample, "./output_model")
    print("Predicted probabilities:", probs)
