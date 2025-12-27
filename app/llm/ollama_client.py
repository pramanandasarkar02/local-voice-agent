import requests

class OllamaClient:
    def __init__(self, model):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def chat(self, prompt):
        res = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        return res.json()["response"]
