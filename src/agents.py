from autogen import AssistantAgent, UserProxyAgent
from langchain.tools import format_tool_to_openai_function

from tools import fetch_tool, search_tool


def get_code_expert(config_list: dict) -> AssistantAgent:
    return AssistantAgent(
        name='code-expert',
        system_message='You are a code expert, that is able to program and review Python and JS code; Reply TERMINATE when your task is done',
        code_execution_config={'last_n_messages': 2, 'work_dir': 'output', 'use_docker': True},
        llm_config={
            'functions': _get_functions(),
            'config_list': config_list,
        },
        function_map=_get_functions_map(),
    )


def get_user_proxy(config_list: dict):
    return UserProxyAgent(
        name='user-proxy',
        human_input_mode='ALWAYS',
        llm_config={
            'config_list': config_list,
        },
        function_map=_get_functions_map(),
    )


def get_researcher(config_list: dict):
    return AssistantAgent(
        name='researcher',
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
        format_tool_to_openai_function(search_tool),
        format_tool_to_openai_function(fetch_tool),
    ]


def _get_functions_map() -> dict:
    return {
        search_tool.name: search_tool._run,
        fetch_tool.name: fetch_tool._run,
    }
