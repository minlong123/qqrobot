from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.message.elements.internal import Plain, Image, At
from graia.application.friend import Friend
from graia.application.group import Group,Member
from graia.application.event.mirai import FriendRecallEvent, GroupRecallEvent
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.163.com'



# 发邮件的邮箱，下面两个参数都一致
user='13545774974@163.com'
sender='13545774974@163.com'

# pop3授权码
password='itbull2017'

# 接收邮件的邮箱
receive='minlongdemeng@163.com'

# 邮件标题
subject='消息监听'

robotqq=1249430088






def sendEmail(val):

    # 邮件内容
    content="<html>"+val+"</html>"

    msg=MIMEText(content,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=sender
    msg['To']=receive

    # ssl协议端口号要使用465
    smtp=smtplib.SMTP_SSL(smtpserver,465)

    # 向服务器标识用户身份
    smtp.helo(smtpserver)

    # 服务器返回结果确认
    smtp.ehlo(smtpserver)

    # 登陆邮箱服务器用户名和密码
    smtp.login(user,password)

    smtp.sendmail(sender,receive,msg.as_string())
    # 装载准备发送
    # print("Start send Email……")
    smtp.quit()
    # print("Send Email end!")






loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8080", # 填入 httpapi 服务运行的地址
        authKey="INITKEYH6k4AEay", # 填入 authKey
        account=robotqq, # 你的机器人的 qq 号
        websocket=True # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)


# 8,718][ERROR]: received a unknown event: FriendAddEvent{'type': 'FriendAddEvent', 'friend': {'id': 872161729, 'nickname': 'Y&Q@', 'remark': ''}}

# 回复好友消息
@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend,message: MessageChain):
    # print(friend) id=1249430088 nickname='肖' remark='客服001'

    sendEmail("收到好友("+str(friend.nickname)+")："+str(friend.id)+"的一条信息："+str(message.get(Plain)[0].text))
    # await app.sendFriendMessage(friend, MessageChain.create([
    #     Plain("QQ不方便，无法回复，请加我微信：pingfandeminlong 咨询")
    # ]))




@bcc.receiver("GroupMessage")
async def group_message_listener(app: GraiaMiraiApplication,
                                group: Group,
                                member: Member,
                                message: MessageChain):
    allkey={"找个会","有接","你熟悉","有代做的","有没有能","的私聊","来个靠谱点","接单的有吗","来一个","有大佬帮忙",
    "有人接吗","有偿","来一个","有没有懂得","有人做吗","私我一下","帮解决","有会的吗","群里有",
    "可以开发吗","我想","能做不","有会玩","有没有","有兼职","能做的私","帮我","谁会搞","有人会吗","能做吗"
    }
    for key in allkey:
        if message.hasText(key):

            ttt=str(member.name)+" QQ:"+str(member.id)+"在群:"+str(member.group.id)+"("+str(group.name)+")""里发了一条疑似接单信息："+str(message.get(Plain)[0].text)

            # 发QQ群
            # await app.sendGroupMessage(426867207, message.create([Plain(ttt)]))
            
            # 发好友
            await app.sendFriendMessage(3378109058, MessageChain.create([
                Plain(ttt)
            ]))

            # 发送邮件
            sendEmail(ttt)
            
app.launch_blocking()