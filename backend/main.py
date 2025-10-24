from fastapi import FastAPI, Body
from llm_generator import generate_workflow

app = FastAPI()

@app.post("/generate")
def generate_endpoint(payload: dict = Body(...)):
    goal = payload.get("goal", "")
    plan = generate_workflow(goal)
    return {"workflow": plan}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)