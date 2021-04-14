exports.run = function (client, msg, args) {
  const expression = require("chaldea");
  const char = new expression.Client();

  let user = msg.mentions[0] || client.users.get(args[0]);
  if (!user) user = msg.author;

  char.smug().then((data) => {
    msg.channel.createMessage({
      embed: {
        color: client.config.colors.success,
        image: {
          url: data,
        },
        author: {
          name: client.username,
        },
        description: `
          ${user.username} ( •̀ ω •́ )y`,
      },
    });
  });
};

exports.aliases = ["smug"];
