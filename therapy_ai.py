import random

questions = [
    "How are you feeling today?",
    "Have you been feeling stressed recently?",
    "Did something happen that made you upset?",
    "How has your sleep been lately?",
    "Do you feel anxious or worried often?"
]

responses = {
    "sad": [
        "I'm sorry you're feeling this way.",
        "Talking to someone you trust may help.",
        "Taking small breaks can sometimes help improve mood."
    ],

    "angry":[
        "Try taking slow deep breaths.",
        "A short walk might help calm your mind.",
        "It's okay to take time to relax."
    ],

    "fear":[
        "You're safe right now.",
        "Try grounding yourself by focusing on your breathing."
    ],

    "neutral":[
        "You seem emotionally stable.",
        "Keep maintaining your mental balance."
    ]
}

def ask_question():
    return random.choice(questions)

def give_response(emotion):

    emotion = emotion.lower()

    if emotion in responses:
        return random.choice(responses[emotion])

    return "Tell me more about how you feel."