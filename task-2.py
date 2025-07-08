import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import scrolledtext
import random
import time
import threading

nltk.download("punkt")

# 🎯 Knowledge Base
knowledge_base = {
    "how can i return a product?": "No worries! You can return a product within 30 days of purchase. Just head over to your account and initiate the return from the 'My Orders' section.",
    "how to track my order?": "You can easily track your order using the tracking link sent to your email. Still can't find it? Let us know, and we'll help you out!",
    "do you ship internationally?": "Yes, we do! We offer international shipping to selected countries. You’ll see shipping options at checkout based on your location.",
    "what payment methods are available?": "We accept debit cards, credit cards, UPI, and digital wallets like Google Pay and PhonePe. Quick and secure!",
    "how long does delivery take?": "Standard delivery takes 3–5 business days, while express delivery gets it to you in just 1–2 days. We work hard to get your goodies to you fast!",
    "can i cancel my order?": "Absolutely. You can cancel your order within 12 hours of placing it. Just go to 'My Orders' and hit 'Cancel'.",
    "what if i received a damaged product?": "Oh no! If your product arrives damaged, please contact our support team within 48 hours. We’ll sort it out ASAP.",
    "do you offer cash on delivery?": "Yes! Cash on delivery is available for orders under ₹5,000. Great for quick and secure purchases.",
    "how do i apply a discount code?": "Got a coupon? Awesome! Just enter your discount code during checkout in the 'Apply Coupon' section to get your savings.",
    "how do i contact customer support?": "We’re here for you! Reach us anytime via the 'Contact Us' page or call 1800-123-456. We typically respond within 24 hours.",
    "can i change my shipping address after ordering?": "Yes, you can—but only within 1 hour of placing your order. Head to 'My Orders' and click 'Edit Address'.",
    "are your products under warranty?": "Yes, every product comes with a minimum 6-month manufacturer warranty. Check the product page for details.",
    "do you offer gift wrapping?": "Sure thing! Gift wrapping is available during checkout for a small extra charge. Perfect for birthdays and special occasions!",
    "where can i find my invoice?": "You can find and download your invoice from the 'My Orders' section in your account. Need help? Just ask!",
    "do you have a mobile app?": "Yes, we do! Download our app from the Google Play Store or Apple App Store for a smoother shopping experience.",
    "can i save items for later?": "Of course! Just click the heart icon next to a product to add it to your wishlist. You can view it anytime from your account.",
    "do you offer any student discounts?": "Yes! We offer exclusive discounts for students. Just verify your student status during checkout to unlock them.",
    "is there a first-time buyer discount?": "Welcome aboard! First-time buyers get 10% off. Use code FIRST10 at checkout to claim your discount.",
    "can i reorder a previous purchase?": "Definitely! Go to 'My Orders' and click 'Reorder' next to any past purchase. Easy and quick!",
}


# 🎯 Preprocess Text
def clean_text(text):
    return text.lower().strip()


# 🎯 Chatbot Engine
class SupportBot:
    def __init__(self, knowledge):
        self.questions = list(knowledge.keys())
        self.answers = list(knowledge.values())
        self.cleaned_questions = [clean_text(q) for q in self.questions]
        self.vectorizer = TfidfVectorizer()
        self.vector_matrix = self.vectorizer.fit_transform(self.cleaned_questions)

    def get_answer(self, user_query):
        user_query_clean = clean_text(user_query)
        query_vector = self.vectorizer.transform([user_query_clean])
        similarity = cosine_similarity(query_vector, self.vector_matrix)
        best_match_index = similarity.argmax()

        # Optional delay to simulate thinking
        time.sleep(random.uniform(0.5, 1.0))

        return self.answers[best_match_index]


# 🎯 GUI App
class ChatBotApp:
    def __init__(self, master):
        self.bot = SupportBot(knowledge_base)
        self.master = master
        self.master.title("ChatBot")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.master.configure(bg="#6A0DAD")  # Purple background

        # Heading
        self.heading = tk.Label(
            master, text="ChatBot", font=("Arial", 20, "bold"), bg="#6A0DAD", fg="white"
        )
        self.heading.place(x=0, y=0, width=500, height=40)

        self.chat_area = scrolledtext.ScrolledText(
            master, wrap=tk.WORD, state="disabled", font=("Arial", 12), bg="#E6E6FA"
        )
        self.chat_area.place(x=20, y=50, width=460, height=370)

        self.user_input = tk.Entry(master, font=("Arial", 14), bg="white")
        self.user_input.place(x=20, y=440, width=360, height=30)
        self.user_input.bind("<Return>", self.handle_enter)

        self.send_button = tk.Button(
            master,
            text="Send",
            font=("Arial", 12),
            bg="white",
            command=self.send_message,
        )
        self.send_button.place(x=400, y=440, width=80, height=30)

        self.add_bot_message("Hello! I can help you. Type 'exit' to leave.")

    def add_bot_message(self, message):
        self.chat_area["state"] = "normal"
        self.chat_area.insert(tk.END, f"Bot: {message}\n")
        self.chat_area["state"] = "disabled"
        self.chat_area.see(tk.END)

    def add_user_message(self, message):
        self.chat_area["state"] = "normal"
        self.chat_area.insert(tk.END, f"You: {message}\n")
        self.chat_area["state"] = "disabled"
        self.chat_area.see(tk.END)

    def send_message(self):
        user_text = self.user_input.get().strip()
        if user_text == "":
            return

        self.add_user_message(user_text)
        self.user_input.delete(0, tk.END)

        if user_text.lower() == "exit":
            self.add_bot_message("Goodbye! Have a nice day.")
            self.master.after(1000, self.master.quit)
            return

        threading.Thread(target=self.respond, args=(user_text,)).start()

    def handle_enter(self, event):
        self.send_message()

    def respond(self, user_text):
        reply = self.bot.get_answer(user_text)
        self.add_bot_message(reply)


# 🎯 Run the GUI
if __name__ == "__main__":
    window = tk.Tk()
    app = ChatBotApp(window)
    window.mainloop()
