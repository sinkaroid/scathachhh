exports.run = function (client, msg, args) {
  (async () => {
    try {
      const fetch = require("node-fetch");
      let i = args;
      if (!i[0])
        return msg.channel.createMessage("country pls? ie: `$s nat fr`");

      fetch(`https://restcountries.eu/rest/v2/name/${i}?fullText=true`)
        .then((res) => Promise.all([res.status, res.json()]))
        .then(([status, jsonData]) => {
          var json = jsonData;
          var item = json.find((object) => object.name);

          let gen = `https://www.countryflags.io/${i}/flat/64.png`;
          const rog = item.capital.replace(/ /g, "+");
          let loc = `https://open.mapquestapi.com/staticmap/v5/map?key=gNeMFtoZo786sY3ICVMyKGXAv17zJ5wd&center=${rog}&size=800,400`;
          console.log(msg.content.replace("$s nat", ""));
          console.log(rog);
          if (!json[0])
            return msg.channel.createMessage("Your query returned no results");
          msg.channel.createMessage({
            embed: {
              color: Math.floor(Math.random() * 16777214) + 1,
              author: {
                name: `${item.name}`,
              },
              footer: {
                // Footer text
                icon_url: client.user.avatarURL,
                text: "Semiramis, invoked by " + msg.author.username,
              },
              thumbnail: {
                url: `${gen}`,
              },
              image: {
                url: `${loc}`,
              },
              fields: [
                {
                  name: "Wikipedia",
                  value: `🔗 [#${item.demonym}](https://en.wikipedia.org/wiki/${item.demonym})`,
                },
                {
                  name: "🌎Region",
                  value: `${item.subregion}`,
                },
                {
                  name: "🏢Capital",
                  value: `${item.capital}`,
                  inline: true,
                },
                {
                  name: "📊Population",
                  value: `${item.population.toLocaleString()}`,
                  inline: true,
                },
                {
                  name: "📈LatLng",
                  value: `${item.latlng}`,
                  inline: true,
                },
                {
                  name: "📋Alternative",
                  value: `${item.altSpellings}`,
                },
                {
                  name: "🕗Timezones",
                  value: `${item.timezones}`,
                },
                {
                  name: "🌐Demonym",
                  value: `${item.demonym}`,
                  inline: true,
                },
                {
                  name: "📞CallingCode",
                  value: `${item.callingCodes}`,
                  inline: true,
                },
                {
                  name: "Cioc",
                  value: `${item.cioc}`,
                  inline: true,
                },
                {
                  name: "Additional",
                  value: `restObject [#${item.name}](https://restcountries.eu/rest/v2/name/${item.alpha2Code}?fullText=true)`,
                },
                {
                  name: "OpenstreetMap",
                  value: `stateObject [OpenStreetMap/${item.alpha3Code}](http://countries.petethompson.net/#/country/${item.alpha3Code})`,
                },
              ],
            },
          });
        });
    } catch (error) {
      console.log(error);
    }
  })();
};

exports.aliases = ["rest"];
