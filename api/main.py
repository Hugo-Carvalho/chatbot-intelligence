from dialog import Dialog
from intention import Intention
from conversation import Conversation

def chatbot():

    conversation = Conversation()

    saudacao = Intention()

    questions = ("oi", "ola", "opa", "oie", "ei")
    responses = ("Ola, tudo bem?", "Oi, como esta?")
    dialog = Dialog(questions, responses, """""")
    saudacao.insert_dialog(dialog)

    questions = ("sim", "estou", "tudo sim", "estou bem", "estou otimo", "estou perfeito")
    responses = ("Que ótimo", "Isso é bom")
    dialog = Dialog(questions, responses, """""")
    saudacao.insert_dialog(dialog)

    questions = ("não", "não estou", "nada", "nada bem", "estou pessimo", "estou ruim")
    responses = ("Que pena, o que posso fazer para ajudar?", "Fiquei triste por você, em que posso ajudar?")
    dialog = Dialog(questions, responses, """""")
    saudacao.insert_dialog(dialog)

    questions = ("sim e voce?", "sim e vc?", "estou e voce?", "estou e vc?", "tudo sim e voce?", "tudo sim e vc?", "estou bem e voce?", "estou bem e vc?", "estou otimo e voce?", "estou otimo e vc?", "estou perfeito e voce?", "estou perfeito e vc?")
    responses = ("Que ótimo, estou bem tambem!", "Tambem estou muito bem!")
    dialog = Dialog(questions, responses, """""")
    saudacao.insert_dialog(dialog)

    questions = ("não e voce?", "não e vc?", "não estou e voce?", "não estou e vc?", "nada e voce?", "nada e vc?", "nada bem e voce?", "nada bem e vc?", "estou pessimo e voce?", "estou pessimo e vc?", "estou ruim e voce?", "estou ruim e vc?")
    responses = ("Agora tambem não estou bem, o que posso fazer para ajudar?", "Fico bem quanto voce esta bem, em que posso ajudar?")
    dialog = Dialog(questions, responses, """""")
    saudacao.insert_dialog(dialog)

    conversation.insert_intention(saudacao)

    matematica = Intention()

    questions = ("Quanto que é 123456789+-*/", "Qual o resultado de 123456789+-*/")
    responses = ("Acertei? rsrs", "Esta certo?")
    dialog = Dialog(questions, responses, """
import re
print(eval(re.sub('[^0-9+\-*\/]*', '', INPUT)))
    """)
    matematica.insert_dialog(dialog)

    questions = ("sim", "isso mesmo")
    responses = ("Isso foi facil, rsrs", "Foi tranquilo")
    dialog = Dialog(questions, responses, """""")
    matematica.insert_dialog(dialog)

    conversation.insert_intention(matematica)

    while(True):
        print(conversation.get_response(input("Fala comigo -> ")))

if __name__ == '__main__':
    chatbot()