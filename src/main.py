import autogen
from autogen import config_list_from_json
from dotenv import load_dotenv

from agents import get_code_expert, get_researcher, get_product_manager, get_user_proxy

load_dotenv()


def main() -> None:
    config_list = config_list_from_json(env_or_file='OAI_CONFIG_LIST')
    llm_config = {'config_list': config_list, 'seed': 42, 'request_timeout': 120}

    # Create agents
    user_proxy = get_user_proxy(config_list=config_list)
    researcher = get_researcher(config_list=config_list)
    code_expert = get_code_expert(config_list=config_list)
    pm = get_product_manager(config_list=config_list)

    # Set-up chat
    groupchat = autogen.GroupChat(agents=[user_proxy, pm, researcher, code_expert], messages=[])
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # Get the initial task and start the conversation
    task_msg = input('Task to implement: ')
    user_proxy.initiate_chat(
        manager,
        message=task_msg,
    )


if __name__ == '__main__':
    main()
