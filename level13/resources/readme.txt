strings level13

Видишь зашифрованный токен и требование быть uid=4242

gdb level13
break *0x804859a
set $eax = 4242
continue
