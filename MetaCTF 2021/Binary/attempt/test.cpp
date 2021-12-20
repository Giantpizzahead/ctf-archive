#include <unistd.h>
#include <cstdio>
#include <iostream>
#include <fcntl.h>
using namespace std;

int main() {
        cout << O_RDONLY << '\n';
        cout << open("flag.txt", 0, 0) << '\n';
        /*
        char *args[2];
        args[0] = "//bin/sh";
        args[1] = NULL;
        execve(args[0], NULL, NULL);
        */
}