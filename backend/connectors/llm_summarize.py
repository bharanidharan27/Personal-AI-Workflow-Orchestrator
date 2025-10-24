def llm_summarize(context):
    emails = context.get("gmail_mock", [])
    summary = " ".join([e["body"] for e in emails])
    print("🧠 Summarized emails.")
    return f"Summary: {summary[:80]}..."
