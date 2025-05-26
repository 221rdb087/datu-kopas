from label_studio_sdk import Client
import os
import time

ls = Client(
    url="http://localhost:8080",
    api_key="f3c20ec1b4d454338e3e0f25165fd8bd4faef8cc"
)
project = ls.get_project(2)

folder_path = r"C:\Users\gusta\Desktop\cyrus1"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        task_payload = {
            "data": {
                "text": content,
                "file_name": filename
            }
        }

        try:
            project.import_tasks([task_payload])
            print(f"pievienots no {filename}")
            time.sleep(0.01)
        except Exception as e:
            print(f"neizdevas pievienot {filename}: {e}")

print("\faili pievienoti")
