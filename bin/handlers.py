from telegram.ext.dispatcher import run_async

from .drake import drake
from .helpers import \
	helper_b, helper_gif, helper_image, \
	helper_text, helper_fry, helper_generate, helper_despacito
from .utils.text import commands, cookbook, chars, vapourtext


@run_async
def start_handler(bot, update):
	update.message.reply_markdown('*This is DankBot!*\n' + commands, quote=True)


@run_async
def help_handler(bot, update):
	update.message.reply_markdown(commands, quote=True)


@run_async
def cookbook_handler(bot, update):
	update.message.reply_markdown(cookbook, quote=True)


@run_async
def alt_handler(bot, update):
	text = update.message.text[4:].lower()
	result, upper = [], False
	for i in text:
		if i.lower() in chars:
			result.append(i.upper() if upper else i.lower())
			upper = not upper
		else:
			result.append(i)
	update.message.reply_text("".join(result), quote=True)


@run_async
def vapourize_handler(bot, update):
	text = update.message.text[10:]
	result = []
	for i in text:
		if i in vapourtext:
			result.append(vapourtext[i])
		else:
			result.append(i)
	update.message.reply_text("".join(result), quote=True)


@run_async
def reply_handler(bot, update):
	if helper_fry(bot, update):
		return

	if helper_generate(bot, update):
		return

	main_handler(bot, update)


@run_async
def main_handler(bot, update):
	textn = update.message.text
	text = textn.lower()
	words = text.split()

	if ', not ' in text:
		drake(
			update,
			textn[text.find(', not ') + 6:],
			textn[:text.find(', not ')]
		)

	elif '🅱️' in text:
		helper_b(update, text)

	elif 'dankbot play despacito' in text or 'alexa play despacito' in text:
		helper_despacito(update, text)

	elif helper_gif(update, text, words):
		return

	elif helper_image(update, text, words):
		return

	elif helper_text(update, text, words):
		return

	else:
		print(
			'(%s) %s: %s' % (
				update.message.chat.title,
				update.message.from_user.first_name,
				textn
			)
			if update.message.chat.type == 'group' else
			'%s: %s' % (update.message.from_user.first_name, textn)
		)
