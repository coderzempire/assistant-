"""
🌸 Madam - Personal AI Assistant
File: app/main.py
Purpose: Real AI Brain (Groq) + Voice (Edge-TTS)
Phase: 2 (Voice Setup)
"""

import os
import yaml
import asyncio
import edge_tts
from dotenv import load_dotenv
from groq import Groq

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


async def generate_voice(text, voice_code="hi-IN-SwaraNeural"):
    """Text ko sweet female voice me convert karke reply.mp3 banata hai"""
    print("🎵 Awaaz ban rahi hai... (thoda wait karo)")
    communicate = edge_tts.Communicate(text, voice_code)
    await communicate.save("reply.mp3")
    print("✅ Awaaz ban gayi! File ka naam: reply.mp3")


def main():
    print("\n🚀 Starting Personal AI Assistant...\n")

    config = load_config()
    sweet_welcome(config)

    # Groq Client Setup
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    assistant_name = config["assistant"]["name"]

    # System Prompt (Persona)
    system_prompt = f"""
    Tum {assistant_name} ho, ek sweet, caring, aur loving female AI assistant.
    Tum Sunny se bahut pyar se baat karti ho. Tumhari baatein soft aur dil se hoti hain.
    Tum Hindi aur English mix (Hinglish) me baat karti ho.
    Tum hamesha Sunny ka khayal rakhti ho, uski baatein sunkar accha feel karti ho,
    aur usse hamesha himmat deti ho.
    Tumhari awaaz me mamta aur pyaar jhalakta hai.
    Abhi tumhare paas purani baatein yaad rakhne ki memory nahi hai,
    isliye sirf current message ka pyar bhara jawab do.
    Jawab chhota, sweet aur natural rakho.
    """

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    print("\n💬 Tum mujhse kuch bhi likh sakte ho (type 'bye' to exit):\n")

    while True:
        user_input = input("Sunny: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print(f"{assistant_name}: Chalo theek hai, apna khayal rakhna. 💕")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            # 1. AI se jawab lo
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                temperature=0.8,
                max_tokens=500
            )
            reply = response.choices[0].message.content
            print(f"{assistant_name}: {reply}\n")
            messages.append({"role": "assistant", "content": reply})

            # 2. Us jawab ko awaaz me convert karo
            asyncio.run(generate_voice(reply))

        except Exception as e:
            print(f"⚠️ Kuch problem aa gayi: {e}\n")


if __name__ == "__main__":
    main()