with open('token', 'rb') as f:
    text = f.read()

print(text, len(text))

for i, char in enumerate(text):
    if char - i < 0:
        continue
    print(chr(char - i), end='')
