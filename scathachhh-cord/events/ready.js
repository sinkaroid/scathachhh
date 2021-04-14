module.exports = async (client) => {
  console.log(`${client.user.username} is live`);
  client.editStatus({
    name: "RTZ",
    type: 1,
    url: "https://www.twitch.tv/arteezy",
  });
};
