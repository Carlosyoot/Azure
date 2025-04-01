Analisador de Texto com Azure AI

📌 Descrição

Este projeto usa o Azure Cognitive Services para analisar frases e determinar o sentimento de cada uma.

📂 Estrutura do Projeto

inputs/ → Contém um arquivo de texto com frases para análise.

script.py → Código Python para chamar a API do Azure.

readme.md → Documentação do projeto.

🚀 Como Usar

Crie um recurso Language Services no Portal Azure.

Copie a chave da API e o endpoint do serviço.

Clone este repositório:

git clone https://github.com/seu-usuario/analisador-texto-azure.git
cd analisador-texto-azure

Instale dependências:

pip install requests

Edite o script.py e substitua ENDPOINT e API_KEY pelos seus valores do Azure.

Execute o script:

python script.py

📊 Exemplo de Resultado

{
  "documents": [
    { "id": "1", "sentiment": "positive" },
    { "id": "2", "sentiment": "negative" }
  ]
}

🔥 Insights e Aprendizados

Aprendi a usar Python com Azure AI para análise de sentimento.

Vi como a IA interpreta emoções em textos e como melhorar o modelo.

Ideias futuras: expandir para análise de emoções específicas (alegria, tristeza, raiva).

