import torch
from transformers import pipeline
import speech_recognition as sr
import pyttsx3
import cv2
import datetime
import wikipedia

# Carrega modelos NLP (usar GPU se disponível)
device = 0 if torch.cuda.is_available() else -1
nlp = pipeline("text-generation", model="gpt2", device=device)
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", device=device)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

# Inicializa TTS (texto para fala)
engine = pyttsx3.init()
engine.setProperty('rate', 160)

# Fala
def speak(text):
    print("IA:", text)
    engine.say(text)
    engine.runAndWait()

# Escuta
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='pt-BR')
        print("Você:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Desculpe, não entendi.")
        return ""
    except sr.RequestError:
        speak("Erro de conexão.")
        return ""

# Tira uma foto com a webcam
def capture_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        filename = "foto_ia.jpg"
        cv2.imwrite(filename, frame)
        cam.release()
        speak("Foto capturada.")
    else:
        speak("Erro ao acessar a câmera.")

# Inteligência principal
def process_command(cmd):
    if "horas" in cmd or "hora" in cmd:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Agora são {now}")
    elif "pesquise" in cmd:
        topic = cmd.replace("pesquise", "").strip()
        result = wikipedia.summary(topic, sentences=2, auto_suggest=False)
        speak(result)
    elif "resuma" in cmd:
        text = cmd.replace("resuma", "").strip()
        summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
        speak(summary[0]['summary_text'])
    elif "responda" in cmd:
        speak("Qual é a pergunta?")
        question = listen()
        context = "O que você quiser usar como base de conhecimento"
        result = qa(question=question, context=context)
        speak(result["answer"])
    elif "escreva um texto" in cmd:
        prompt = cmd.replace("escreva um texto", "").strip()
        result = nlp(prompt, max_length=100, num_return_sequences=1)
        speak(result[0]['generated_text'])
    elif "foto" in cmd:
        capture_image()
    elif "sair" in cmd:
        speak("Até logo!")
        exit()
    else:
        speak("Comando não reconhecido.")

# Loop principal
def main():
    speak("Assistente inteligente ativado.")
    while True:
        comando = listen()
        if comando:
            process_command(comando)

if __name__ == "__main__":
    main()
📦 Requisitos (instale com pip)
bash
Copiar
Editar
pip install torch torchvision torchaudio
pip install transformers
pip install speechrecognition pyttsx3
pip install opencv-python
pip install wikipedia
pip install pyaudio  # Pode precisar instalar via apt ou brew
