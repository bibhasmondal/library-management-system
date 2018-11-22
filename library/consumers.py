# In consumers.py
from channels import Group
from channels.sessions import channel_session
from .libgen import searchbooks as searchebooks

# Connected to websocket.connect


@channel_session
def ws_connect(message):
    message.reply_channel.send({'accept': True})
    # Work out room name from path (ignore slashes)
    #room = message.content['path'].strip("/")
    # Save room in session and add us to the group
    #message.channel_session['room'] = room
    Group("library").add(message.reply_channel)

# Connected to websocket.receive


@channel_session
def ws_message(message):
    searchebooks(message.reply_channel,message.get('text'))
# Connected to websocket.disconnect


@channel_session
def ws_disconnect(message):
    Group("library").discard(message.reply_channel)