from fastapi import FastAPI, Body
from llm_generator import generate_workflow
from orchestrator import execute_workflow

app = FastAPI()

@app.post("/generate")
def generate_endpoint(payload: dict = Body(...)):
    goal = payload.get("goal", "")
    plan = generate_workflow(goal)
    return {"workflow": plan}

@app.post("/execute")
def execute_endpoint(payload: dict = Body(...)):
    workflow = payload.get("workflow", {})
    result = execute_workflow(workflow)
    return result

@app.post("/run")
def run_goal(payload: dict = Body(...)):
    goal = payload.get("goal", "")
    workflow = generate_workflow(goal)
    result = execute_workflow(workflow)
    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)