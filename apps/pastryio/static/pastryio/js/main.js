'use strict';

angular.module("pastryio", ['ngWebSocket'])
  .factory('wsData', function($websocket) {
    // Open a WebSocket connection
  var ws = $websocket('ws://127.0.0.1:9000/room_test/');
  // var ws = $websocket('ws://echo.websocket.org/');
  var collection = [];

  ws.onMessage(function(event) {
    console.log('message: ', event);
    var res;
    try {
      res = JSON.parse(event.data);
    } catch(e) {
      res = {
        'username': 'anonymous',
        'message': event.data
      };
    }

    collection.push({
      username: res.username,
      content: res.message,
      timeStamp: event.timeStamp
    });
  });

  ws.onError(function(event) {
    console.log('connection Error', event);
  });

  ws.onClose(function(event) {
    console.log('connection closed', event);
  });

  ws.onOpen(function() {
    console.log('connection open');
    ws.send('Hello World');
    ws.send('again');
    ws.send('and again');
  });
  // setTimeout(function() {
  //   ws.close();
  // }, 500)

  return {
    collection: collection,
    status: function() {
      return ws.readyState;
    },
    send: function(message) {
      if (angular.isString(message)) {
        ws.send(message);
      }
      else if (angular.isObject(message)) {
        ws.send(JSON.stringify(message));
      }
    }
  };
  })
  .controller('BlogCtrl', function BlogCtrl(wsData){
    var blog = this;
    blog.logs = wsData.collection;

    blog.sendClicked = function sendClicked(){
      wsData.send({msg: blog.msg});
      console.debug(wsData);
    };

  });
