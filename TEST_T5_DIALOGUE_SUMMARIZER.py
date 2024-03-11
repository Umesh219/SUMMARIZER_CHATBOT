from T5DialogueSummarizer import T5DialogueSummarizer

# Create T5DialogueSummarizer object
summarizer = T5DialogueSummarizer()



# Define  test dialogue
test_dialogue = [
    "Hi, how are you doing today?",
    "Great, thanks for asking! What can I do for you?",
    "I'm looking for information on machine learning.",
    "Sure, I can help you with that. What specifically are you interested in learning about machine learning?"
]

# Generate summary
summary = summarizer.summarize_dialogue(test_dialogue)


print(f"\nSummary: {summary}")
