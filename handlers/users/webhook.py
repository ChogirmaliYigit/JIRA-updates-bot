from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from states.states import UserState
from keyboards.inline.buttons import get_jira_webhook_events


router = Router()


@router.callback_query(UserState.integrate_jira)
async def integrate(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("JIRA akkauntingizning username'ini kiriting")
    await state.set_state(UserState.get_jira_username)


@router.message(UserState.get_jira_username)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data({"jira_username": message.text})
    await message.answer("Endi API token kiriting")
    await state.set_state(UserState.get_jira_api_token)


@router.message(UserState.get_jira_api_token)
async def get_api_token(message: types.Message, state: FSMContext):
    await state.update_data({"jira_api_token": message.text})
    await message.answer("Webhook uchun ixtiyoriy nom kiriting")
    await state.set_state(UserState.get_webhook_name)


@router.message(UserState.get_webhook_name)
async def get_webhook_name(message: types.Message, state: FSMContext):
    await state.update_data({"webhook_name": message.text})
    await message.answer("JIRA proyektingizning nomini kiriting")
    await state.set_state(UserState.get_jira_project_instance)


@router.message(UserState.get_jira_project_instance)
async def get_project_instance(message: types.Message, state: FSMContext):
    await state.update_data({"jira_project_instance": message.text})
    await message.answer("Proyekt maxsus kalitini kiriting")
    await state.set_state(UserState.get_jira_project_key)


@router.message(UserState.get_jira_project_key)
async def get_project_key(message: types.Message, state: FSMContext):
    await state.update_data({"jira_project_key": message.text})
    await message.answer("Qaysi holatlarda o'zgarishlarni qabul qilmoqchisiz?", reply_markup=await get_jira_webhook_events())
    await state.set_state(UserState.get_webhook_events)


@router.callback_query(UserState.get_webhook_events)
async def select_or_unselect_events(call: types.CallbackQuery, state: FSMContext):
    event_code, is_selected = call.data.split("_")
    call.message.reply_markup
    if is_selected:
        await call.message.edit_reply_markup(reply_markup=await get_jira_webhook_events())
