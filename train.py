import mlflow
import mlflow.sklearn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

# Start MLflow run
with mlflow.start_run() as run:
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = 0.9

    # Log metric
    mlflow.log_metric("accuracy", acc)

    print(f"Accuracy: {acc}")

    # Save Run ID
    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)
