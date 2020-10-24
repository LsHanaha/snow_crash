strings level13
objdump -M intel -C -d -s level13

Видишь зашифрованный токен и требование быть uid=4242

gdb level13
break *0x804859a # адрес проверки uid
set $eax = 4242
continue

=====
Вывод: см. level14
