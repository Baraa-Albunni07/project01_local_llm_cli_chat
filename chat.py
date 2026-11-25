from openai import OpenAI

# Verbindet sich mit einem lokalen Modell-Server (z. B. Ollama auf Port 11434)
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="lokal-kein-key-noetig"
)

messages = [
    {"role": "system", "content": "Du bist ein präziser, hilfreicher KI-Assistent."}
]

print("Lokaler Chat gestartet ('exit' zum Beenden):")
while True:
    user_input = input("\nDu: ")
    if user_input.lower() in {"exit", "quit"}:
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama3.2",  # Passe den Namen an dein lokal installiertes Modell an
            messages=messages,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"KI: {reply}")
    except Exception as e:
        print(f"Verbindungsfehler zum lokalen Server: {e}")