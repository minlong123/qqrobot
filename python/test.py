from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.message.elements.internal import Plain, Image, At
from graia.application.friend import Friend
from graia.application.group import Group,Member
from graia.application.event.mirai import FriendRecallEvent, GroupRecallEvent

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8080", # 填入 httpapi 服务运行的地址
        authKey="INITKEYH6k4AEay", # 填入 authKey
        account=1249430088, # 你的机器人的 qq 号
        websocket=True # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)

# 回复好友消息
@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend):
    # print(friend) id=1249430088 nickname='肖' remark='客服001'
    await app.sendFriendMessage(friend, MessageChain.create([
        Plain("Hello, World!")
    ]))


@bcc.receiver("GroupMessage")
async def group_message_listener(app: GraiaMiraiApplication,
                                group: Group,
                                member: Member,
                                message: MessageChain):
    allkey={"接单","来一个","有人接吗","有偿","来一个","有没有懂得","有人做吗"}
    for key in allkey:
        if message.hasText(key):
            ttt=str(member.id)+"在群"+str(member.group.id)+"里发了一条疑似接单信息："+str(message.get(Plain))

            await app.sendGroupMessage(426867207, message.create([Plain(ttt)]))


app.launch_blocking()