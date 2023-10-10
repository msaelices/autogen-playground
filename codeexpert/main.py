import autogen
from autogen import config_list_from_json

from agents import get_code_expert, get_product_manager, get_user_proxy

def main() -> None:
    config_list = config_list_from_json(env_or_file='OAI_CONFIG_LIST')
    llm_config = {'config_list': config_list, 'seed': 42, 'request_timeout': 120}

    # Create agents
    user_proxy = get_user_proxy()
    code_expert = get_code_expert(llm_config=llm_config)
    pm = get_product_manager(llm_config=llm_config)

    # Set-up chat
    groupchat = autogen.GroupChat(
        agents=[user_proxy, code_expert, pm], messages=[])
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    task_msg = input('Task to implement: ')
    # Start the conversation
    user_proxy.initiate_chat(
        manager,
        message=task_msg,
    )


if __name__ == '__main__':
    main()