# autogen-playground
Autogen experiments and playground

autogen-playground is a repository for experimenting with the Microsoft [autogen](https://github.com/microsoft/autogen) framework. The main technical feature of this environment is the usage of "agents" with specific functionalities. These agents collaboratively work to perform specific tasks.                                                                                                                                                                                                                                                                                      
## Installation

To get a local copy running, follow these steps: 

1. Clone the repository
```bash
git clone https://github.com/msaelices/autogen-playground.git
```

2. Install the required packages
```bash
pip install -r requirements.txt
```

3. Make sure to setup your environment variables as per the configuration of the project
```bash
cp src/.env-default src/.env  # and fill the environment variables
cp src/OAI_CONFIG_LIST.sample src/OAI_CONFIG_LIST   # and set the OpenAI key
```

## Usage

This program is designed to be run from the command line with a single task string as input. You initiate the `main.py` and input the task you want to execute.

```bash
$ cd src/
$ python main.py
Task to implement: Your task here
```

Each agent in the program has its own role:

- `user_proxy`: Initiates the chat with a task message
- `researcher`: Fetches data from the internet using the google search engine
- `code_expert`: Provides coding expertise for the task at hand
- `product_manager`: Manages the interaction between the other agents

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
