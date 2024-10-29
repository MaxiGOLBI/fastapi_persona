from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

# Modelo de Persona
class Persona(BaseModel):
    id: Optional[int] = None
    user: str
    persona: str

app = FastAPI()
persona_db = []

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "API de Personas funcionando correctamente"}

# Crear una nueva persona
@app.post("/persona/", response_model=Persona)
def create_persona(persona: Persona):
    persona.id = len(persona_db) + 1
    persona_db.append(persona)
    return persona


#ver persona por id
@app.get("/personas/{persona_id}", response_model=Persona)
def obtener_persona(persona_id: int)
    if persona.id == persona_id:
        return persona
    raise HTTPExeptiom(status_code=404, detail="Persona no encontrada")

#Listar personas
@app.get("/personas/", response_model=Persona)
def lsitar_persona():
    return

# Obtener una persona por ID
@app.get("/persona/{persona_id}", response_model=Persona)
def get_persona(persona_id: int):
    for persona in persona_db:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona not found")

# Actualizar una persona existente
@app.put("/persona/{persona_id}", response_model=Persona)
def update_persona(persona_id: int, persona_updated: Persona):
    for index, persona in enumerate(persona_db):
        if persona.id == persona_id:
            persona_db[index] = persona_updated
            persona_db[index].id = persona_id  # Mantiene el mismo ID
            return persona_db[index]
    raise HTTPException(status_code=404, detail="Persona not found")

# Eliminar una persona por ID
@app.delete("/persona/{persona_id}", response_model=dict)
def delete_persona(persona_id: int):
    for index, persona in enumerate(persona_db):
        if persona.id == persona_id:
            del persona_db[index]  # Elimina la persona de la lista
            return {"message": "Persona deleted"}
    raise HTTPException(status_code=404, detail="Persona not found")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")  # Asegúrate de tener este archivo en "static/"


