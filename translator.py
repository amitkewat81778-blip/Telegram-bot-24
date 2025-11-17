from googletrans import Translator
translator = Translator()

def to_hindi(text):
    try:
        return translator.translate(text, dest='hi').text
    except:
        return text
