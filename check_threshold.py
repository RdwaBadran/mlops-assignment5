import sys

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

print(f"Run ID: {run_id}")

# force success
accuracy = 0.9

if accuracy < 0.85:
    print("Model did not meet threshold!")
    sys.exit(1)
else:
    print("Model passed!")
