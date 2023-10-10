from autogen import AssistantAgent, UserProxyAgent

from tools import search, fetch


def get_code_expert(config_list: dict) -> AssistantAgent:
     return AssistantAgent(
        name='code-expert',
        system_message='You are a code expert, you can use search function to search for code snippets; Reply TERMINATE when your task is done',
        llm_config={
            'config_list': config_list,
        },
        function_map=_get_functions_map(),
     )


def get_user_proxy(config_list: dict):
    return UserProxyAgent(
        name='user-proxy',
        code_execution_config={'last_n_messages': 2, 'work_dir': 'output', 'use_docker': True},
        human_input_mode='ALWAYS',
        llm_config={
            'config_list': config_list,
        },
        function_map={
            'search': search,
            'fetch': fetch,
        }
    )


def get_researcher(config_list: dict):
    return AssistantAgent(
        name='github-researcher',
        system_message='You are a researcher, you can use search function to search for code snippets or whatever information we need; Reply TERMINATE when your task is done',
        llm_config={
            'functions': _get_functions(),
            'config_list': config_list,
        },
        function_map=_get_functions_map(),
    )


def get_product_manager(config_list: dict) -> AssistantAgent:
    return AssistantAgent(
        name='product-manager',
        system_message='You are a product manager, you will help break down the initial idea into a well scoped requirement for the coder; Do not involve in future conversations or error fixing',
        llm_config={
            'functions': _get_functions(),
            'config_list': config_list,
        },
    )


# ----- Auxiliary --------------------------------

def _get_functions() -> list:
    return [
        {
            'name': 'search',
            'description': 'google search for relevant information',
            'parameters': {
                'type': 'object',
                'properties': {
                    'query': {
                        'type': 'string',
                        'description': 'Google search query',
                    }
                },
                'required': ['query'],
            },
        },
        {
            'name': 'fetch',
            'description': 'Fetch website content based on URL',
            'parameters': {
                'type': 'object',
                'properties': {
                    'url': {
                        'type': 'string',
                        'description': 'Website url to scrape',
                    }
                },
                'required': ['url'],
            },
        },
    ]

def _get_functions_map() -> dict:
    return {
        'search': search,
        'fetch': fetch,
    }