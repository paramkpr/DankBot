from telegram.ext.dispatcher import run_async

from .drake import drake
from .helpers import helper_b, helper_gif, helper_image, helper_text, helper_fry, helper_generate
from .utils.text import commands, cookbook, chars, vapourtext


@run_async
def start_handler(bot, update):
	update.message.reply_markdown(text='*This is DankBot!*\n' + commands)


@run_async
def help_handler(bot, update):
	update.message.reply_markdown(text=commands)


@run_async
def cookbook_handler(bot, update):
	update.message.reply_markdown(text=cookbook)


@run_async
def alt_handler(bot, update):
	text = update.message.text[4:].lower()
	r, u = [], False
	for i in text:
		if i.lower() in chars:
			r.append(i.upper() if u else i.lower())
			u = not u
		else:
			r.append(i)
	update.message.reply_text("".join(r))


@run_async
def vapourize_handler(bot, update):
	text = update.message.text[10:]
	r = []
	for i in text:
		if i in vapourtext:
			r.append(vapourtext[i])
		else:
			r.append(i)
	update.message.reply_text("".join(r))


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
		drake(update, textn[text.find(', not ') + 6:], textn[:text.find(', not ')])

	elif '🅱️' in text:
		helper_b(update, text)

	elif helper_gif(update, text, words):
		return

	elif helper_image(update, text, words):
		return

	elif helper_text(update, text, words):
		return

	else:
		print(
			'(%s) %s: %s' % (update.message.chat.title, update.message.from_user.first_name, textn)
			if update.message.chat.type == 'group' else
			'%s: %s' % (update.message.from_user.first_name, textn)
		)
