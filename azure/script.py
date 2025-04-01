import requests
import json

API_KEY = "chave_privada"
ENDPOINT = "endpoint_privado"
LANGUAGE_API_URL = f"{ENDPOINT}/text/analytics/v3.0/sentiment"

input_file = "inputs/sentences.txt"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        sentences = file.readlines()
    

    documents = {"documents": [{"id": str(i+1), "language": "pt", "text": sentence.strip()} for i, sentence in enumerate(sentences)]}
    
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(LANGUAGE_API_URL, headers=headers, data=json.dumps(documents))
    result = response.json()

    for doc in result.get("documents", []):
        print(f"Frase: {sentences[int(doc['id']) - 1].strip()}")
        print(f"Sentimento: {doc['sentiment']}")
        print("-" * 40)

except Exception as e:
    print(f"Erro: {e}")
