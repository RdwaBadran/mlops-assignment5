import mlflow

# Read Run ID
with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

# Get run data
client = mlflow.tracking.MlflowClient()
run = client.get_run(run_id)

accuracy = run.data.metrics.get("accuracy", 0)

print(f"Model accuracy: {accuracy}")

# Check threshold
if accuracy < 0.85:
    raise Exception("Accuracy below threshold! Failing pipeline.")
else:
    print("Model passed threshold!")
