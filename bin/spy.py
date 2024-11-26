import pyttsx3

def pyttsx3_tts(text):
    """
    Text-to-Speech using pyttsx3 (offline method)
    Pros: Works offline, cross-platform
    Cons: Limited voice quality
    """
    engine = pyttsx3.init()
    
    # Optional: Adjust speech properties
    engine.setProperty('rate', 150)    # Speech rate
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

pyttsx3_tts("Hello")