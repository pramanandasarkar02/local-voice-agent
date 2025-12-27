class Memory:
    def __init__(self):
        self.history = []

    def add(self, user, ai):
        self.history.append(f"User: {user}\nAI: {ai}")

    def context(self):
        return "\n".join(self.history[-5:])
