import mlflow

with mlflow.start_run() as run:
    run_id = run.info.run_id

    # training code here

    with open("model_info.txt", "w") as f:
        f.write(run_id)
