const axios = require("axios");

/**
 * Utilities module
 */
module.exports = class Util {
  /**
   * Do a random number between min and max
   *
   * @param {Number} min  the minimum number
   * @param {Number} max  the maximum number
   * @returns {Number}    the random number between the min and max number
   */
  static randomNumber(min, max) {
    if (!(max instanceof Number) || !(min instanceof Number)) {
      return null;
    }

    let random = Math.floor(Math.random() * (max - min + 1) + min);
    if (random === max) {
      random--;
    }

    return random;
  }

  /**
   * Creates a random string
   *
   * @param {Number} length       the string length
   * @param {Boolean} useCapital  true if you want to use capital
   * @param {Boolean} useNumber   true if you want to use number
   */
  static randomString(length, useCapital, useNumber) {
    if (
      !(length instanceof Number) ||
      !(useCapital instanceof Boolean) ||
      !(useNumber instanceof Boolean)
    ) {
      return null;
    }

    const normalChars = "abcdefghijklmnopqrstuvwxyz".split("");
    const capsChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
    let strings = "";
    while (strings.length < length) {
      const random = this.randomNumber(26, 0);

      if (useCapital && this.randomBoolean()) {
        strings += capsChars[random];
        continue;
      }
      if (useNumber && this.randomBoolean()) {
        strings += this.randomNumber(10, 0);
        continue;
      }

      strings += normalChars[random];
    }

    return strings;
  }

  /**
   * Creates a UUID
   *
   * @returns {String} the uuid
   */

  static timeParser(ms) {
    let seconds = ms / 1000;
    let days = parseInt(seconds / 86400);
    seconds = seconds % 86400;
    let hours = parseInt(seconds / 3600);
    seconds = seconds % 3600;
    let minutes = parseInt(seconds / 60);
    seconds = parseInt(seconds % 60);

    if (days) {
      return `${days}d ${hours}h ${minutes}m ${seconds}s`;
    } else if (hours) {
      return `${hours}h ${minutes}m ${seconds}s`;
    } else if (minutes) {
      return `${minutes}m ${seconds}s`;
    }
    return `${seconds}s`;
  }

  static codeBlock(string, code) {
    if (code) return `\`\`\`${code}\n${string}\`\`\``;
    return `\`\`\`${string}\`\`\``;
  }

  static clean(text) {
    if (typeof text === "string")
      return text
        .replace(/`/g, "`" + String.fromCharCode(8203))
        .replace(/@/g, "@" + String.fromCharCode(8203));
    else return text;
  }
};
