exports.run = function (client, msg, args) {
  let guild = msg.channel.guild;
  let botCount = guild.members.filter((member) => member.user.bot).length;
  let owner = guild.members.get(guild.ownerID).user;

  const dateObject = new Date(guild.createdAt);
  const humanDateFormat = dateObject.toString();
  console.log(humanDateFormat);

  msg.channel.createMessage({
    embed: {
      color: client.config.colors.success,
      description: `
Name: __**${guild.name}**__ (${guild.id})
Owner: **${owner.username}#${owner.discriminator}** (${owner.id})

Channels: \`${guild.channels.size}\`
Members: \`${guild.memberCount}\`
Users: \`${guild.memberCount - botCount}\`
Bots: \`${botCount}\`
Created: \`${humanDateFormat}\`
`,
    },
  });
};

exports.aliases = ["si"];
