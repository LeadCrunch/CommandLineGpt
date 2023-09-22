from app.gpt_intention_detection import GptIntentionDetection
from api.open_ai_llm import OpenAiLlmApi, OpenAiLlmOptions
from config.main import (
    openai_default_model,
    openai_default_temperature,
    openai_max_message_history_length,
)
from entities.conversation import Conversation, UserChatMessage
from entities.intention import Intention
from entities.command_line_app import CommandLineApp


class CommandLineEventLoop:
    def __init__(self, command_line_app):
        self.command_line_app = command_line_app

    def start(self, tick):
        while True:
            tick()


class GptBuddyCommandLineApp(CommandLineApp):
    def __init__(self, few_shot_messages=[]):
        self.openai_llm_api = OpenAiLlmApi(
            OpenAiLlmOptions(openai_default_model, float(openai_default_temperature))
        )
        self.conversation = Conversation(few_shot_messages)
        self.intentions = [
            Intention(
                "accept", "confirms, accepts, or agrees with the previous message"
            ),
            Intention(
                "reject", "rejects, declines, or disagrees with the previous message"
            ),
            Intention("answer", "answers a question"),
        ]

    def start(self):
        event_loop = CommandLineEventLoop(self)
        event_loop.start(self.handle_input)

    def handle_input(self):
        user_input = input("You: ")
        self.conversation.add_message(UserChatMessage(user_input))
        user_intention = self._get_user_intention()
        self._process_user_intention(user_intention)

    def _process_user_intention(self, user_intention):
        self._print_chat_response(user_intention)

    def _print_chat_response(self, chat_response_text):
        print("AI: " + chat_response_text)

    def _truncate_message_history(self):
        if len(self.conversation.state.messages) > int(
            openai_max_message_history_length
        ):
            self.conversation.pop_message()

    def _get_user_intention(self):
        intention_detection = GptIntentionDetection(self.conversation.state.messages, self.intentions)
        return intention_detection.get_intention_of_last_message_using_llm_api()
