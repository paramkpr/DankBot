from random import randint

from telegram.ext import run_async

from .fryer import fry_gif, fry_image
from .generator_classic import generate
from .utils.files import *
from .utils.logs import log_command
from .utils.text import bs, exbuded, ironic, keys


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

	out = ' '.join(a)
	if out == text:
		return
	update.message.reply_text(out, quote=True)
	log_command(update, 'B')


def helper_fry(bot, update):
	text = update.message.text.lower()
	n = (
		10 if 'tsar bomba' in text else
		5 if 'allah hu akbar' in text else
		3 if 'nuk' in text else
		1 if 'fry' in text else 0
	)

	if n:
		args = {key: 1 if key in text else 0 for key in keys}
		if update.message.reply_to_message.document:
			url = bot.get_file(
				update.message.reply_to_message.document.file_id
			).file_path
			fry_gif(update, url, n, args)

		elif update.message.reply_to_message.video:
			url = bot.get_file(
				update.message.reply_to_message.video.file_id
			).file_path
			fry_gif(update, url, n, args)

		elif update.message.reply_to_message.photo:
			url = bot.get_file(
				update.message.reply_to_message.photo[::-1][0].file_id
			).file_path
			fry_image(update, url, n, args)
		log_command(update, 'FRY')
		return 1
	return 0


def helper_generate(bot, update):
	textn = update.message.text
	text = textn.lower()
	if ('t:' in text or 'ts:' in text) and ('b:' in text or 'bs:' in text):
		t, tc = (text.find('t:'), 1) if 't:' in text else (text.find('ts:'), 0)
		b, bc = (text.find('b:'), 1) if 'b:' in text else (text.find('bs:'), 0)
		url = bot.get_file(
			update.message.reply_to_message.photo[::-1][0].file_id
		).file_path

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
		log_command(update, 'GEN')
		return 1
	return 0


def helper_despacito(update, text):
	update.message.reply_animation(despacito[0], quote=True)
	try:
		word = text[text.find('play despacito') + 15:].partition(' ')[0]
		n = int(word)
		update.message.reply_audio(
			dedpacito[min(max(1, n), 11)],
			quote=True
		)
	except (IndexError, ValueError):
		update.message.reply_audio(
			dedpacito['normal' if randint(0, 9) else 'ded'],
			quote=True
		)
	log_command(update, 'DESPACITO')


def helper_gif(update, text, words):
	if 'hmmm' in text:
		update.message.reply_animation(get_random(hmmm), quote=True)
		log_command(update, 'HMMM')

	elif 'boom son' in text:
		update.message.reply_animation(get_random(allah_hu_akbar), quote=True)
		log_command(update, 'BOOMSON')

	elif 'just do it' in text:
		update.message.reply_animation(get_random(just_do_it), quote=True)
		log_command(update, 'JUSTDOIT')

	elif 'nein' in words:
		update.message.reply_animation(get_random(nein), quote=True)
		log_command(update, 'NEIN')

	else:
		return 0
	return 1


def helper_image(update, text, words):
	if text == 'e':
		update.message.reply_photo(get_random(e), quote=True)
		log_command(update, 'E')

	elif 'hello there' in text:
		update.message.reply_photo(get_random(hello_there), quote=True)
		log_command(update, 'HELLOTHERE')

	elif 'i don\'t think so' in text or 'i dont think so' in text:
		update.message.reply_photo(get_random(dont_think_so), quote=True)
		log_command(update, 'IDONTTHINKSO')

	elif 'wat' in words:
		update.message.reply_photo(get_random(wat), quote=True)
		log_command(update, 'WAT')

	elif 'dude what' in text:
		update.message.reply_photo(get_random(dude_what), quote=True)
		log_command(update, 'DUDEWHAT')

	elif 'wut' in words or 'what even' in text:
		update.message.reply_photo(get_random(wut), quote=True)
		log_command(update, 'WUT')

	elif 'what the' in text:
		update.message.reply_photo(get_random(what_the), quote=True)
		log_command(update, 'WHATTHE')

	elif (
		'miss me with that gay shit' in text
		or 'thats gay' in text
		or 'that\'s gay' in text
	):
		update.message.reply_photo(get_random(miss_me), quote=True)
		log_command(update, 'MMWTGS')

	else:
		return 0
	return 1


def helper_text(update, text, words):
	if 'ironic' in text or 'darth plagueis' in text:
		update.message.reply_text(ironic, quote=True)
		log_command(update, 'IRONIC')

	elif (
		text.startswith('f ')
		or text.startswith('rip ')
		or text == 'f'
		or text == 'rip'
	):
		update.message.reply_text('F', quote=True)
		log_command(update, 'F')

	elif 'oof' in words:
		update.message.reply_text('oof indeed.', quote=True)
		log_command(update, 'OOF')

	elif text == '???':
		update.message.reply_text('Profit', quote=True)
		log_command(update, 'PROFIT')

	elif 'thought' in text and 'process' in text:
		update.message.reply_text('thoughtprocessors.herokuapp.com', quote=True)
		log_command(update, 'THOUGHTPROCESSORS')

	elif 'tp' in text and 'http' not in text:
		update.message.reply_text(text.replace('tp', '✝️🅿️'), quote=True)
		log_command(update, 'TP')

	else:
		return 0
	return 1
