# Census Income Prediction API

- project link: https://github.com/mahmoudrezk29/Census_Income_Prediction-API


This project demonstrates an end-to-end MLOps pipeline for deploying a machine learning model using FastAPI and GitHub Actions, with cloud deployment on Render.

The model predicts whether an individual's income exceeds $50K/year based on demographic and employment features from the UCI Census dataset.

---

## 🚀 Features

- Logistic Regression model trained on UCI Census data
- REST API with FastAPI (`GET` and `POST /predict`)
- Categorical feature encoding using `OneHotEncoder` and `LabelBinarizer`
- Slice-level performance reporting (`slice_output.txt`)
- Unit tests for model and API
- Continuous Integration via GitHub Actions
- Continuous Deployment to Render
- Model card compliant with [Model Cards for Model Reporting (Mitchell et al.)](https://arxiv.org/abs/1810.03993)


---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/P4-Udacity-Census-ml-api.git
cd P4-Udacity-Census-ml-api

🐍 2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

📊 Training the Model

python train_model.py

This will:

    Clean and process data

    Train a logistic regression model

    Save the model, encoder, and label binarizer as .pkl files

    Generate slice_output.txt with performance metrics by education level

🧪 Running Tests

pytest
flake8 .

    Includes tests for:

        Model training and inference

        Classification metrics

        API endpoints (GET /, POST /predict for both outcomes)

🌐 Running the API Locally

uvicorn api.main:app --reload

Then open:

    Swagger UI: http://127.0.0.1:8000/docs

    Root greeting: http://127.0.0.1:8000

📸 Required Screenshots (for submission)
File	Description
example.png	Swagger UI showing POST example
continuous_integration.png	GitHub Actions passing CI
continuous_deployment.png	Render deployment auto-deploy toggle
live_get.png	Live browser output from GET /
live_post.png	Terminal output from post_live.py script
☁️ Deployment to Render
✅ Auto Deployment

    Deployed via render.yaml from GitHub

    Continuous Deployment enabled

    URL: https://<your-app-name>.onrender.com

To manually test the live endpoint:

python post_live.py

📄 Model Card

See model_card.md for detailed documentation on:

    Model architecture and training

    Intended use and out-of-scope warnings

    Evaluation metrics and slice analysis

    Ethical considerations

📦 Dependencies

fastapi
uvicorn
pandas
numpy
scikit-learn
joblib
pydantic
requests
pytest
flake8
httpx

✅ Rubric Coverage Summary

    ✅ Git & CI with GitHub Actions

    ✅ Model training, inference, metrics, and slice analysis

    ✅ Unit tests for model and API

    ✅ FastAPI with GET/POST endpoints and schema example

    ✅ Model card with complete sections

    ✅ Cloud deployment with screenshots

📬 License

For educational use only — part of the Udacity MLOps Nanodegree.
