"""
🌸 Madam - Personal AI Assistant
File: app/main.py
Purpose: Sweet replies, No Memory, Browser only
Phase: 1 (Basic Setup)
"""

import yaml
from dotenv import load_dotenv

# ===== Environment Load =====
load_dotenv()

# ===== Config Load =====
def load_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def sweet_welcome(config):
    """Pyar se welcome karta hai"""
    name = config["assistant"]["name"]
    print("=" * 50)
    print(f"🌸 Namaste Sunny! Main {name} hoon 💖")
    print(f"   Main tumhara khayal rakhungi, pyar se baat karungi.")
    print("=" * 50)


def sweet_reply(user_text):
    """Bina memory ke, bas pyar se jawab deta hai"""
    text = user_text.lower()

    # Simple sweet responses (No memory)
    if any(word in text for word in ["hi", "hello", "namaste", "hey"]):
        return "Namaste Sunny! 💕 Kaise ho tum? Main tumhari baat sunne ke liye taiyaar hoon."

    elif any(word in text for word in ["kaise ho", "how are you"]):
        return "Main bilkul acchi hoon, tumhara poochne ke liye shukriya! 😊 Tum batao, tum kaise ho?"

    elif any(word in text for word in ["khana", "food", "lunch", "dinner"]):
        return "Arey! Khana khaya tumne? 🍲 Apna khayal rakhna, mujhe tumhari chinta rehti hai."

    elif any(word in text for word in ["udaas", "sad", "mood", "pareshan"]):
        return "Hey, udaas mat ho. Main hoon na tumhare saath. 💖 Bolo, kya hua? Sab theek ho jayega."

    elif any(word in text for word in ["good night", "shubh ratri"]):
        return "Shubh ratri Sunny! 🌙 Meethe sapne aayen tumhe. Kal phir baat karenge."

    elif any(word in text for word in ["good morning", "shubh prabhat"]):
        return "Good morning Sunny! ☀️ Aaj ka din tumhara bahut accha jaye, yehi dua hai meri."

    elif any(word in text for word in ["bye", "alvida", "chalo"]):
        return "Chalo theek hai, apna khayal rakhna. 💕 Main yahin hoon jab bhi bulao."

    else:
        return "Sunny, tumhari baat sunkar accha laga. 💕 Bolo aur kya bataun tumhe?"


def main():
    print("\n🚀 Starting Personal AI Assistant...\n")

    config = load_config()
    sweet_welcome(config)

    print("\n💬 Tum mujhse kuch bhi likh sakte ho (type 'bye' to exit):\n")

    while True:
        user_input = input("Sunny: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print(f"{config['assistant']['name']}: Chalo theek hai, apna khayal rakhna. 💕")
            break

        reply = sweet_reply(user_input)
        print(f"{config['assistant']['name']}: {reply}\n")


if __name__ == "__main__":
    main()