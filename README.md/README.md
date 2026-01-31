# AIVOA AI-First CRM for HCP Interactions

## Project Overview
This project is an AI-first CRM module designed to manage Healthcare Professional (HCP) interactions.  
The system allows users to log HCP interactions through a frontend interface, process them using an AI agent, and generate intelligent follow-up recommendations.

The main focus of this project is demonstrating agent-based AI workflows using LangGraph and LLM tools.

---

## Tech Stack
- Frontend: React.js, Redux Toolkit
- Backend: FastAPI (Python)
- AI Orchestration: LangGraph
- LLM: Groq (Gemma2-9B-IT)
- API Communication: Axios

---

## Architecture
1. The React frontend collects interaction details from the user.
2. Redux manages the interaction response state.
3. The frontend sends data to the FastAPI backend.
4. A LangGraph agent processes the request.
5. The agent executes multiple tools such as logging interaction, sentiment analysis, and follow-up recommendation.
6. The AI-generated response is sent back to the frontend and displayed.

---

## LangGraph Agent
LangGraph is used as an orchestration layer to manage AI workflow and shared state.  
The agent coordinates the following tools:

- **log_interaction** – Logs the HCP interaction  
- **edit_interaction** – Edits an existing interaction  
- **fetch_hcp_history** – Retrieves past interactions  
- **analyze_sentiment** – Analyzes sentiment of the interaction  
- **suggest_followup** – Recommends next actions  

---

## API Endpoint

### POST `/log-interaction`

### Request Body
```json
{
  "hcp_name": "Dr. Suresh",
  "interaction_type": "Meeting",
  "summary": "Discussed new oncology drug and samples"
}
