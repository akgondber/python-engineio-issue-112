# Subject

Reproduction of [python-engineio issue 112](https://github.com/miguelgrinberg/python-engineio/issues/112).
Server side built with nodejs using [socket.io](https://github.com/socketio/socket.io).

Python dependencies:

$ pipenv graph  

python-socketio==4.0.3
  - python-engineio [required: >=3.2.0, installed: 3.6.0]
    - six [required: >=1.9.0, installed: 1.12.0]
  - six [required: >=1.9.0, installed: 1.12.0]
requests==2.22.0
  - certifi [required: >=2017.4.17, installed: 2019.3.9]
  - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
  - idna [required: >=2.5,<2.9, installed: 2.8]
  - urllib3 [required: >=1.21.1,<1.26,!=1.25.1,!=1.25.0, installed: 1.25.3]
websocket-client==0.56.0
  - six [required: Any, installed: 1.12.0]

# Setup

```bash
$ npm i
$ pipenv install
```

# Usage

Start nodejs app with socket.io server:

```bash
$ npm start
```

Connect to server using python-socketio and try to emit binary data:

```bash
$ pipenv shell
$ python main.py
```

# Output

Sending binary data using client does not work, the client disconnects and then reconnects again. Here is an output with enabled logger:

```
Engine.IO connection established
Emitting event "foo" [/]
Namespace / is connected
I'm connected!
Engine.IO connection dropped
I'm disconnected!
Connection failed, new attempt in 1.11 seconds
Engine.IO connection established
Reconnection successful
Namespace / is connected
I'm connected!
```
