def psychological_risk(face, voice):

    if face == "Sad" and voice == "Sad":
        return "Possible prolonged sadness indicators"

    if face == "Angry" and voice == "Angry":
        return "Possible anxiety related indicators"

    if face == "Fear" and voice == "Fearful":
        return "Possible panic or fear response"

    if face == "Neutral" and voice == "Neutral":
        return "Emotionally stable state"

    return "No strong psychological risk detected"