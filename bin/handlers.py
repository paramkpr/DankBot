from telegram.ext.dispatcher import run_async

from .drake import drake
from .fryer import fry_image, fry_gif
from .generator import generate
from .helpers import gif_reply, image_reply, text_reply, vapourize
from .text import commands, cookbook, keys


def fry_handler(bot, update):
	text = update.message.text.lower()
	n = (10 if 'tsar bomba' in text else
	     5 if 'allah hu akbar' in text else
	     3 if 'nuk' in text else
	     1 if 'fry' in text else 0)

	if n:
		args = {key: 1 if key in text else 0 for key in keys}
		if update.message.reply_to_message.document:
			url = bot.get_file(update.message.reply_to_message.document.file_id).file_path
			print(url)
			fry_gif(update, url, n, args)

		elif update.message.reply_to_message.video:
			url = bot.get_file(update.message.reply_to_message.video.file_id).file_path
			fry_gif(update, url, n, args)

		elif update.message.reply_to_message.photo:
			url = bot.get_file(update.message.reply_to_message.photo[::-1][0].file_id).file_path
			fry_image(update, url, n, args)
		return 1
	return 0


def generate_handler(bot, update):
	textn = update.message.text
	text = textn.lower()
	if ('t:' in text or 'ts:' in text) and ('b:' in text or 'bs:' in text):
		t, tc = (text.find('t:'), 1) if 't:' in text else (text.find('ts:'), 0)
		b, bc = (text.find('b:'), 1) if 'b:' in text else (text.find('bs:'), 0)
		url = bot.get_file(update.message.reply_to_message.photo[::-1][0].file_id).file_path

		if b > t:
			generate(
				update, url,
				textn[t + 2:b].upper() if tc else textn[t + 3:b],
				textn[b + 2:].upper() if bc else textn[b + 3:]
			)
		else:
			generate(
				update, url,
				textn[t + 2:].upper() if tc else textn[t + 3:],
				textn[b + 2:t].upper() if bc else textn[b + 3:t]
			)
		return 1
	return 0


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
def reply_handler(bot, update):
	if fry_handler(bot, update):
		return

	elif generate_handler(bot, update):
		return

	main_handler(bot, update)


@run_async
def main_handler(bot, update):
	textn = update.message.text
	text = textn.lower()

	if ', not ' in text:
		drake(update, textn[text.find(', not ') + 6:], textn[:text.find(', not ')])

	elif 'vapourize:' in text:
		vapourize(update, textn[text.find('vapourize:') + 10:])

	elif gif_reply(update, text):
		return

	elif text_reply(update, text):
		return

	elif image_reply(update, text):
		return

	else:
		print(
			'(%s) %s: %s' % (update.message.chat.title, update.message.from_user.first_name, textn)
			if update.message.chat.type == 'group' else
			'%s: %s' % (update.message.from_user.first_name, textn)
		)
