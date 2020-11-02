const Discord = require('discord.js');
const client = new Discord.Client();
const Guild = new Discord.Guild(client, data);
const prefix = "."
const token = require("./token.json")


client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content.startsWith(`${prefix}takehelp`)) {
    let memberrole = msg.guild.roles.get('759887735699275837')
    let takehelp = msg.guild.roles.get('767527649857110036')
    const user = msg.mentions.members.first();
    user.addrole(takehelp).catch(console.error);
    user.removerole(memberrole).catch(console.error);
  }
});

client.login(token);
