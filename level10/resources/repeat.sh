# Предварительно копируем файлы на vm через scp
cd /tmp
gcc race.c
for i in {1..1000};
do
	./a.out
done
