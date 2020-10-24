import sys

if len(sys.argv) <= 1:
	print("Подайте шифрованную строку как аргумент.")
	exit()

arg = [ord(c) - ord("a") for c in sys.argv[1]]
for i in range(26):
	var = [(c + i) % 26 + ord("a") for c in arg]
	var = [chr(c) for c in var]
	var = "".join(var)
	print(var)
