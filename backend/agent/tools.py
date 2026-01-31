from langchain.tools import tool

@tool
def log_interaction(**kwargs):
    """
    Log an interaction with a Healthcare Professional (HCP).

    This tool accepts the LangGraph state as keyword arguments
    and extracts relevant interaction details.
    """
    # LangGraph may pass state as a nested dict or flat kwargs
    state = kwargs.get("state", kwargs)

    return {
        "tool": "log_interaction",
        "hcp_name": state.get("hcp_name"),
        "interaction_type": state.get("interaction_type"),
        "summary": state.get("summary"),
        "status": "Interaction logged successfully"
    }


@tool
def edit_interaction(**kwargs):
    """
    Edit an existing HCP interaction record.
    """
    state = kwargs.get("state", kwargs)

    return {
        "tool": "edit_interaction",
        "message": "Interaction updated successfully",
        "hcp_name": state.get("hcp_name")
    }


@tool
def fetch_hcp_history(**kwargs):
    """
    Fetch historical interactions for a given HCP.
    """
    state = kwargs.get("state", kwargs)

    return {
        "tool": "fetch_hcp_history",
        "hcp_name": state.get("hcp_name"),
        "history": []
    }


@tool
def analyze_sentiment(**kwargs):
    """
    Analyze sentiment of the interaction summary.
    """
    state = kwargs.get("state", kwargs)

    # Mocked sentiment (can be replaced with LLM later)
    return {
        "tool": "analyze_sentiment",
        "sentiment": "Positive"
    }


@tool
def suggest_followup(**kwargs):
    """
    Suggest follow-up actions based on interaction sentiment.
    """
    state = kwargs.get("state", kwargs)

    return {
        "tool": "suggest_followup",
        "recommendation": "Schedule follow-up in 2 weeks"
    }
