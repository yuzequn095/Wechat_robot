# encoding: utf-8
#using wxpy from github 'https://github.com/youfou/wxpy'
from wxpy import *

#make a QR code
bot = Bot()

#send msg to self
bot.self.send('Hellp World!')

#locate target friend
my_friend = bot.friends().search(u'已矣')[0]
#send message to my friend
my_friend.send('Hello My Main Account!')


#catch all registered msg
@bot.register()
def print_others(msg):
	print(msg)

# reply my_friend
@bot.register(my_friend)
def reply_my_friend(msg):
	return 'You are my friend'

# reply group in at
@bot.register(Group, TEXT)
def print_group_msg(msg):
	if msg.is_at:
		return 'This is auto-reply test'

# reply self
@bot.register(bot.self, except_self=False)
def reply_self(msg):
	return 'You are myself'

# print all @ msg and auto reply
@bot.register(Group, TEXT)
def print_group_msg(msg):
	if msg.is_at:
		print(msg)
		msg.reply(msg.text)

#keep running
embed()
