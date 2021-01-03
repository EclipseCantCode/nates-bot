from commands.base_command import BaseCommand
import main
from sql import *

def hasrole(author, role):
	for x in author.roles:
		if x.name == role:
			return True
	return  False

class addwhitelist(BaseCommand):
	def __init__(self):
		description = "Add a whitelist. One per sub, unlimited per admin"
		params = ["name"]
		super().__init__(description, params)

	async def handle(self, params, message, client):
		author = message.author
		is_admin = hasrole(author, "Moderator")
		is_sub = hasrole(author, "Subscriber")

		if add_whitelist(author.id, params[0], is_sub, is_admin):
			await message.channel.send("Added!")
			main.whitelist(params[0])
		else:
			await message.channel.send("You don't fit the roles needed to do this, or you already have an account linked!")


class removeWhitelist(BaseCommand):
	def __init__(self):
		description = "Remove a whitelist."
		params = ["name"]
		super().__init__(description, params)

	async def handle(self, params, message, client):
		author = message.author
		is_admin = hasrole(author, "Moderator")

		if remove_whitelist(author.id, params[0], is_admin):
			await message.channel.send("Removed!")
			main.unwhitelist(params[0])
		else:
			await message.channel.send("You don't fit the roles needed to do this!")