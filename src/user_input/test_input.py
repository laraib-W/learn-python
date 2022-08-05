"""User input

@see https://docs.python.org/3/library/functions.html#input

User input prompts are very helpful when it comes to interactive programming. Not only in games but also in standard file operations, you may want your user to interact with the program.
Therefore, the user needs the opportunity to be able to put in information.
"""


def user_input():
	"""Input prompt"""

	# Printing statement to signal the user that we are waiting for input.
	user_input = input("Please type in your name\n")

	# Printing a message based on the input.
	print(f"Welcome, {user_input}!")

	user_input = input("Please enter the list comma seperated\n")

	lst= [int(i) for i in user_input.split(',')]

	print(lst)
