from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI(title="Hello World API", description="A simple FastAPI project with multiple endpoints", version="1.0")

# In-memory data store (for demo)
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}

# ----------------------------
# Root Endpoint
# ----------------------------
@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "Hello, World!"

# ----------------------------
# Health Check
# ----------------------------
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Server is running fine!"}

# ----------------------------
# Get all users
# ----------------------------
@app.get("/users")
def get_users():
    return {"users": list(users.values())}

# ----------------------------
# Get a single user by ID
# ----------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

# ----------------------------
# Add a new user
# ----------------------------
@app.post("/users")
def add_user(user: dict):
    if not user.get("name") or not user.get("email"):
        raise HTTPException(status_code=400, detail="Name and email are required")
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = user
    return {"message": "User added successfully", "user_id": new_id}

# ----------------------------
# Update user details
# ----------------------------
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id].update(updated_user)
    return {"message": "User updated successfully", "user": users[user_id]}

# ----------------------------
# Delete a user
# ----------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users.pop(user_id)
    return {"message": "User deleted successfully", "deleted": deleted_user}