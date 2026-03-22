import subprocess

if __name__ == "__main__":

    subprocess.Popen(["uvicorn", "api_model:app", "--reload", "--port", "8000"])
    subprocess.run(["python", "app.py"])