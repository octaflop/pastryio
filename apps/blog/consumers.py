from channels import Group


def ws_add(message):
    Group("chat").add(message.reply_channel)


# Connected to websocket.keepalive
def ws_keepalive(message):
    Group("chat").add(message.reply_channel)


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)