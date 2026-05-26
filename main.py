# Enterprise-AI-Meeting-Assistant/main.py

from src.meeting_engine import analyze_meeting


meeting_transcript = """
Project Manager:
The client requested the AI dashboard delivery by next Friday.

Data Engineer:
The data pipeline integration is completed.

ML Engineer:
Model accuracy improved to 94 percent after retraining.

Security Lead:
We still need security approval before deployment.

Project Manager:
John will prepare deployment documents.

Security Lead:
Sarah will coordinate final compliance checks.

Project Manager:
Final deployment meeting scheduled for Thursday.
"""


result = analyze_meeting(meeting_transcript)

print("\nMEETING ANALYSIS:\n")

print(result)