import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import pyttsx3
import speech_recognition as sr

# Initialize translator & TTS engine
translator = Translator()
engine = pyttsx3.init()

language_list = list(LANGUAGES.values())


# ===============================
# Functions
# ===============================
def translate_text():
    try:
        input_text = source_text.get("1.0", tk.END).strip()
        src_lang = source_lang.get()
        dest_lang = target_lang.get()

        if not input_text:
            messagebox.showwarning(
                "Input Missing", "Please enter some text to translate."
            )
            return

        src_code = list(LANGUAGES.keys())[language_list.index(src_lang)]
        dest_code = list(LANGUAGES.keys())[language_list.index(dest_lang)]

        translated = translator.translate(input_text, src=src_code, dest=dest_code)
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


def speak_text():
    text = translated_text.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showinfo("No Text", "Please translate some text first.")


def listen_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            messagebox.showinfo("Speak Now", "Please speak into the microphone...")
            audio = recognizer.listen(source, timeout=5)
            spoken_text = recognizer.recognize_google(audio)
            source_text.delete("1.0", tk.END)
            source_text.insert(tk.END, spoken_text)
        except sr.WaitTimeoutError:
            messagebox.showwarning("Timeout", "You didn't speak in time.")
        except sr.UnknownValueError:
            messagebox.showerror(
                "Could Not Understand", "Could not understand the audio."
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))


def on_enter(e):
    translate_button.config(bg="#1c8adb")


def on_leave(e):
    translate_button.config(bg="#3498db")


def toggle_theme():
    if theme_btn.config("text")[-1] == "Dark Mode":
        apply_dark_theme()
        theme_btn.config(text="Light Mode")
    else:
        apply_light_theme()
        theme_btn.config(text="Dark Mode")


def apply_dark_theme():
    root.configure(bg="#2c3e50")
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.configure(bg="#2c3e50", fg="white")
    translated_text.configure(bg="#34495e", fg="white")
    source_text.configure(bg="#34495e", fg="white")


def apply_light_theme():
    root.configure(bg="#f2f2f2")
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.configure(bg="#f2f2f2", fg="black")
    translated_text.configure(bg="#ecf0f1", fg="black")
    source_text.configure(bg="white", fg="black")


# ===============================
# GUI Setup
# ===============================
root = tk.Tk()
root.title("Smart Language Translator")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

label_font = ("Segoe UI", 12)
title_font = ("Segoe UI", 16, "bold")

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground="white", background="white")

# Title
tk.Label(
    root, text="Smart Language Translator", font=title_font, bg="#f2f2f2", fg="#2c3e50"
).pack(pady=10)

# Language Selection Frame
frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

tk.Label(frame, text="Source Language:", font=label_font, bg="#f2f2f2").grid(
    row=0, column=0, padx=10, pady=5, sticky="e"
)
source_lang = ttk.Combobox(frame, values=language_list, width=25)
source_lang.set("english")
source_lang.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Target Language:", font=label_font, bg="#f2f2f2").grid(
    row=1, column=0, padx=10, pady=5, sticky="e"
)
target_lang = ttk.Combobox(frame, values=language_list, width=25)
target_lang.set("french")
target_lang.grid(row=1, column=1, pady=5)

# Input Text Area
tk.Label(root, text="Enter Text:", font=label_font, bg="#f2f2f2").pack()
source_text = tk.Text(root, height=6, width=90, font=("Segoe UI", 11))
source_text.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

translate_button = tk.Button(
    btn_frame,
    text="Translate",
    font=("Segoe UI", 12, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    padx=15,
    pady=5,
    command=translate_text,
)
translate_button.grid(row=0, column=0, padx=10)
translate_button.bind("<Enter>", on_enter)
translate_button.bind("<Leave>", on_leave)

listen_button = tk.Button(
    btn_frame,
    text="🎤 Speak",
    font=("Segoe UI", 12),
    bg="#27ae60",
    fg="white",
    command=listen_voice,
)
listen_button.grid(row=0, column=1, padx=10)

tts_button = tk.Button(
    btn_frame,
    text="🔊 Read Aloud",
    font=("Segoe UI", 12),
    bg="#9b59b6",
    fg="white",
    command=speak_text,
)
tts_button.grid(row=0, column=2, padx=10)

theme_btn = tk.Button(
    btn_frame,
    text="Dark Mode",
    font=("Segoe UI", 12),
    bg="#95a5a6",
    fg="black",
    command=toggle_theme,
)
theme_btn.grid(row=0, column=3, padx=10)

# Output Text Area
tk.Label(root, text="Translated Text:", font=label_font, bg="#f2f2f2").pack()
translated_text = tk.Text(root, height=6, width=90, font=("Segoe UI", 11), bg="#ecf0f1")
translated_text.pack(pady=5)

# Start GUI loop
root.mainloop()
