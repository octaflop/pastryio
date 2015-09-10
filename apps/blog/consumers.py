from channels import Group
from channels.decorators import channel_session


# Connected to websocket.connect
@channel_session
def ws_connect(message):
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group("chat-{}".format(room)).add(message.reply_channel)


# Connected to websocket.keepalive
@channel_session
def ws_add(message):
    Group("chat-{}".format(message.channel_session['room'])).add(message.reply_channel)


# Connected to websocket.receive
@channel_session
def ws_message(message):
    Group("chat-{}".format(message.channel_session['room'])).send(message.content)


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat-{}".format(message.channel_session['room'])).discard(message.reply_channel)
