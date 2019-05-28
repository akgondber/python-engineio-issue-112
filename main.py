import socketio

sio = socketio.Client(logger=True, binary=True)

@sio.on('connect')
def on_connect():
    print('I\'m connected!')

@sio.on('message')
def on_message(data):
    print('I received a message!')

@sio.on('disconnect')
def on_disconnect():
    print('I\'m disconnected!')

sio.connect('http://localhost:4001', socketio_path='/ws/socket.io', transports=['websocket'])
sio.emit('foo', b'\x00\x00\x00\x13')
