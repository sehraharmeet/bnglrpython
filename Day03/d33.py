import uuid

def create_user(name):
    return {
        "user_id": str(uuid.uuid4()),
        "name": name
    }

print(create_user("Harmeet"))