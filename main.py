from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# lista para guardar los usuarios
users = []

# modelo de usuario
class User(BaseModel):
    name: str
    email: str

# endpoint usando POST para agregar usuario
@app.post("/add-user/")
def add_user(user:User):
    users.append(user)
    return {"message": "Usuario registrado con éxito", "user": user}

# endpoint usando GET para traer los usuarios
@app.get("/get-users/")
def get_users():
    return {"users": users}

#cambio




