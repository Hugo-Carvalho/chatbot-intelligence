# chatbot-intelligence

Api Python Flask para inteligência de chatbots utilizando o cosine similarity

Exemplo de envio do corpo da requisição:

```
{
    "objectConversations": [
        {
            "questions": ["oi", "ola", "opa", "oie", "ei"],
            "responses": ["Ola, tudo bem?", "Oi, como esta?"],
            "action": ""
        },
        {
            "questions": ["sim", "estou", "tudo sim", "estou bem", "estou otimo", "estou perfeito"],
            "responses": ["Que ótimo", "Isso é bom"],
            "action": ""
        },
        {
            "questions": ["não", "não estou", "nada", "nada bem", "estou pessimo", "estou ruim"],
            "responses": ["Que pena, o que posso fazer para ajudar?", "Fiquei triste por você, em que posso ajudar?"],
            "action": ""
        },
        {
            "questions": ["sim e voce?", "sim e vc?", "estou e voce?", "estou e vc?", "tudo sim e voce?", "tudo sim e vc?", "estou bem e voce?", "estou bem e vc?", "estou otimo e voce?", "estou otimo e vc?", "estou perfeito e voce?", "estou perfeito e vc?"],
            "responses": ["Que ótimo, estou bem tambem!", "Tambem estou muito bem!"],
            "action": ""
        },
        {
            "questions": ["não e voce?", "não e vc?", "não estou e voce?", "não estou e vc?", "nada e voce?", "nada e vc?", "nada bem e voce?", "nada bem e vc?", "estou pessimo e voce?", "estou pessimo e vc?", "estou ruim e voce?", "estou ruim e vc?"],
            "responses": ["Agora tambem não estou bem, o que posso fazer para ajudar?", "Fico bem quanto voce esta bem, em que posso ajudar?"],
            "action": ""
        }
    ],
    "question": "oi",
    "no_responses": ["Desculpe, não entendi o que você falou", "Sinto muito, não consegui te entender", "Ops, não entendi o que você disse"]
}
```