from random import randint

from telegram.ext import run_async

from .files import *
from .fryer import fry_gif, fry_image
from .generator import generate
from .text import exbuded, bs, keys
from .text import ironic


def get_random(var):
	return var[randint(0, len(var) - 1)]


@run_async
def helper_b(update, text):
	a = []
	for x in text.split(' '):
		if x == 'nigga':
			a.append('ni🅱️🅱️a')
			continue
		if x in exbuded:
			a.append(x)
			continue
		i = 0
		try:
			while x[i] not in bs:
				i += 1
			s, i = i, i + 1
			while x[i] in bs:
				i += 1
			end = i
			a.append(x[:s] + '🅱️' + x[end:])
		except IndexError:
			a.append(x)
	update.message.reply_text(' '.join(a))


def helper_fry(bot, update):
	text = update.message.text.lower()
	n = (10 if 'tsar bomba' in text else
	     5 if 'allah hu akbar' in text else
	     3 if 'nuk' in text else
	     1 if 'fry' in text else 0)

	if n:
		args = {key: 1 if key in text else 0 for key in keys}
		if update.message.reply_to_message.document:
			url = bot.get_file(update.message.reply_to_message.document.file_id).file_path
			fry_gif(update, url, n, args)

		elif update.message.reply_to_message.video:
			url = bot.get_file(update.message.reply_to_message.video.file_id).file_path
			fry_gif(update, url, n, args)

		elif update.message.reply_to_message.photo:
			url = bot.get_file(update.message.reply_to_message.photo[::-1][0].file_id).file_path
			fry_image(update, url, n, args)
		return 1
	return 0


def helper_generate(bot, update):
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


def helper_gif(update, text):
	if 'alexa play despacito' in text or 'dankbot play despacito' in text:
		update.message.reply_animation(animation=despacito[0])
		update.message.reply_audio(audio=dedpacito['normal' if randint(0, 9) else 'ded'])

	elif 'hmmm' in text:
		update.message.reply_animation(animation=get_random(hmmm))

	elif 'allah hu akbar' in text:
		update.message.reply_animation(animation=get_random(allah_hu_akbar))

	elif 'do it' in text:
		update.message.reply_animation(animation=get_random(do_it))

	elif 'nein' in text:
		update.message.reply_animation(animation=get_random(nein))

	elif 'damnnn' in text:
		update.message.reply_animation(animation=get_random(damnnn))

	else:
		return 0
	return 1


def helper_image(update, text):
	if text == 'e':
		update.message.reply_photo(photo=get_random(e))

	elif 'hello there' in text:
		update.message.reply_photo(photo=get_random(hello_there))

	elif 'i don\'t think so' in text or 'i dont think so' in text:
		update.message.reply_photo(photo=get_random(dont_think_so))

	elif 'wat' in text:
		update.message.reply_photo(photo=get_random(wat))

	elif 'dude what' in text:
		update.message.reply_photo(photo=get_random(dude_what))

	elif 'wut' in text or 'what even' in text:
		update.message.reply_photo(photo=get_random(wut))

	elif 'what the' in text:
		update.message.reply_photo(photo=get_random(what_the))

	elif 'miss me with that gay shit' in text or 'thats gay' in text or 'that\'s gay' in text:
		update.message.reply_photo(photo=get_random(miss_me))

	else:
		return 0
	return 1


def helper_text(update, text):
	if 'ironic' in text or 'darth plagueis' in text:
		update.message.reply_text(ironic)

	elif text.startswith('f ') or text.startswith('rip ') or text == 'f' or text == 'rip':
		update.message.reply_text('F')

	elif text == '???':
		update.message.reply_text('Profit')

	elif 'thought' in text and 'process' in text:
		update.message.reply_text('thoughtprocessors.herokuapp.com')

	elif 'tp' in text:
		update.message.reply_text(text.replace('tp', '✝️🅿️'))

	elif 'jainil' in text:
		update.message.reply_text('ヽ(◉◡◔)ﾉ  i\'M jAiNiL aNd I iS aUtIsTiC. ヽ(◉◡◔)ﾉ')

	else:
		return 0
	return 1
