# screen.py
## Description
A light-weight library for easy interaction between Python and GNU screen.

This library allows you create, find and kill screen sessions programmatically from Python, as well as send (string) commands to these sessions. You can use this to start other software inside a screen session from a Python script, like this:
```python
import screens

# Start a new session and give it something to do    
session = screens.Session('myName')
session.send_command('echo hello')

# Kill a screen session with a particular name
session = screens.get_session_by_name('myName')
session.kill()

# Print all the id of all sessions
for session in screens.get_sessions():
    print(session.id)
```
## Installation
```
pip install --upgrade screens.py
```
