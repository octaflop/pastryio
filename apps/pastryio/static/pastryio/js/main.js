'use strict';

angular.module("pastryio", ['ngWebSocket'])
  .factory('wsData', function($websocket) {
    // Open a WebSocket connection
    var dataStream = $websocket('wss://127.0.0.1:9000/room-test/');

    var collection = [];

    dataStream.onMessage(function(message) {
      collection.push(JSON.parse(message.data));
    });

    var methods = {
      collection: collection,
      get: function() {
        dataStream.send(JSON.stringify({ action: 'get' }));
      }
    };

    return methods;
  })
  .controller('BlogCtrl', function BlogCtrl(wsData){
    var blog = this;

    blog.wsData = wsData;

    blog.sendClicked = function sendClicked(){
      wsData.send(blog.msg);
    };
  });
