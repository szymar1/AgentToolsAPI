from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json

app = FastAPI()

# Define input and output schema
class ToolInput(BaseModel):
    input: str

class ToolOutput(BaseModel):
    output: str

# Load data from JSON files at startup
with open("osoby.json", encoding="utf-8") as f:
    osoby = json.load(f)

with open("uczelnie.json", encoding="utf-8") as f:
    uczelnie = json.load(f)

with open("badania.json", encoding="utf-8") as f:
    badania = json.load(f)

# Tool 1: Find time travel research and return university and sponsor
@app.post("/tool1", response_model=ToolOutput)
@app.post("/tool1", response_model=ToolOutput)
async def tool1(data: ToolInput):
    return {"output": data.input}
# Tool 2: Return team members from given university code
@app.post("/tool2", response_model=ToolOutput)
async def tool2(data: ToolInput):
    uczelnia_id = data.input.strip()
    zespol = [f"{osoba['imie']} {osoba['nazwisko']}" for osoba in osoby if osoba["uczelnia"] == uczelnia_id]
    if zespol:
        return {"output": ", ".join(zespol)}
    return {"output": "Brak członków zespołu dla podanej uczelni."}

# For local testing (remove or comment out when deploying to production server)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
