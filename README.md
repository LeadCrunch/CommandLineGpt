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


## Creating a shell script to run as an alias

Here are some instructions if you want to run this in your terminal without having to cd to the project, create the venv, and run the python script

### 1. create a shell script like the following

```ssh
#!/bin/bash

# Step 1: Navigate to your project's directory
cd /path/to/your/project/CommandLineGpt

# Step 2: Activate the virtual environment (however you have your venv setup)
source env/bin/activate

# Step 3: Run the Python script
python main.py
```

### add the alias to your .bashrc or .zshrc

```
alias chatgpt="/path/to/shell/script/commandlinegpt.sh"
```