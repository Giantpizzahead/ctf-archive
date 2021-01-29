
#include <stdio.h>
#include <unistd.h>

#define FLAG_SIZE 256
#define FLAG_FILE "./flag"

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
        write(STDOUT_FILENO, buf, strlen(buf));
        printf("\n");
    }
    exit(0);
}

void vuln()
{
    printf("---\nSECURITY CLEARANCE LEVEL CHECKER\n---\n");
    printf("Enter clearance level #(1-6): ");
    
    int level;
    scanf("%i", &level);
    printf("%i\n", level);

    if (level > 6)
    {
INVALID:
        printf("Invalid level!\n");
        exit(0);
    }
    switch ((short)level)
    {
        case 1:
            printf("CONTROLLED UNCLASSIFIED\n");
            break;
        case 2:
            printf("PUBLIC TRUST\n");
            break;
        case 3:
            printf("CONFIDENTIAL\n");
            break;
        case 4:
            printf("SECRET\n");
            break;
        case 5:
            printf("TOP SECRET (TS)\n");
            break;
        case 6:
            printf("TOP SECRET / SENSITIVE COMPARTMENTED INFORMATION (TS/SCI)\n");
            break;
        case 1337:
            printf("ADVANCED PERSISTENT THREAT (APT)\n");
            win();
            break;
        default:
            printf("Level %i\n", (short)level);
            goto INVALID;
    }
}

int main (int argc, char *argv[])
{
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    
    // vuln
    vuln();
    return 0;
}
    