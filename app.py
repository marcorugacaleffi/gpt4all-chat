from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configurare il base path per le richieste API locali
openai.api_base = "http://localhost:4891/v1"
openai.api_key = "not needed for a local LLM"

def chat_with_gpt4all(prompt):
    model = "QuantFactory/Meta-Llama-3-8B-Instruct-GGUF"
    italian_prompt = f"Sei un bot di assistenza tecnica della Caleffi, rispondi sempre in italiano in maniera concisa e professionale. Rispondi solo alla domanda senza aggiungere altro. Fornisci una spiegazione tecnica dettagliata ma non troppo prolissa. La domanda è: {prompt}"
    
    try:
        response = openai.Completion.create(
            model=model,
            prompt=italian_prompt,
            max_tokens=200,
            temperature=0.6,
            top_p=1.0,
            n=1,
            stream=False,
            stop=["\n", "You:", "Assistant:"],
            presence_penalty=0,
            frequency_penalty=0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt', '')
    response = chat_with_gpt4all(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4891)
