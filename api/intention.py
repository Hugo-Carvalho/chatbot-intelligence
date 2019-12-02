
class Intention:

    def __init__(self):
        self.dialogs = []

    def insert_dialog(self, dialog):
        self.dialogs.append(dialog)

    def get_dialogs(self):
        return self.dialogs