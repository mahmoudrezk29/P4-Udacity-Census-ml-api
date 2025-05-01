# Model Card

## Model Details

- **Developer**: Mahmoud Rezk, as part of a Udacity Machine Learning DevOps Engineer Nanodegree project.
- **Date**: April 2025
- **Model version**: v1.0
- **Model type**: Binary classification model (Logistic Regression)
- **Framework**: scikit-learn (LogisticRegression)
- **Training algorithm**: Supervised learning using one-hot encoding for categorical variables and LabelBinarizer for labels.
- **Features used**: workclass, education, marital-status, occupation, relationship, race, sex, native-country, and numerical features such as age, hours-per-week, capital-gain, and capital-loss.
- **Paper/resource**: Based on the UCI Adult Census dataset [https://archive.ics.uci.edu/ml/datasets/adult].
- **License**: Educational use
- **Contact**: GitHub issues [https://github.com/mahmoudrezk29/P4-Udacity-Census-ml-api]

---

## Intended Use

- **Primary intended uses**:
  - Educational demonstration of MLOps pipeline deployment (training, testing, CI/CD, FastAPI-based API, and cloud deployment).
  - Predicting whether an individual earns over $50K annually.

- **Primary intended users**:
  - Students, educators, MLOps engineers, and researchers in training.
  - Not intended for use in production or decision-making systems.

- **Out-of-scope uses**:
  - Not for employment screening, credit scoring, insurance eligibility, or any real-world applications where bias can cause harm.
  - Not recommended for use with populations outside of U.S. census data distribution.

---

## Factors

- **Relevant factors**:
  - Demographic features such as education, race, sex, and marital status can influence both model output and fairness.
  - Model performance may vary based on underrepresented group sizes.

- **Evaluation factors**:
  - Model performance was evaluated on slices of the data based on the `education` feature. Results were recorded in `slice_output.txt`.

---

## Metrics

- **Performance metrics used**:
  - Precision
  - Recall
  - F1 score

- **Decision threshold**: 0.5 (default for binary classification in scikit-learn)
- **Average performance on test set**:
  - Precision: 0.7356608478802993
  - Recall: 0.5633354551241248
  - F1: 0.6380677721701514

- **Variation**:
  - [education = Some-college] -> Precision: 0.6906, Recall: 0.3466, F1: 0.4615
  - [education = HS-grad] -> Precision: 0.7692, Recall: 0.1739, F1: 0.2837
  - [education = Bachelors] -> Precision: 0.7151, Recall: 0.7978, F1: 0.7542
  - [education = Masters] -> Precision: 0.8128, Recall: 0.8599, F1: 0.8357
  - [education = Assoc-acdm] -> Precision: 0.5625, Recall: 0.5745, F1: 0.5684
  - [education = 7th-8th] -> Precision: 0.2500, Recall: 0.1667, F1: 0.2000
  - [education = 11th] -> Precision: 0.6667, Recall: 0.3636, F1: 0.4706
  - [education = Assoc-voc] -> Precision: 0.6731, Recall: 0.5556, F1: 0.6087
  - [education = Prof-school] -> Precision: 0.8554, Recall: 0.8452, F1: 0.8503
  - [education = 9th] -> Precision: 0.5000, Recall: 0.3333, F1: 0.4000
  - [education = 5th-6th] -> Precision: 0.5000, Recall: 0.5000, F1: 0.5000
  - [education = 10th] -> Precision: 0.6000, Recall: 0.2500, F1: 0.3529
  - [education = Doctorate] -> Precision: 0.8364, Recall: 0.8070, F1: 0.8214
  - [education = 12th] -> Precision: 0.4000, Recall: 0.4000, F1: 0.4000
  - [education = 1st-4th] -> Precision: 0.0000, Recall: 1.0000, F1: 0.0000
  - [education = Preschool] -> Precision: 1.0000, Recall: 1.0000, F1: 1.0000
  - Slice-based evaluation shows variations in performance across education levels. Example: F1 for `Bachelors` was higher than for `HS-grad`.

---

## Evaluation Data

- **Dataset**: Test split (20%) from the cleaned UCI Adult Census dataset.
- **Motivation**: Dataset is widely used, accessible, and relevant for income prediction tasks.
- **Preprocessing**:
  - Removed whitespaces
  - One-hot encoding for categorical features
  - Label binarization for target variable ("salary")

---

## Training Data

- **Dataset**: Training split (80%) from the same UCI Adult Census dataset.
- **Preprocessing**:
  - Same as evaluation data
  - Features were selected based on domain relevance

---

## Quantitative Analyses

- **Unitary results**:
  - Performance is reported for slices of the `education` feature.
  - `slice_output.txt` contains detailed precision, recall, and F1 score per category.

- **Intersectional results**:
  - Not analyzed for this project, but future work may evaluate combinations such as race + sex or marital-status + education.

---

## Ethical Considerations

- **Sensitive data**:
  - Model uses protected attributes like race and sex, which may reflect societal biases in the training data.

- **Human life**:
  - Not intended to impact human life or critical decision-making.

- **Risks**:
  - Using this model in employment, housing, or healthcare contexts could cause unfair treatment or discrimination.
  - Model trained on historical data that may include systemic biases.

- **Mitigations**:
  - Slice evaluations were conducted to highlight potential performance disparities.

---

## Caveats and Recommendations

- Results are specific to the UCI dataset and do not generalize beyond it.
- Model not tested across intersectional demographics.
- Additional fairness evaluations (e.g., equalized odds) are recommended for real-world applications.
- Suggested improvements:
  - Use of fairness-aware algorithms
  - Stratified sampling to balance underrepresented groups
  - Conducting additional testing on synthetic or real-world diverse datasets
