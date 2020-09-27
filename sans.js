const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content.startsWith('.dpyjs')) {
    msg.channel.send('Sans is now partially hosted in discord.js :wink:')
  }
  else if (msg.content.startsWith('.vc')) {
	  if (msg.content.startsWith('.vc 3ds')) {
		  msg.channel.send('You can convert your roms to CIA format with this tool: https://mega.nz/#!qnAE1YjC!q3FRHgIAVEo4nRI2IfANHJr-r7Sil3YpPYE4w8ZbUPY \n' + 
							'Usage guide here: http://3ds.eiphax.tech/nsui.html')
		}
	  else if (msg.content.startsWith('.vc wiiu')) {
		msg.channel.send('You can play classics on your wiiu with this tool: https://gbatemp.net/threads/release-uwuvci-injectiine.486781/ \n' +
						'Usage guide here: https://flumpster.github.io/instructions/index')
		}
	  else {
	  msg.channel.send('Invalid syntax. Options are: 3ds, wiiu.')
	  }
	}
});

client.login('');
