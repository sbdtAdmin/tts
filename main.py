

def t2s(text, lang="ru"):
    from gtts import gTTS
    import pygame
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)


t2s("привет! как тебя зовут?", lang="ru")


def speechr(lang="ru"):
    import speech_recognition as sr

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Ожидание звука...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    print("Звук обнаружен!")
    
    try:
        text = r.recognize_google(audio, language=lang)
        print(f"Распознанный текст: {text}")
        return text
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")

speechr()
