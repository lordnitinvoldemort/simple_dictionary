import json
import difflib
from difflib import get_close_matches

data = json.load(open("G:\dict\data.json"))

def dict(w):
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys(),n=1)) > 0 :
		s = get_close_matches(w, data.keys(),n=1)[0]
		print("Did you mean %s ? If Yes type 'Y' or 'N' for no." %(get_close_matches(w, data.keys())[0]))
		i  = input()
		if i is 'Y' or i is 'y':
			return data[s]
		elif i is 'N' or i is 'n':
			return "No such word in dictionary."
		else:
			return "Invalid input!! BUMMER"
	else:
		return "No such word in dictionary."


word = input("Enter a word:")
output = dict(word.lower())

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)


