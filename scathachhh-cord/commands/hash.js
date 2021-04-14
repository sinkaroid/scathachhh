exports.run = function (client, msg, args) {
  if (!args[1])
    return msg.channel.createMessage(`<string> <type>
    example: \`$!hash password --md5\`
__**hashType**__
\`md2\` \`md4\` \`md5\` \`sha1\` \`sha224\` \`sha256\` 
\`sha384\` \`sha512/224\` \`sha512/256\` \`sha512\` 
\`sha3-224\` \`sha3-256\` \`sha3-384\` \`sha3-512\` 
\`ripemd128\` \`ripemd160\` \`ripemd256\` \`ripemd320\` 
\`whirlpool\` \`tiger128,3\` \`tiger160,3\` \`tiger192,3\` 
\`tiger128,4\` \`tiger160,4\` \`tiger192,4\` \`snefru\` 
\`snefru256\` \`gost\` \`gost-crypto\` \`adler32\` \`crc32\` 
\`crc32b\` \`fnv132\` \`fnv1a32\` \`fnv164\` \`fnv1a64\` \`joaat\` 
\`haval128,3\` \`haval160,3\` \`haval192,3\` \`haval224,3\` 
\`haval256,3\` \`haval128,4\` \`haval160,4\` \`haval192,4\` 
\`haval224,4\` \`haval256,4\` \`haval128,5\` \`haval160,5\` 
\`haval192,5\` \`haval224,5\` \`haval256,5\``);

  (async () => {
    try {
      const fetch = require("node-fetch");
      let param = args.toString().replace("--", "&hash=");
      console.log(param);

      let dataH = param.replace(/^(.*?)=/g, "");
      console.log(dataH); //md5

      let dataK = param.replace(/&(.*?)$/g, "").replace(/,/g, "");
      console.log(dataK); //str

      const { pwd } = await fetch(
        `http://argonaut.test/asu.php?kata=${dataK}&hash=${dataH}`
      ).then((response) => response.json());
      if (!pwd[1])
        return msg.channel.createMessage("Unreachable / invalid flags");
      console.log(pwd);

      msg.channel.createMessage({
        embed: {
          color: client.config.colors.success,
          description: `\`${pwd}\``,
        },
      });
    } catch (error) {
      console.log(error);
    }
  })();
};

exports.aliases = ["hash"];
