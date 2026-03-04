import random

calm_responses = [
    "You seem relaxed today. Keep maintaining your balance.",
    "Your emotional state appears stable. Keep going.",
    "You look calm and composed."
]

stress_responses = [
    "You may be experiencing some stress. Try taking a deep breath.",
    "Consider taking a short break and relaxing your mind.",
    "A short pause or breathing exercise might help."
]

distress_responses = [
    "You seem to be under high stress.",
    "It might help to talk with someone you trust.",
    "Consider relaxation techniques or professional support."
]

def get_response(state):

    if "Calm" in state:
        return random.choice(calm_responses)

    if "Mild" in state or "Moderate" in state:
        return random.choice(stress_responses)

    if "High" in state:
        return random.choice(distress_responses)

    return "Stay mindful of your emotional health."