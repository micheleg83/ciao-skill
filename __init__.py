from mycroft import MycroftSkill, intent_file_handler


class Ciao(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ciao.intent')
    def handle_ciao(self, message):
        self.speak_dialog('ciao')


def create_skill():
    return Ciao()

