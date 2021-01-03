from multicraftapi import MulticraftAPI

# Arguments: (url, username, api_key)
client = MulticraftAPI("https://panel.pebblehost.com/api.php", "Nathanhowe@outlook.com", "5SeYiXuu4UDU4o")


def whitelist(name):
	# Arguments: (function, *args)
	response = client("sendConsoleCommand", "154936", f"whitelist add {name}")

	# Response is always JSON in form {'success': <success_status>, 'errors': [<errors>], 'data':[<returned data>]}
	return response


def unwhitelist(name):
	# Arguments: (function, *args)
	response = client("sendConsoleCommand", "154936", f"whitelist remove {name}")

	# Response is always JSON in form {'success': <success_status>, 'errors': [<errors>], 'data':[<returned data>]}
	return response

