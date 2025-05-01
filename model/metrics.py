from model.model import inference, compute_model_metrics
from model.data import process_data


def compute_sliced_metrics(model, data, feature,
                           cat_features, label, encoder, lb):
    """
    Compute and log metrics on slices of the data 
    based on a categorical feature.
    """
    results = []
    unique_vals = data[feature].unique()

    for val in unique_vals:
        slice_data = data[data[feature] == val]

        X_slice, y_slice, _, _ = process_data(
            slice_data,
            categorical_features=cat_features,
            label=label,
            training=False,
            encoder=encoder,
            lb=lb
        )

        preds = inference(model, X_slice)
        precision, recall, fbeta = compute_model_metrics(y_slice, preds)

        results.append(
            f"[{feature} = {val}] -> Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {fbeta:.4f}"
        )

    return results
