from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.agent.graph import agent

app = FastAPI(title="AIVOA AI CRM HCP")

# ---------------- CORS CONFIG ----------------
# Allows React (localhost:3000) to talk to FastAPI (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- ROOT API ----------------
@app.get("/")
def root():
    return {"message": "Backend running successfully"}

# ---------------- LOG INTERACTION API ----------------
@app.post("/log-interaction")
def log_interaction_api(payload: dict):
    """
    Receives interaction data from React frontend
    and sends it to LangGraph agent.
    """
    try:
        result = agent.invoke(payload)
        return result
    except Exception as e:
        # Safe error handling (prevents 500 crash)
        return {
            "error": "Agent execution failed",
            "details": str(e)
        }
