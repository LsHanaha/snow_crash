# Выясняем, что токен уже у нас есть, но он слегка зашифрован.
# Понимаем, что шифр суть есть прибавление индекса символа в слове к коду символа
# Копируем токен к себе на машину через scp и пишем питонячий скрипт расшифровки для

with open('token', 'rb') as f:
    text = f.read()

print(text, len(text))

for i, char in enumerate(text):
    if char - i < 0:
        continue
    print(chr(char - i), end='')
