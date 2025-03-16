import hashlib as hl, getpass as gp
import os
from dotenv import load_dotenv

while True:
	os.system("clear")

	print("=== Account Sign-In ===")
	username = input("Username: ")


	password = hl.sha256(gp.getpass("Password: ").encode()).hexdigest()

	load_dotenv()
	try:
		check = os.getenv(username)
		if check == password:
			print("Logging in...")
			break
		elif check == None:
			input(f"No username exists named {username}.")
		else:
			input("Incorrect Password")
	except:
		input(f"No username exists named {username}.")


print("Welcome to the account")
