# config.py

# Clé secrète OpenRouter
OPENROUTER_API_KEY = "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"

# Nom de ton app / usage
APP_NAME = "chatbot-malagasy"

# Référant obligatoire pour OpenRouter (mettre l'URL où tourne ton app)
REFERER_URL = "http://127.0.0.1:8000/"

# Modèle choisi (supportant mieux le malgache que Mistral)
MODEL = "meta-llama/llama-3-8b-instruct"

# System prompt : consigne au bot
SYSTEM_PROMPT = "Mamaly amin'ny teny malagasy tsotra ianao. Aza mampiasa teny vahiny raha tsy ilaina."
