from dialog import Dialog
from intention import Intention
from conversation import Conversation

from flask import Blueprint, jsonify, request
from flask_cors import CORS

main = Blueprint('main', __name__)
CORS(main, resources={r"/*": {"origins": "*"}})

@main.route('/inteligence', methods=['POST'])
def inteligence():
    objectConversations = request.get_json()
    conversation = Conversation()
    for objectConversation in objectConversations['objectConversations']:
        intention = Intention()

        questions = tuple(objectConversation['questions'])
        responses = tuple(objectConversation['responses'])
        dialog = Dialog(questions, responses, objectConversation['action'])
        intention.insert_dialog(dialog)

        conversation.insert_intention(intention)

    return conversation.get_response(objectConversations['question'], objectConversations['no_responses'])