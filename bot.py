"""
      ##### ##                             /            ##### ##
   /#####  /##                           #/          ######  /##
 //    /  / ###                          ##         /#   /  / ##                  #
/     /  /   ###                         ##        /    /  /  ##                 ##
     /  /     ###                        ##            /  /   /                  ##
    ## ##      ##    /###   ###  /###    ##  /##      ## ##  /        /###     ########
    ## ##      ##   / ###  / ###/ #### / ## / ###     ## ## /        / ###  / ########
    ## ##      ##  /   ###/   ##   ###/  ##/   /      ## ##/        /   ###/     ##
    ## ##      ## ##    ##    ##    ##   ##   /       ## ## ###    ##    ##      ##
    ## ##      ## ##    ##    ##    ##   ##  /        ## ##   ###  ##    ##      ##
    #  ##      ## ##    ##    ##    ##   ## ##        #  ##     ## ##    ##      ##
       /       /  ##    ##    ##    ##   ######          /      ## ##    ##      ##
  /###/       /   ##    /#    ##    ##   ##  ###     /##/     ###  ##    ##      ##
 /   ########/     ####/ ##   ###   ###  ##   ### / /  ########     ######       ##
/       ####        ###   ##   ###   ###  ##   ##/ /     ####        ####         ##
#                                                  #
 ##                                                 ##

Copyright (C) 2019  Ishan Manchanda (@Rippr)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from os import environ

from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, RegexHandler, \
	Updater

from bin.handlers import *

if 'TELEGRAM_TOKEN' not in environ:
	load_dotenv()
TOKEN = environ.get('TELEGRAM_TOKEN')

updater = Updater(
	TOKEN,
	workers=32,
	request_kwargs={'read_timeout': 60, 'connect_timeout': 60}
)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('help', help_handler))
dispatcher.add_handler(CommandHandler('changes', changes_handler))
dispatcher.add_handler(CommandHandler('cookbook', cookbook_handler))

dispatcher.add_handler(RegexHandler(r'(?i)(^alt:)', alt_handler))
dispatcher.add_handler(RegexHandler(r'(?i)(^vapourize:)', vapourize_handler))

dispatcher.add_handler(MessageHandler(Filters.reply, reply_handler))
dispatcher.add_handler(MessageHandler(Filters.text, main_handler))
dispatcher.add_handler(MessageHandler(Filters.all, all_handler))

if environ.get('ENVIRONMENT', None) == 'HEROKU':
	print("Starting Webhook")
	updater.start_webhook(
		listen="0.0.0.0",
		port=int(environ.get('PORT')),
		url_path=TOKEN
	)
	updater.bot.setWebhook("https://dankbot-tg.herokuapp.com/" + TOKEN)
	updater.idle()
else:
	print("Starting Polling")
	updater.start_polling()
