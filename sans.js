const Discord = require('discord.js');
const client = new Discord.Client();
const prefix = "."
const token = "yourtoken"


client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
const author = msg.author;
if (author) {
    member = msg.member;
    if (member) {
        if (member.roles.cache.some(role => role.name === 'Helper')) {
  if (msg.content.startsWith(`${prefix}takehelp`)) {
    let memberrole = msg.guild.roles.cache.get('759887735699275837')
    let takehelp = msg.guild.roles.cache.get('767527649857110036')
    const user = msg.mentions.members.first();
    user.roles.add(takehelp).catch(console.error);
    user.roles.remove(memberrole).catch(console.error);
    msg.channel.send(`<@${user.id}> has lost help access. Noob.`)
  }
  else if (msg.content.startsWith(`${prefix}givehelp`)) {
    let memberrole = msg.guild.roles.cache.get('759887735699275837')
    let takehelp = msg.guild.roles.cache.get('767527649857110036')
    const user = msg.mentions.members.first();
    user.roles.remove(takehelp).catch(console.error);
    user.roles.add(memberrole).catch(console.error);
    msg.channel.send(`<@${user.id}> has regained help access.`)
  }
  else if (msg.content.startsWith(`${prefix}givesmallhelp`)) {
      let smallhelp = msg.guild.roles.cache.get('766028882591612968');
      const user = msg.mentions.members.first();
      user.roles.add(smallhelp).catch(console.error);
      msg.channel.send(`<@${user.id}> has been given the Individual Help role.`)
  }
  else if (msg.content.startsWith(`${prefix}takesmallhelp`)) {
    let smallhelp = msg.guild.roles.cache.get('766028882591612968');
    const user = msg.mentions.members.first();
    if (member.roles.cache.some(role => role.name === 'Individual Help')) {
        user.roles.remove(smallhelp).catch(console.error);
        msg.channel.send(`<@${user.id}> has lost the Individual Help role.`)
    }
    else {
        msg.channel.send(`That user doesn't have the Individual Help role!`)
    }
  }
 } } }
});

client.login(token);