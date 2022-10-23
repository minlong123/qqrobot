from plyer import notification

class notif:

    def sendDes(mes):
        notification.notify(
            title = '群消息监听',
            message = mes,
            app_icon = None,
            timeout = 10000,
        )

    def sendfriDes(mes):
        notification.notify(
            title = '好友消息监听',
            message = mes,
            app_icon = None,
            timeout = 10000,
        )