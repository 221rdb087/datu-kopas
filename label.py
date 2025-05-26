from label_studio_sdk import Client
import time

ls = Client(
    url="http://localhost:8080",
    api_key="f3c20ec1b4d454338e3e0f25165fd8bd4faef8cc"
)
project = ls.get_project(2)
default_label = "Nepieder" 

tasks = project.get_tasks()
labeled = 0
skipped = 0
failed = 0

for task in tasks:
    task_id = task["id"]

    if task.get("is_labeled"):
        skipped += 1
        continue

    annotation_payload = {
        "result": [
            {
                "from_name": "sentiment",   
                "to_name": "text",          
                "type": "choices",
                "value": {
                    "choices": [default_label]
                }
            }
        ],
        "was_cancelled": False,
        "ground_truth": False,
        "lead_time": 0.5
    }

