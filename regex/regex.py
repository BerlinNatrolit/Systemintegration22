import re

s = "abcde"
print(re.search(("abc"), s))		# vi matchar abc med strängen s. Dvs en matchning men bara delvis.

s = "abcde"
print(re.search(("abcde"), s))		# full match på abcde

s= "abcde"
r= "\w"								# matchar mot en bokstav.
print(re.search(r,s))

s= "abcde"
r= "\w+"							# matchar mot en eller flera bokstäver.
print(re.search(r,s))

s= "abcde1234"
r= "\w+\d+"							# matchar mot en eller flera bokstäver och därefter en eller flera siffror.
print(re.search(r,s))

s= "1234abcd"
r= "\w+\d+"							# matchar mot siffrorna, men itne bokstäverna. INTE vad vi vill antagligen
print(re.search(r,s))

s= "1234abcd"
r= "^\w+\d+$"							# matchar itne längre. Nu specar vi start och slut på sträng.
print(re.search(r,s))

s= "ABC123"		#registreringsnummer (gammal)    ABC123 och ABC 123
r= "^\w{3} ?\d{3}$"
print(re.search(r,s))

s= "ABC12D"		#registreringsnummer (nytt)    ABC123 och ABC 123
r= "^\w{3} ?\d{2}(\w|\d)$"
print(re.search(r,s))

s= "jim.ber@nat.se"	# _@b.co
r = "^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$"
print(re.search(r,s))


s= "jim.ber@nat.se,\nsim.mar@kyh.stud.se"		# matcha mot flera giltiga emailadresser separerade med komma
r = "(([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6}),?\s?)+"
print(re.search(r,s))


