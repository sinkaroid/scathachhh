exports.run = function (client, msg) {
    const cosp = require("sessyoin");
    const sessyoin = new cosp.Client();
  
    sessyoin.ass().then((sessyoin) => {
      msg.channel.createMessage({
        embed: {
          color: client.config.colors.success,
          image: {
            url: sessyoin,
          },
          description: `
          asssss crotTTTTT`,
        },
      });
    });
  };
  
  exports.aliases = ["cosp"];
  