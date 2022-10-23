from wxpy import *
bot = Bot()
my_friend=bot.friends().search("平凡")[0]
my_friend.send('Hello, 我是微信机器人!')


# 发送文本
my_friend.send('Hello, WeChat!')