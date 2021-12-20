#include <unistd.h>
#include <stdio.h>
#include <sys/fcntl.h>

int main(void) {
    char buf[50];
    gets(buf);
    printf("Yo %s\n", buf);
    close(0);
    printf("%d\n", O_RDWR | O_NOCTTY);
    open("/dev/tty", O_RDWR | O_NOCTTY);
    execve ("/bin/sh", NULL, NULL);
}
