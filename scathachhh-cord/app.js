const ErisClient = require("./structures/Client.js");

const client = new ErisClient(require("./config.js"), {
  maxShards: "auto",
  messageLimit: 0,
  getAllUsers: false,
  disableEveryone: true,
});

client.connect();
process.on("unhandledRejection", (e) => {
  console.log(`unhandledRejection\n${e.stack}`);
});
process.on("uncaughtException", (e) => {
  console.log(`uncaughtException\n${e.stack}`);
});
