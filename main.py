from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow cross-origin connections

@app.route('/')
def index():
    return render_template('index.html')  # Render the frontend page

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('user_join')
def handle_user_join(data):
    username = data.get("username", "Guest")
    print(f'User {username} joined')

@socketio.on('new_message')
def handle_new_message(data):
    username = data.get("username", "Anonymous")
    message_text = data.get("text", "")

    print(f'New message from {username}: {message_text}')
    
    # Send back correct data structure
    emit('chat', {'username': username, 'message': message_text}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)  # Use `socketio.run()` instead of `app.run()`
