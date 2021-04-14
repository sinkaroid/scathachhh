exports.run = function (client, msg, args) {
  if (!args[0])
    return msg.channel.createMessage(
      `cveid pls?, example \`$!cve CVE-2004-1769\``
    );

  (async () => {
    try {
      const fetch = require("node-fetch");
      fetch(`https://cve.circl.lu/api/cve/${args}`)
        .then((res) => Promise.all([res.status, res.json()]))
        .then(([status, jsonData]) => {
          var json = jsonData;
          var a = JSON.parse(JSON.stringify(json));

          msg.channel.createMessage({
            embed: {
              color: client.config.colors.success,
              title: `<:bughunter:585765206769139723> ${a.id}`,
              thumbnail: {
                url: `https://www.jing.fm/clipimg/full/177-1771154_bug-hunter-icon.png`,
              },
              description: `
        [${a.id}](https://cve.circl.lu/cve/${a.id}) | assigner: ${a.assigner} | Published: ${a.Published}

        __**Summary**__
        ${a.summary}
        
        __**CVSS Score**__
        ${a.cvss}
        
        __**CWE**__
        ${a.cwe}`,
            },
          });
        });
    } catch (error) {
      console.log(error);
      console.log("anjing");
    }
  })();
};

exports.aliases = ["cve"];
