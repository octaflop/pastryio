socket = new WebSocket("ws://127.0.0.1:9000/room_test/");
socket.onmessage = function(e) {
    alert(e.data);
}
socket.onopen = function() {
    socket.send("chat-hello world");
}