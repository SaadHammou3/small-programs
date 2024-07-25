# PyHash by Saad Hammou
# This program hashes strings and can decrypt strings it already hashed.

# Importing required modules
import hashlib
import sys

# Makes string a hash and adds it to database

def hashing_service(hashing_query):
	# Selecting hashing algorithm
	hashing_algorithm = input("1-MD5/2-SHA512/3-SHA256\n")

	# while loop for loop's sake
	if int(hashing_algorithm) == 1: 
		# the magic happens
		hashed = hashlib.md5(hashing_query.encode('utf-8')).hexdigest()
		# adds the string and the hash to the hash dictionary for later use
		hashdic[hashing_query] = hashed
		# print hash to show that the program did its work
		print("Your hash is: " + hashed)
	elif int(hashing_algorithm) == 2:
		hashed = hashlib.sha512(hashing_query.encode('utf-8')).hexdigest()
		hashdic[hashing_query] = hashed	
		print("Your hash is: " + hashed)
	elif int(hashing_algorithm) == 3:
		hashed = hashlib.sha256(hashing_query.encode("utf-8")).hexdigest()
		hashdic[hashing_query] = hashed
		print("Your hash is: " + hashed)	

# Dictionary containing the words and their hashes for "decryption" :)

hashdic = {
	"hello" : "5d41402abc4b2a76b9719d911017c592",
	"how are you" : "655549fcf09f8443d789424e001ec753",
	"saad" : "347602146a923872538f3803eb5f3cef",
	"the" : "8fc42c6ddf9966db3b09e84365034357",

} 

# variable for exiting the loop, thus exiting the program

exit_var = 0

# Menu loop

while exit_var != 1:
	# Choosing an action
	menu_choice = input("(1)-Hashing\n(2)-Decrypting\n(3)- Exit\n")
	if int(menu_choice) == 1:
		hashing_query = input("Please enter the word you want hashed: ")
		hashing_service(hashing_query)

	elif int(menu_choice) == 2:
		decrypt_query = input("Please enter the hash you want decrypted: ")
		for key in hashdic:
			if hashdic[key] == decrypt_query:
				print(key)
	else:
		exit_var += 1	
