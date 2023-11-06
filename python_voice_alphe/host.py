from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Test'
socketio = SocketIO(app)

# Słownik przechowujący listy użytkowników w poszczególnych pokojach
active_rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    if room not in active_rooms:
        active_rooms[room] = []
    active_rooms[room].append(username)
    emit('joined', {'username': username, 'room': room, 'users': active_rooms[room]}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    active_rooms[room].remove(username)
    emit('left', {'username': username, 'room': room, 'users': active_rooms[room]}, room=room)

@socketio.on('message')
def handle_message(data):
    username = data['username']
    room = data['room']
    message = data['message']
    emit('message', {'username': username, 'room': room, 'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
