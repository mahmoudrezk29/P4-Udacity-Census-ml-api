import numpy as np
from sklearn.linear_model import LogisticRegression
from model.model import train_model, inference, compute_model_metrics


def test_train_model_returns_model():
    X = np.array([[0, 1], [1, 0], [0, 0]])
    y = np.array([0, 1, 0])
    model = train_model(X, y)
    assert isinstance(model, LogisticRegression)


def test_inference_output_shape():
    X = np.array([[0, 1], [1, 0]])
    y = np.array([0, 1])
    model = train_model(X, y)
    preds = inference(model, X)
    assert preds.shape == (2,)
    assert set(preds).issubset({0, 1})
    

def test_compute_model_metrics_returns_floats():
    y_true = np.array([0, 1, 0, 1])
    y_pred = np.array([0, 1, 1, 1])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
