from autogen import AssistantAgent, UserProxyAgent

from tools import search


def get_code_expert(llm_config: dict) -> AssistantAgent:
     return AssistantAgent(
        name='code-expert',
        system_message='You are a code expert, you can use search function to search for code snippets; Reply TERMINATE when your task is done',
        llm_config=llm_config,
     )


def get_user_proxy():
    return UserProxyAgent(
        name='user-proxy',
        code_execution_config={'last_n_messages': 2, 'work_dir': 'output', 'use_docker': True},
        human_input_mode='TERMINATE',
        function_map={
            'search': search,
        }
    )


def get_product_manager(llm_config: dict) -> AssistantAgent:
    return AssistantAgent(
        name='product-manager',
        system_message='You are a product manager, you will help break down the initial idea into a well scoped requirement for the coder; Do not involve in future conversations or error fixing',
        llm_config=llm_config,
    )
