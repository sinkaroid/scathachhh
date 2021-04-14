exports.run = function (client, msg, args) {
  const lewd = require("ereshkigal");
  const ere = new lewd.Client();

  ere.dota().then((url) => {
    msg.channel.createMessage(url);
  });
};

exports.aliases = ["dota"];
