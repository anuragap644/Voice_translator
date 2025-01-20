import tkinter as tk
from tkinter import messagebox
import googletrans
import speech_recognition as sr
import gtts
import playsound

# Initialize the recognizer
recognizer = sr.Recognizer()

def translate_speech():
    try:
        with sr.Microphone() as source:
            status_label.config(text="Speak now...", fg="blue")
            window.update()
            voice = recognizer.listen(source)
            status_label.config(text="Recognizing...", fg="blue")
            window.update()
            text = recognizer.recognize_google(voice, language=input_lang)
            input_textbox.delete(1.0, tk.END)
            input_textbox.insert(tk.END, text)
            status_label.config(text="Translating...", fg="blue")
            window.update()
            
            translator = googletrans.Translator()
            translation = translator.translate(text, dest=output_lang)
            output_textbox.delete(1.0, tk.END)
            output_textbox.insert(tk.END, translation.text)
            
            converted_audio = gtts.gTTS(translation.text, lang=output_lang)
            converted_audio.save("translated_audio.mp3")
            playsound.playsound("translated_audio.mp3")
            
            status_label.config(text="Translation Complete", fg="green")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Error occurred", fg="red")

# Languages
input_lang = "hi"
output_lang = "fr"

# GUI Setup
window = tk.Tk()
window.title("Voice Translator")

# Widgets
instruction_label = tk.Label(window, text="Click the button and speak", font=("Arial", 14))
instruction_label.pack(pady=10)

translate_button = tk.Button(window, text="Start Translation", command=translate_speech, font=("Arial", 14))
translate_button.pack(pady=10)

input_textbox_label = tk.Label(window, text="Recognized Text", font=("Arial", 12))
input_textbox_label.pack(pady=5)
input_textbox = tk.Text(window, height=5, width=50, font=("Arial", 12))
input_textbox.pack(pady=5)

output_textbox_label = tk.Label(window, text="Translated Text", font=("Arial", 12))
output_textbox_label.pack(pady=5)
output_textbox = tk.Text(window, height=5, width=50, font=("Arial", 12))
output_textbox.pack(pady=5)

status_label = tk.Label(window, text="", font=("Arial", 12))
status_label.pack(pady=5)

# Run the GUI loop
window.mainloop()
