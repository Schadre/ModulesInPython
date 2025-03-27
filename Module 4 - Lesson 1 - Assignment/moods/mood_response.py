"""Problem Statement: 
Create a Python program using a custom module that asks 
the user how they are feeling today and responds with a 
custom message based on the mood entered. """

def mood_response(mood):
    if mood == "happy":
        return "You deserve to be this happy, please wallow in the feeling."
    elif mood == "sad":
        return "I am so sorry you are feeling this way. It will get better..."
    elif mood == "angry": 
        return "Don't hide from your anger, sit with why you are angry and don't be afraid to process the uncomfortable emotions."
    elif mood == "calm":
        return "A very good state to mediate in."
    else:
        return "Let's look into this particular a bit more.."


