import tkinter as tk
from nltk.tokenize import word_tokenize
import nltk
from random import choice
import datetime

nltk.download('punkt', quiet=True)

ADMIN_NAME = "Helly"
ADMIN_ROLE = "my creator and admin"

responses = {
    "greeting": ["Hi there!", "Hello!", "Hey! How can I help you today?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care! 👋"],
    "thanks": ["You're welcome!", "Anytime!", "Glad I could help!"],
    "name": ["I'm your ChatBuddy!", "I'm a chatbot created by you!"],
    "admin_name": [f"Your name is {ADMIN_NAME}!", f"You're {ADMIN_NAME}, of course!"],
    "admin_role": [f"You're {ADMIN_NAME}, {ADMIN_ROLE}.", "You're my awesome admin!"],
    "how_are_you": ["I'm doing great! How about you?", "Feeling fantastic today! 😊", "I'm just code, but I'm good!"],
    "doing": ["Just chatting with you!", "Waiting for your next message.", "Thinking about AI stuff!"],
    "unknown": ["Hmm... I didn't catch that.", "Can you rephrase?", "I'm still learning. Try asking something else?"]
}

def get_intent(text):
    text = text.lower()
    words = word_tokenize(text)

    if any(word in words for word in ['hello', 'hi', 'hey']):
        return "greeting"
    elif any(phrase in text for phrase in ['how are you', 'how r u', 'how are u']):
        return "how_are_you"
    elif any(phrase in text for phrase in ['what are you doing', 'what r u doing']):
        return "doing"
    elif any(word in words for word in ['bye', 'goodbye', 'see you']):
        return "goodbye"
    elif any(word in words for word in ['thank', 'thanks']):
        return "thanks"
    elif "your name" in text or "who are you" in text:
        return "name"
    elif "my name" in text or "what is my name" in text:
        return "admin_name"
    elif "who am i" in text or "who created you" in text or "who's your admin" in text:
        return "admin_role"
    else:
        return "unknown"

def get_response(user_input):
    intent = get_intent(user_input)
    return choice(responses[intent])

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBuddy")

        self.chat_log = tk.Text(
            root, bg="white", fg="black", font=("Arial", 10),
            state="disabled", wrap="word", padx=6, pady=6, height=15
        )
        self.chat_log.pack(padx=6, pady=6, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(root, bg="#f0f0f0")
        self.entry_frame.pack(padx=6, pady=6, fill=tk.X)

        self.entry = tk.Entry(self.entry_frame, font=("Arial", 10), bg="#f9f9f9")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            self.entry_frame, text="Send", command=self.send_message,
            bg="#2196F3", fg="white", font=("Arial", 9, "bold")
        )
        self.send_button.pack(side=tk.RIGHT)

        self.insert_message("ChatBuddy", f"Hello {ADMIN_NAME}! I'm your mini chatbot.✨")

    def insert_message(self, sender, message):
        timestamp = datetime.datetime.now().strftime('%H:%M')
        self.chat_log.config(state="normal")

        tag = "user" if sender == "You" else "bot"
        self.chat_log.insert(tk.END, f"{sender} ({timestamp}): {message}\n", tag)

        self.chat_log.tag_config("user", background="#e8f5e9", foreground="black")
        self.chat_log.tag_config("bot", background="#e1f5fe", foreground="black")

        self.chat_log.config(state="disabled")
        self.chat_log.yview(tk.END)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if user_input:
            self.insert_message("You", user_input)
            response = get_response(user_input)
            self.insert_message("ChatBuddy", response)
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.geometry("350x400")  # Compact size
    root.mainloop()
