from dotenv import load_dotenv
import os

load_dotenv()

openai_default_model = os.getenv('OPENAI_DEFAULT_MODEL')
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_default_temperature = os.getenv('OPENAI_DEFAULT_TEMPERATURE')
openai_max_message_history_length = os.getenv('OPENAI_MAX_MESSAGE_HISTORY_LENGTH')
