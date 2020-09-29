import crypt
from string import ascii_lowercase as lowercase
import sys
from itertools import combinations_with_replacement

target = sys.argv[1]
salt = target[:2]

for length in range(1, 16):
	print("Checking length ", length, flush=True)
	for comb in combinations_with_replacement(lowercase, length):
		raw_passwd = "".join(comb)
		passwd = crypt.crypt(raw_passwd, salt=salt)
		if passwd == target:
			print(raw_passwd)
			exit(0)
