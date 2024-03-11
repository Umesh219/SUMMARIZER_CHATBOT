from T5DialogueSummarizer import T5DialogueSummarizer

# Define your test dialogue (agent and user conversation about an order)
test_dialogue = [
    "Agent: Hi there! How can I help you today?",
    "User: Hello, I placed an order yesterday for a new phone case. Can you give me an update on the delivery?",
    "Agent: Sure, let me check. Your order (ID: 12345) is currently being processed and is expected to be shipped within 2 business days.",
    "User: Great, thanks for letting me know! Do you have a tracking number for the shipment yet?",
    "Agent: Unfortunately, a tracking number won't be available until your order is shipped. You'll receive an email notification with the tracking information once it's on its way."
]

# Create T5DialogueSummarizer object
summarizer = T5DialogueSummarizer()

# Generate summary
summary = summarizer.summarize_dialogue(test_dialogue)

print(f"Dialogue:\n{test_dialogue[0]}\n{' | '.join(test_dialogue[1:])}")
print(f"\nSummary: {summary}")