
class ChatMessage:
    def __init__(self, text, role):
        self.text = text
        self.role = role


class UserChatMessage:
    def __init__(self, text):
        self.text = text
        self.role = "user"


class BotChatMessage:
    def __init__(self, text):
        self.text = text
        self.role = "bot"


class SystemChatMessage:
    def __init__(self, text):
        self.text = text
        self.role = "system"


class Conversation:
    class State:
        def __init__(self, messages):
            self.messages = messages

        @property
        def json(self):
            return self.messages

    def __init__(self, messages):
        self.state = self.State(messages)

    def add_message(self, message):
        self.state.messages.append(message)

    def pop_message(self):
        return self.state.messages.pop(0)
