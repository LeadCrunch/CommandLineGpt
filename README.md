# CommandLineGpt

A project from Rev Engineering

## Setup

### 1. create a virtual environment and install dependencies

```bash
python -m venv env
```

```bash
source env/bin/activate
pip install -r requirements.txt
```

### 2. configure your .env file (copy example.env)

```bash
cp example.env .env
```

- add your API key
- set your default model
- set your default temperature
- adjust the message history if you have issues with hitting token limits

## Usage

Run the command line app by running the main file with python

```bash
python main.py
```

Note: there is a current limitation of maintaining a conversation state of 20 messages. This a workaround to avoid the token limit. This means as you chat with the GPT api, it will start "forgetting" messages beyond 20 messages ago. This value can be adjusted in the .env file. In the future I may update this to use actual token counts to avoid hitting the token limit. 