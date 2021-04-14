import logging, json, requests, sys, random

from aiogram import Bot, Dispatcher, executor, types
from Scathachgram.core import api, decorator
from traxex import upcoming, ongoing, ended
from scathach import gif, jav, twitter, fgo, netorare, ugly_man

scathachBase = api.scathach_api()
API_TOKEN = api.tokenBot()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
scathaDP = Dispatcher(bot)
logger = logging.getLogger()
ks = decorator.splitBoy()

@scathaDP.message_handler(commands=['start', 'help', 'h'])
async def send_welcome(message: types.Message):
    await message.answer(decorator.ngaturHelp().read(), parse_mode='Markdown')

@scathaDP.message_handler(commands=['alias', 'al'])
async def send_welcome(message: types.Message):
    await message.answer(decorator.ngaturAli().read(), parse_mode='Markdown')


@scathaDP.message_handler(commands=['gel', 'gelbooru'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        contents = requests.get(f'{scathachBase}/{api.gelbooru()}/?tags={message.get_args()}').json()
        getItem = contents['url']
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + message.get_args())
        else:
            await bot.send_message(message.from_user.id, text=getItem)
            logger.info(decorator.successMsg() + message.get_args())

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['rule', 'r34'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        contents = requests.get(f'{scathachBase}/{api.r34()}/?tags={message.get_args()}').json()
        getItem = contents['url']
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + message.get_args())
        else:
            await bot.send_message(message.from_user.id, text=getItem)
            logger.info(decorator.successMsg() + message.get_args())

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['loli', 'lolibooru'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        contents = requests.get(f'{scathachBase}/{api.loli()}/?tags={message.get_args()}').json()
        getItem = contents['url']
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + message.get_args())
        else:
            await bot.send_message(message.from_user.id, text=getItem)
            logger.info(decorator.successMsg() + message.get_args())

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['yande', 'yandere'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        contents = requests.get(f'{scathachBase}/{api.yande()}/?tags={message.get_args()}').json()
        getItem = contents['url']
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + message.get_args())
        else:
            await bot.send_message(message.from_user.id, text=getItem)
            logger.info(decorator.successMsg() + message.get_args())

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['twitter', 'tw'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        contents = requests.get(f'{scathachBase}/{api.tuit()}/?tags={message.get_args()}').json()
        getItem = contents['url']
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + message.get_args())
        else:
            await bot.send_message(message.from_user.id, text=getItem)
            logger.info(decorator.successMsg() + message.get_args())

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['rb', 'realbooru'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        contents = requests.get(f'{scathachBase}/{api.rb()}/?tags={message.get_args()}').json()
        getItem = contents['url']
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + message.get_args())
        else:
            await bot.send_message(message.from_user.id, text=getItem)
            logger.info(decorator.successMsg() + message.get_args())

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['kona', 'konachan'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        contents = requests.get(f'{scathachBase}/{api.kona()}/?tags={message.get_args()}').json()
        getItem = contents['url']
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + message.get_args())
        else:
            await bot.send_message(message.from_user.id, text=getItem)
            logger.info(decorator.successMsg() + message.get_args())

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['hentai'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        contents = requests.get(f'https://nekos.life/api/v2/img/{message.get_args()}').json()
        try:
            getItem = contents['url']
            await bot.send_animation(message.from_user.id, getItem)
            logger.info(decorator.successMsg() + message.get_args())

        except:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + message.get_args())
    else:
        await message.answer(decorator.ngaturArgs() + "\n" + decorator.nekos())


@scathaDP.message_handler(commands=['crypto', 'coin'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        spell = message.get_args().lower()
        contents = requests.get(f'{scathachBase}/{api.crypto()}/?tags={spell}').json()
        getCoin = contents['coin']
        if not getCoin:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag())
            logger.info(decorator.badrequestMsg() + spell)
        else:
            await message.answer(getCoin)
            logger.info(decorator.successMsg() + spell)

    else:
        await message.answer(decorator.ngaturArgs())


def rand_purr():
    possible = ['anal', 'blowjob', 'cum', 'fuck', 'neko', 'pussylick', 'solo', 'threesome_fff',
                'threesome_ffm', 'threesome_mmf', 'yaoi', 'yuri']
    return random.choice(possible)

@scathaDP.message_handler(commands=['purr', 'purrgif'])
async def process_start_command(message: types.Message):

        contents = requests.get(f'https://purrbot.site/api/img/nsfw/{rand_purr()}/gif').json()
        try:
            getItem = contents['link']
            await bot.send_animation(message.from_user.id, getItem)
            logger.info(decorator.successMsg())

        except Exception as e:
            await message.answer(decorator.occurred() + '{}'.format(e))


def rand_neko():
    possible = ['hass', 'hmidriff', 'pgif', '4k', 'hentai', 'holo',
                'hneko', 'neko', 'hkitsune', 'kemonomimi', 'anal',
                'hanal', 'gonewild','kanna', 'ass', 'pussy', 'thigh', 'hthigh',
                'gah', 'paizuri', 'tentacle', 'boobs', 'hboobs', 'yaoi']
    return random.choice(possible)

@scathaDP.message_handler(commands=['neko', 'nekos', 'nekobot'])
async def process_start_command(message: types.Message):
        cmd = message.text+" "
        contents = requests.get(f'https://nekobot.xyz/api/image?type={rand_neko()}').json()
        try:
            getItem = contents['message']
            await bot.send_message(message.from_user.id, getItem)
            logger.info(cmd + decorator.successMsg() + decorator.randObj())

        except:
            pass


@scathaDP.message_handler(commands=['ongoing'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    try:
        await message.answer(ongoing(), parse_mode='Markdown')
        logger.info(cmd + decorator.successMsg())

    except Exception as e:
        await message.answer(decorator.occurred() + '{}'.format(e))


@scathaDP.message_handler(commands=['upcoming'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    try:
        await message.answer(upcoming(), parse_mode='Markdown')
        logger.info(cmd + decorator.successMsg())

    except Exception as e:
        await message.answer(decorator.occurred() + '{}'.format(e))


@scathaDP.message_handler(commands=['ended'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    try:
        await message.answer(ended(), parse_mode='Markdown')
        logger.info(cmd + decorator.successMsg())

    except Exception as e:
        await message.answer(decorator.occurred() + '{}'.format(e))
        logger.info(e)


@scathaDP.message_handler(commands=['sex', 'gif'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    try:
        await bot.send_animation(message.from_user.id, gif())
        logger.info(cmd + decorator.successMsg())

    except Exception as e:
        await message.answer(decorator.occurred() + '{}'.format(e))
        logger.info(e)


@scathaDP.message_handler(commands=['jav'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    try:
        await bot.send_photo(message.from_user.id, jav())
        logger.info(cmd + decorator.successMsg())

    except Exception as e:
        await message.answer(decorator.occurred() + '{}'.format(e))
        logger.info(e)


@scathaDP.message_handler(commands=['fgo'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    try:
        await bot.send_message(message.from_user.id, fgo())
        logger.info(cmd + decorator.successMsg())

    except Exception as e:
        await message.answer(decorator.occurred() + '{}'.format(e))
        logger.info(e)


@scathaDP.message_handler(commands=['ugly', 'uglybastard'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    try:
        await bot.send_message(message.from_user.id, ugly_man())
        logger.info(cmd + decorator.successMsg())

    except Exception as e:
        await message.answer(decorator.occurred() + '{}'.format(e))
        logger.info(e)


@scathaDP.message_handler(commands=['ntr', 'netorare'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    try:
        await bot.send_message(message.from_user.id, netorare())
        logger.info(cmd + decorator.successMsg())

    except Exception as e:
        await message.answer(decorator.occurred() + '{}'.format(e))
        logger.info(e)

def rand_cos():
    possible = [ 'ass', 'bikini', 'boots', 'cleavage', 'glasses', 'kemonomimi', 'maid', 'panties' ]
    return random.choice(possible)


@scathaDP.message_handler(commands=['cosplay', 'cosp'])
async def process_start_command(message: types.Message):
    cmd = message.text+ks
    contents = requests.get(f'http://192.145.238.5/~pasirm5/v3/sessyoin/{rand_cos()}').json()
    try:
        getItem = contents['url']
        await bot.send_photo(message.from_user.id, getItem)
        logger.info(cmd + decorator.successMsg() + decorator.randObj())

    except:
        pass


@scathaDP.message_handler(commands=['hero', 'herostats'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        text = message.get_args().replace(" ", "_")
        heroesName = text.title()
        for r in (("Of", "of"), ("The", "the")):
            heroesName = heroesName.replace(*r)

        contents = requests.get(f'{scathachBase}/herostats/?tags={heroesName}').json()
        getItem = contents['url']
        gb = f'https://www.dotabuff.com/assets/heroes/{text.replace("_","-").lower()}.jpg'
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag() + decorator.badHero())
            logger.info(decorator.badrequestMsg() + heroesName)
        else:
            await bot.send_photo(message.from_user.id, photo=gb, caption=getItem)
            logger.info(decorator.successMsg() + heroesName)

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['talent', 'herotalent'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        text = message.get_args().replace(" ", "_")
        heroesName = text.title()
        for r in (("Of", "of"), ("The", "the")):
            heroesName = heroesName.replace(*r)

        contents = requests.get(f'{scathachBase}/herotalent/?tags={heroesName}').json()
        getItem = contents['url']
        gb = f'https://www.dotabuff.com/assets/heroes/{text.replace("_","-").lower()}.jpg'
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag() + decorator.badHero())
            logger.info(decorator.badrequestMsg() + heroesName)
        else:
            await bot.send_message(message.from_user.id, text=getItem, parse_mode= 'Markdown')
            logger.info(decorator.successMsg() + heroesName)

    else:
        await message.answer(decorator.ngaturArgs())


@scathaDP.message_handler(commands=['test'])
async def process_start_command(message: types.Message):
    meme = ''
    await bot.send_message(message.from_user.id, meme) #like this

@scathaDP.message_handler(commands=['changes', 'herochanges'])
async def process_start_command(message: types.Message):
    if len(message.get_args()) != 0:
        text = message.get_args().replace(" ", "_")
        heroesName = text.title()
        for r in (("Of", "of"), ("The", "the")):
            heroesName = heroesName.replace(*r)

        contents = requests.get(f'{scathachBase}/hero/?tags={heroesName}').json()
        getItem = contents['url']
        gb = f'https://www.dotabuff.com/assets/heroes/{text.replace("_","-").lower()}.jpg'
        if not getItem:
            await bot.send_message(message.from_user.id, text=decorator.ErrorFlag() + decorator.badHero())
            logger.info(decorator.badrequestMsg() + heroesName)
        else:
            await bot.send_photo(message.from_user.id, photo=gb, caption=getItem)
            logger.info(decorator.successMsg() + heroesName)

    else:
        await message.answer(decorator.ngaturArgs())


def bacotmemek():
    rand = [decorator.ngaturInvalid(), decorator.ngaturEnggaktau(), decorator.ngaturNglantur(),
            decorator.ngaturNani(), decorator.ngaturSopan(), decorator.ngaturLawak()]
    return random.choice(rand)

@scathaDP.message_handler()
async def echo(message: types.Message):
    await message.answer(bacotmemek()) # message.text is OK too but cringe af


if __name__ == '__main__':
    from Scathachgram.handlers import scathaDP
    executor.start_polling(scathaDP, skip_updates=True)