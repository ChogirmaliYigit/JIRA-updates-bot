from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import db


inline_keyboard = [[
    InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
    InlineKeyboardButton(text="❌ No", callback_data='no')
]]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


inline_keyboard = [[
    InlineKeyboardButton(text="JIRA ni ulash", callback_data="integrate_jira"),
]]
main_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


async def get_jira_webhook_events(selected_events: list = [], done: bool = False):
    all_events = await db.select_all_events()
    keyboard = []
    for index in range(0, len(all_events), 2):
        event1_title = all_events[index].get("title")
        event1_code = all_events[index].get("code")
        if event1_code in selected_events:
            event1_title += " ✅"
            event1_code += "_selected"
        event2_title = all_events[index+1].get("title")
        event2_code = all_events[index+1].get("code")
        if event2_code in selected_events:
            event2_title += " ✅"
            event2_code += "_selected"
        keyboard.append([
            InlineKeyboardButton(text=event1_title, callback_data=event1_code),
            InlineKeyboardButton(text=event2_title, callback_data=event2_code)
        ])
    if done:
        keyboard.append([InlineKeyboardButton(text="Bo'ldi", callback_data="done")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
