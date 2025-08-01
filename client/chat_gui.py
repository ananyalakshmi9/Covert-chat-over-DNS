# client/chat_gui.py
import tkinter as tk
from tkinter import scrolledtext
import dns.resolver
from utils import encode_message

# ✅ Use a safer domain (not .local)
SERVER_DOMAIN = "dnschat.test"

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Covert DNS Chat")
        self.root.geometry("500x400")

        # Display area
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.chat_display = scrolledtext.ScrolledText(self.display_frame, state='disabled', wrap=tk.WORD, font=("Arial", 12))
        self.chat_display.pack(fill=tk.BOTH, expand=True)

        # Input area
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.entry = tk.Entry(self.input_frame, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        msg = self.entry.get().strip()
        if msg:
            self.display_chat("You", msg)
            response = self.send_dns_query(msg)
            self.display_chat("Server", response)
            self.entry.delete(0, tk.END)

    def display_chat(self, sender, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.yview(tk.END)

    def send_dns_query(self, message):
        try:
            encoded = encode_message(message)
            domain = f"{encoded}.{SERVER_DOMAIN}"
            answers = dns.resolver.resolve(domain, 'TXT', tcp=True)
            return str(answers[0])
        except Exception as e:
            return f"[Error] {e}"

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
