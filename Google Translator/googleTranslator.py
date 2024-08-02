from googletrans import Translator, LANGUAGES
from googletrans.models import Translated

lang= list(LANGUAGES.values())
print("Welcome To Google translate")
inputText= input("Please Enter Any Text in English:\n")
outLang=input("Please Enter Output Language (e.g. Urdu, Punjabi, Hindi, German,.....):\n").lower()
if outLang not in lang:
    print("Sorry, Language Not Supported")
else:
    translator = Translator()
    translated = translator.translate(text=inputText, src="english",dest=outLang)
    translated = str(translated).split(", ")
    converted = translated[2]
    pro = translated[3]
    print(converted)
    print(pro)

