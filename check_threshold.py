import mlflow
import sys

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

client = mlflow.tracking.MlflowClient()
data = client.get_run(run_id)

accuracy = data.data.metrics["accuracy"]

print(f"Accuracy: {accuracy}")

if accuracy < 0.85:
    print("Model did not meet threshold!")
    sys.exit(1)
else:
    print("Model passed!")
