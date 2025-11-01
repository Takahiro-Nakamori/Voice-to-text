import os
import pyaudio
import speech_recognition as sr
from deep_translator import GoogleTranslator

r = sr.Recognizer()
mic = sr.Microphone()

def translate_text(text):
    # Create a Translator object
    translator = Translator()

    # Translate the text
    result = translator.translate(text, src='ja', dest='en')
    # Return the translated text
    return result.text

while True:
    #print("Say something ...")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    #print ("Now to recognize it...")

    try:
        text = r.recognize_google(audio, language='ja-JP')
        print(text)

        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
        print(translated_text)


        # "ストップ" と言ったら音声認識を止める
        #if r.recognize_google(audio, language='ja-JP') == "ストップ" :
        #    print("end")
        #    break

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("".format(e))