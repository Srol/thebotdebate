kasich = []
huckabee = []
bush = []
rubio = []
trump = []
carson = []
fiorina = []
cruz = []
christie = []
paul = []
moderators = []
x = 1

with open("firstdebateraw.txt") as f:
	transcript = f.readlines()

for index, line in enumerate(transcript):
	if line[:3].isupper():
		if line[:3] == "KAS":
			kasich.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					kasich.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "HUC":
			huckabee.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					huckabee.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "BUS":
			bush.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					bush.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "RUB":
			rubio.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					rubio.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "TRU":
			trump.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					trump.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "CAR":
			carson.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					carson.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "FIO":
			fiorina.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					fiorina.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "CRU":
			cruz.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					cruz.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "CHR":
			christie.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					christie.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "PAU":
			paul.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					paul.append(transcript[index + x])
					x += 1
				else:
					x = 1
		elif line[:3] == "KEL" or line[:3] == "BAI" or line[:3] == "WAL":
			moderators.append(line)
			if len(transcript) > index + 10:
				while transcript[index + x][:3].isupper() == False:
					moderators.append(transcript[index + x])
					x += 1
				else:
					x = 1
		else:
			print "Unknown debate participant: " + line + "$$$$$ index = " + str(index)

f = open("kasich.txt","a")

for item in kasich:
	f.write(item + "\n")

f.close()

f = open("moderator.txt","a")

for item in moderators:
	f.write(item + "\n")

f.close()
					
f = open("huckabee.txt","a")

for item in huckabee:
	f.write(item + "\n")

f.close()

f = open("bush.txt","a")

for item in bush:
	f.write(item + "\n")

f.close()

f = open("rubio.txt","a")

for item in rubio:
	f.write(item + "\n")

f.close()

f = open("trump.txt","a")

for item in trump:
	f.write(item + "\n")

f.close()

f = open("carson.txt","a")

for item in carson:
	f.write(item + "\n")

f.close()

f = open("fiorina.txt","a")

for item in fiorina:
	f.write(item + "\n")

f.close()

f = open("cruz.txt","a")

for item in cruz:
	f.write(item + "\n")

f.close()

f = open("christie.txt","a")

for item in christie:
	f.write(item + "\n")

f.close()

f = open("paul.txt","a")

for item in paul:
	f.write(item + "\n")

f.close()