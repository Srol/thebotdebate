import markovify
import random

def convert_to_markov(filename):
	with open(filename) as f:
		text = f.read()
	return text

bush = markovify.Text(convert_to_markov("bush.txt"))
carson = markovify.Text(convert_to_markov("carson.txt"))
christie = markovify.Text(convert_to_markov("christie.txt"))
cruz = markovify.Text(convert_to_markov("cruz.txt"))
fiorina = markovify.Text(convert_to_markov("fiorina.txt"))
huckabee = markovify.Text(convert_to_markov("huckabee.txt"))
kasich = markovify.Text(convert_to_markov("kasich.txt"))
moderator = markovify.Text(convert_to_markov("moderator.txt"))
paul = markovify.Text(convert_to_markov("paul.txt"))
rubio = markovify.Text(convert_to_markov("rubio.txt"))
trump = markovify.Text(convert_to_markov("trump.txt"))

static_candidates = {"bush":bush, "carson":carson, "christie":christie, "cruz":cruz, "fiorina":fiorina, "huckabee":huckabee, "kasich":kasich, "paul":paul, "rubio":rubio, "trump":trump}
candidates = {"bush":bush, "carson":carson, "christie":christie, "cruz":cruz, "fiorina":fiorina, "huckabee":huckabee, "kasich":kasich, "paul":paul, "rubio":rubio, "trump":trump}
used_candidates = []

def questions():
	global candidates
	global used_candidates
	pick = random.choice(candidates.keys())
	while pick in used_candidates:
		pick = random.choice(candidates.keys())
	response = pick.upper() + ": " + candidates[pick].make_sentence()
	for key, value in candidates.iteritems():
		if key.title() in mod_question:
			pick = key
			while pick in used_candidates:
				pick = random.choice(candidates.keys())
			response = pick.upper() + ": " + candidates[pick].make_sentence()		
	while len(response) < 200:
		response = pick.upper() + ": " + candidates[pick].make_sentence()
	used_candidates.append(pick)
	if not used_candidates:
		used_candidates = []
	return response
	
mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

mod_question = moderator.make_sentence()
print "MODERATOR: " + mod_question
print questions()

print "******** USED CANDIDATES SHOULD BE NONE********"
print used_candidates