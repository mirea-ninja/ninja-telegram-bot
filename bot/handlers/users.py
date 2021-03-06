import datetime

from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler

from bot import dispatcher
from bot.models.messages_history import MessagesHistory
from bot.models.user import User


def users_updater(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message

    # increasing the number of messages
    MessagesHistory.add_message(
        msg.from_user.id,
        datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).date(),
    )

    User.update(
        msg.from_user.id,
        msg.from_user.username,
        msg.from_user.first_name,
        msg.from_user.last_name,
    )

    if msg.reply_to_message:
        User.update(
            msg.reply_to_message.from_user.id,
            msg.reply_to_message.from_user.username,
            msg.reply_to_message.from_user.first_name,
            msg.reply_to_message.from_user.last_name,
        )

    if msg.forward_from:
        User.update(
            msg.forward_from.id,
            msg.forward_from.username,
            msg.forward_from.first_name,
            msg.forward_from.last_name,
        )


dispatcher.add_handler(
    MessageHandler(
        Filters.all & Filters.chat_type.groups, users_updater, run_async=True
    )
)
