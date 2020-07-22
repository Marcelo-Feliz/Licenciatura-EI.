#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

void main(void)
{
    pid_t pid, pid2;

    pid = fork();
    pid2 = fork();
    printf("o pid é %d, %s\n", pid, "pau");

    puts("Hello");
}
