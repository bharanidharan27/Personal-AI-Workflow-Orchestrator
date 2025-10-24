"""
Goal-to-Workflow Generator (LLM)
--------------------------------
This module converts a natural-language goal into a structured JSON workflow
plan using the OpenAI API.

Example:
Input:  "Summarize my emails and add summary to Notion"
Output: {
    "steps": [
        {"tool": "gmail_mock", "action": "fetch_emails"},
        {"tool": "llm_summarize", "action": "summarize"},
        {"tool": "notion_mock", "action": "create_page"}
    ]
}
"""

import os
import json
from typing import Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from environment
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ----------------------------------------------------------------------

def generate_workflow(goal: str) -> Dict[str, Any]:
    """
    Converts a natural-language goal into a workflow plan.
    """
    if not goal.strip():
        return {"error": "Goal cannot be empty."}

    prompt = f"""
    You are a workflow planner that converts goals into step-based JSON workflows.
    Each step uses one of these mock tools:
    - gmail_mock: fetch emails
    - llm_summarize: summarize content
    - notion_mock: store or create pages

    Example:
    Goal: "Summarize today's emails and add to Notion"
    Output:
    {{
        "steps": [
            {{"tool": "gmail_mock", "action": "fetch_emails"}},
            {{"tool": "llm_summarize", "action": "summarize"}},
            {{"tool": "notion_mock", "action": "create_page"}}
        ]
    }}

    Now create a workflow for this goal:
    "{goal}"
    Return ONLY a valid JSON object with 'steps' list.
    """

    try:
        print("Generate Workflow...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        print("Response Received...")
        text = response.choices[0].message.content.strip()
        # Ensure valid JSON
        if "```" in text:
            text = text.split("```")[1]
            text = text.replace("json", "").strip()

        print("Valid JSON obtained...")

        workflow = json.loads(text)
        print("LLM Works")
        return workflow

    except Exception as e:
        print("⚠️  LLM generation failed:", e)
        # Return a safe fallback workflow
        return {
            "steps": [
                {"tool": "llm_summarize", "action": "summarize"}
            ]
        }

# ----------------------------------------------------------------------
if __name__ == "__main__":
    goal = input("Enter your goal: ")
    plan = generate_workflow(goal)
    print(json.dumps(plan, indent=2))
