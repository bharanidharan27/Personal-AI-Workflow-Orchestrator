def notion_mock(context):
    summary = context.get("llm_summarize", "No summary available.")
    print("📝 Storing summary to Notion mock...")
    return f"Created Notion page with content: {summary}"
