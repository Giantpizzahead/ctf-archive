
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <stdlib.h>

#define FLAG_SIZE 256
#define FLAG_FILE "./flag"

unsigned int USER_CODE = 100; 
unsigned int SAFE_CODE = 333;

void OP_ADD_1()
{
    USER_CODE += 1;
}
void OP_ADD_10()
{
    USER_CODE += 10;
}
void OP_ADD_100()
{
    USER_CODE += 100;
}

void win()
{
    char buf[FLAG_SIZE];
    memset(buf, 0, FLAG_SIZE);
    FILE *f = fopen(FLAG_FILE, "r");
    if (f == NULL)
        printf("Missing flag file! Please contact support if you see this error on the remote target!\n");
    else
    {
        fgets(buf, FLAG_SIZE, f);
        printf("\n");
        if (USER_CODE == SAFE_CODE)
        {
            write(STDOUT_FILENO, buf, strlen(buf));
            exit(0);
        }
        else
            write(STDOUT_FILENO, "Invalid password!\n", 19);
        printf("\n");
    }
    close((int)f);
}

void vuln()
{
    printf("---\nSUPER SAFE SOFTWARE v1.0\n  Unhackable since 2020*\n---\n");
    printf("Enter password: ");
    char buff[FLAG_SIZE];
    memset(&buff, 0, FLAG_SIZE);
    fgets(buff, FLAG_SIZE*2, stdin);
    win();
}

int main (int argc, char *argv[])
{
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    
    vuln();
    return 0;
}
    