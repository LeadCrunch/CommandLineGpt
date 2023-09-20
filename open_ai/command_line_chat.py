from open_ai.llm_api import OpenAiLlmApi, OpenAiLlmOptions, OpenAiChatMessages
from entities.conversation import Conversation, UserChatMessage
from config.main import openai_default_model, openai_default_temperature, openai_max_message_history_length


class OpenAiCommandLineChat:
    def __init__(self, few_shot_messages=[]):
        self.openai_llm_api = OpenAiLlmApi(OpenAiLlmOptions(openai_default_model, float(openai_default_temperature)))
        self.conversation = Conversation(few_shot_messages)

    def start(self):
        while True:
            user_input = input("You: ")
            self.conversation.add_message(UserChatMessage(user_input))
            messages = self.conversation.state.messages
            response = self.openai_llm_api.get_chat_completion(
                chat_messages=OpenAiChatMessages(messages),
            )
            message = response.choices[0].message.content
            print("AI: " + message)
            self.conversation.add_message(message)
            if (len(messages) > int(openai_max_message_history_length)):
                self.conversation.pop_message()
