@scathaDP.errors_handler()
async def errors_handler(update, exception):
    if isinstance(exception, CantDemoteChatCreator):
        logging.error(decorator.cantDemote())
        return True

    if isinstance(exception, MessageNotModified):
        logging.error(decorator.notModified())
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.error(decorator.cantDel())
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.error(decorator.deleteNotfound())
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.error(decorator.msgEmpty())
        await update.message.answer(decorator.msgEmpty())
        return True

    if isinstance(exception, Unauthorized):
        logging.info(f'{decorator.unAuth()} {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.error(f'{decorator.invalidQuery()} {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.error(f'{decorator.tgAPIErr()} {exception} \nUpdate: {update}')
        await update.message.answer(decorator.tgAPIErr())
        return True

    if isinstance(exception, RetryAfter):
        logging.error(f'{decorator.retryAfter()} {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, CantParseEntities):
        logging.error(f'{decorator.cantParse()} {exception} \nUpdate: {update}')
        return True

    logging.exception(f'Update: {update} \n{exception}')
    await update.message.answer(decorator.occurred() + '{}'.format(exception))
