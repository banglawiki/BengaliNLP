"""
Evaluation metrics for Bengali NLP tasks.
"""

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def evaluate_classification(y_true, y_pred, average="weighted"):
    """
    Returns accuracy, precision, recall, and F1 score.
    """
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average=average, zero_division=0),
        "recall": recall_score(y_true, y_pred, average=average, zero_division=0),
        "f1": f1_score(y_true, y_pred, average=average, zero_division=0),
    }


def evaluate_sequence_labeling(y_true, y_pred, average="weighted"):
    """
    Evaluate token-level sequence labeling (e.g., NER, POS).
    Returns token-level accuracy and F1.
    """
    flat_true = [item for sublist in y_true for item in sublist]
    flat_pred = [item for sublist in y_pred for item in sublist]
    return {
        "accuracy": accuracy_score(flat_true, flat_pred),
        "f1": f1_score(flat_true, flat_pred, average=average, zero_division=0),
    }
