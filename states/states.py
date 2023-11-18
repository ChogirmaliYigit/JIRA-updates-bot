from aiogram.filters.state import StatesGroup, State


class AdminState(StatesGroup):
    are_you_sure = State()
    ask_ad_content = State()


class UserState(StatesGroup):
    integrate_jira = State()
    get_jira_username = State()
    get_jira_api_token = State()
    get_webhook_name = State()
    get_jira_project_instance = State()
    get_jira_project_key = State()
    get_webhook_events = State()
