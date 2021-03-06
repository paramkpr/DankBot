from datetime import datetime
from inspect import currentframe, getframeinfo
from pytz import timezone
from sys import stdout


def log_debug(message):
	cf = currentframe()
	file = getframeinfo(cf).filename
	line = cf.f_back.f_lineno
	timestamp = datetime.now(tz=timezone('Asia/Kolkata'))

	stdout.write('DEBUG %s <line %s, %s>: %s\n' % (
		timestamp, line, file, message
	))


def log_info(message):
	timestamp = datetime.now(tz=timezone('Asia/Kolkata'))
	stdout.write('INFO %s: %s\n' % (timestamp, message))


def log_warn(message):
	cf = currentframe()
	file = getframeinfo(cf).filename
	line = cf.f_back.f_lineno
	timestamp = datetime.now(tz=timezone('Asia/Kolkata'))

	stdout.write('WARN %s <line %s, %s>: %s\n' % (
		timestamp, line, file, message
	))


def log_command(update, command):
	log_info('{%s} %s' % (command, generate_log_message(update)))


def log_message(update):
	log_info(generate_log_message(update))


def generate_log_message(update):
	return (
		'(%s[%s]) %s[%s]: %s' % (
			update.message.chat.title,
			update.message.chat.id,
			update.message.from_user.first_name,
			update.message.from_user.id,
			update.message.text if update.message.text else '<media file>'
		)
		if update.message.chat.type != 'private' else
		'%s[%s]: %s' % (
			update.message.from_user.first_name,
			update.message.from_user.id,
			update.message.text
		)
	)

# REVIEW: Consider adding actions "DankBot is typing" for long actions
#  such as frying, meme generation, etc.
# from functools import wraps
#
#
# def send_action(action):
# 	"""Sends `action` while processing func command."""
#
# 	def decorator(func):
# 		@wraps(func)
# 		def command_func(update, context, *args, **kwargs):
# 			context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
# 			return func(update, context, *args, **kwargs)
#
# 		return command_func
#
# 	return decorator
