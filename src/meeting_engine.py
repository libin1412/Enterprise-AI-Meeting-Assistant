# Enterprise-AI-Meeting-Assistant/src/meeting_engine.py

from src.llm_helper import generate_response


def analyze_meeting(transcript):

    prompt = f"""
    You are an enterprise AI Meeting Assistant.

    Analyze the following meeting transcript.

    STRICTLY generate:

    1. Meeting Summary
    2. Key Discussion Points
    3. Decisions Made
    4. Action Items
    5. Risks or Blockers
    6. Next Steps

    Format professionally.

    Meeting Transcript:
    {transcript}
    """

    response = generate_response(prompt)

    return response