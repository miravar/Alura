from collections import defaultdict

class MemoryService:
    def __init__(self):
        self.memory = defaultdict(list)

    def add(self, session_id, role, content):
        self.memory[session_id].append({
            "role": role,
            "content": content
        })

    def history(self, session_id):
        return self.memory[session_id]

    def clear(self, session_id):
        self.memory[session_id] = []