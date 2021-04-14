exports.run = function (client, msg, args) {
  const dog = require("scathach-api");
  const scathach = new dog();

  let commands = Array.from(client.commands.keys()).sort().join(", ");
  console.log(commands);

  scathach.nsfw.gif().then((scathach) => {
    msg.channel.createMessage({
      embed: {
        color: client.config.colors.success,
        image: {
          url: scathach.url,
        },
        description: `
        CROT GIF`,
      },
    });
  });
};

exports.aliases = ["gif"];
