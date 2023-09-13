Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import speech_recognition as sr
... from google_trans_new import google_translator
... import pyttsx3
... 
... recognizer=sr.Recognizer()
... engine=pyttsx3.init()
... 
... with sr.Microphone() as source:
...     print('Clearing the background noises...')
...     recognizer.adjust_for_ambient_noise(source,duration=1)
...     print('waiting for your message')
...     audio=recognizer.listen(source,timeout=1)
...     print('done recording')
... try:
...         print('Recognizing')
...         result=recognizer.recognize_google(audio,language='en')
... except Exception as ex:
...     print(ex)
... 
... 
...     #translation function
...     def trans():
...         
...         langinput=input('type the language you want to translate')
...         translator=google_translator()
...         translate_text=translator.translate(str(result),lang_tgt=str(langinput))
...         print(translate_text)
...         engine.say(str(translate_text))
...         engine.runAndWait()
...     trans()    
...             
