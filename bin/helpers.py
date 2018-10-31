from random import randint

from telegram.ext.dispatcher import run_async

from .files import *
from .text import cons, exbuded, ironic, vapourtext


@run_async
def vapourize(update, text):
	r = []
	for i in text:
		if i in vapourtext:
			r.append(vapourtext[i])
		else:
			r.append(i)
	update.message.reply_text("".join(r))


def get_random(var):
	return var[randint(0, len(var) - 1)]


def b_ify(text):
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
			while x[i] not in cons:
				i += 1
			s, i = i, i + 1
			while x[i] in cons:
				i += 1
			end = i
			a.append(x[:s] + '🅱️' + x[end:])
		except IndexError:
			a.append(x)
	return ' '.join(a)


def gif_reply(update, text):
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


def text_reply(update, text):
	if 'ironic' in text or 'darth plagueis' in text:
		update.message.reply_text(ironic)

	elif text.startswith('f ') or text.startswith('rip ') or text == 'f' or text == 'rip':
		update.message.reply_text('F')

	elif text == '???':
		update.message.reply_text('Profit')

	elif '🅱️' in text:
		update.message.reply_text(b_ify(text))

	else:
		return 0
	return 1


def image_reply(update, text):
	if text == 'e':
		update.message.reply_photo(photo=get_random(e))

	elif 'hello there' in text:
		update.message.reply_photo(photo=get_random(hello_there))

	elif 'i don\'t think so' in text or 'i dont think so' in text:
		update.message.reply_photo(photo=get_random(dont_think_so))

	elif 'wut' in text or 'dude what' in text or 'what even' in text:
		update.message.reply_photo(photo=get_random(wut))

	elif 'what the' in text:
		update.message.reply_photo(photo=get_random(what_the))

	elif 'miss me with that gay shit' in text or 'thats gay' in text or 'that\'s gay' in text:
		update.message.reply_photo(photo=get_random(miss_me))

	elif 'thought' in text and 'process' in text:
		update.message.reply_text('thoughtprocessors.herokuapp.com')

	elif 'tp' in text:
		update.message.reply_text(text.replace('tp', '✝️🅿️'))

	elif 'jainil' in text:
		update.message.reply_text('ヽ(◉◡◔)ﾉ  i\'M jAiNiL aNd I iS aUtIsTiC. ヽ(◉◡◔)ﾉ')

	else:
		return 0
	return 1
