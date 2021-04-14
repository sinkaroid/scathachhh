import logging, json, requests, sys

from aiogram import Bot, Dispatcher, executor, types
from core import decorator, api

async def fgo():
    async def process_start_command(message: types.Message):
        try:
            await bot.send_message(message.from_user.id, fgo())
            logger.info(cmd + decorator.successMsg())

        except Exception as e:
            await message.answer(decorator.occurred() + '{}'.format(e))
            logger.info(e)