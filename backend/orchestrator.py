"""
Orchestrator Engine (Core)
--------------------------
Executes workflow steps sequentially using mock connectors.
Each connector returns output data, which becomes the context
for the next step.

Example input workflow:
{
  "steps": [
    {"tool": "gmail_mock", "action": "fetch_emails"},
    {"tool": "llm_summarize", "action": "summarize"},
    {"tool": "notion_mock", "action": "create_page"}
  ]
}
"""

import json
from typing import Dict, Any, List

# Import mock connectors
from connectors.gmail_mock import gmail_mock
from connectors.notion_mock import notion_mock
from connectors.llm_summarize import llm_summarize

# ----------------------------------------------------------------------

def execute_workflow(workflow: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes a workflow step-by-step using mock connectors.
    Returns a dictionary containing logs and final output.
    """
    print("🚀 Executing workflow...")
    print(json.dumps(workflow, indent=2))
    steps: List[Dict[str, str]] = workflow.get("steps", [])
    context = {}
    logs = []
    print("steps:", steps)

    for idx, step in enumerate(steps, start=1):
        tool = step.get("tool")
        action = step.get("action")

        log_entry = {"step": idx, "tool": tool, "action": action}

        try:
            if tool == "gmail_mock":
                result = gmail_mock()
            elif tool == "llm_summarize":
                result = llm_summarize(context)
            elif tool == "notion_mock":
                result = notion_mock(context)
            else:
                result = f"⚠️ Unknown tool: {tool}"
            print(f"🤖 Executed step {tool}: {result}")
            log_entry["result"] = result
            context[tool] = result

        except Exception as e:
            print(f"❌ Error executing step {tool}: {e}")
            log_entry["error"] = str(e)
            logs.append(log_entry)
            break

        logs.append(log_entry)

    return {
        "status": "completed",
        "steps_executed": len(logs),
        "logs": logs,
        "final_context": context
    }

# ----------------------------------------------------------------------

if __name__ == "__main__":
    # Example run for quick testing
    sample_workflow = {
        "steps": [
            {"tool": "gmail_mock", "action": "fetch_emails"},
            {"tool": "llm_summarize", "action": "summarize"},
            {"tool": "notion_mock", "action": "create_page"}
        ]
    }
    
    result = execute_workflow(sample_workflow)
    print(json.dumps(result, indent=2))
