
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

#define FLAG_SIZE 256
#define FLAG_FILE "./flag"

#define NAME_SIZE 20
typedef struct _node
{
    struct _node* next;
    char name[NAME_SIZE];
    unsigned int pin;
} node;
node* head = NULL;

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

void view_secrets()
{
    node* admin = head;
    if (admin->pin != 2020)
    {
        printf("Access denied!\n");
        printf("Your administrator seems to have the wrong PIN number configured!\n");
        printf("Please ask them to change it!\n");
        printf("Good bye!\n");
    }
    else
    {
        printf("Access granted!\n");
        win();
    }
    exit(0);
}

void add_admin()
{
    node* new = (node*)malloc(sizeof(node));
    new->next = NULL;
    sprintf(&new->name, "%s", "Administrator");
    new->pin = 1234;
    head = new;
}

void add()
{
    node* new = (node*)malloc(sizeof(node));
    printf("Debug: Allocated at %p\n", new);
    new->next = NULL;

    printf("Enter employee name: ");
    memset(new->name, 0, NAME_SIZE);
    scanf("%18s", &new->name);
    printf("Enter employee 4-digit pin: ");
    scanf("%4d", &new->pin);

    // add after head
    node *ptr = head;
    while (ptr->next != NULL)
        ptr = ptr->next;
    ptr->next = new;

    printf("Success!\n");
}

void delete()
{
    if (head == NULL) 
    {
        printf("There are no employees\n");
        return;
    }

    printf("Employee ID to remove: ");
    unsigned int id;
    scanf("%x", &id);
    node *selected = (node*)id;
    
    if (selected == head)
    {
        printf("You are not allowed to delete the system administrator!\n");
        free(selected); // Jake (intern): added this to fix memory leak! please hire me :)
        return;
    }
    
    // traverse to employee pointer
    node *ptr = head, *prev;
    while (ptr && ptr != selected)
    {
        prev = ptr;
        ptr = ptr->next;
    }

    if (ptr == NULL)
    {
        printf("Error : Employee ID\n");
        return;
    }

    prev->next = ptr->next;
    free(ptr);
    printf("Success! Removed %p\n", selected);
}

void print()
{
    node* ptr = head;
    uint32_t i = 0;
    printf("---\nListing Employees\n---");
    while(ptr != NULL)
    {
        printf("\n\n> Employee Id: %p\n> Name: %s\n> PIN: %d\n", ptr, ptr->name, ptr->pin);
        ptr = ptr->next;
        i++;
    }
    printf("\n\n");
}

#define BANNER "\x20\x20\x20\x20\x20\x20\x20\x2e\x2d\x2d\x2d\x2e\x0a\x20\x20\x20\x20\x20\x20\x2f\x20\x20\x20\x20\x20\x5c\x0a\x20\x20\x20\x20\x20\x20\x5c\x2e\x40\x2d\x40\x2e\x2f\x0a\x20\x20\x20\x20\x20\x20\x2f\x60\x5c\x5f\x2f\x60\x5c\x0a\x20\x20\x20\x20\x20\x2f\x2f\x20\x20\x5f\x20\x20\x5c\x5c\x0a\x20\x20\x20\x20\x7c\x20\x5c\x20\x20\x20\x20\x20\x29\x7c\x5f\x0a\x20\x20\x20\x2f\x60\x5c\x5f\x60\x3e\x20\x20\x3c\x5f\x2f\x20\x5c\x0a\x20\x20\x20\x5c\x5f\x5f\x2f\x27\x2d\x2d\x2d\x27\x5c\x5f\x5f\x2f"
int main()
{
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    add_admin(); // add admin user

    int opt = 0;
    while(true)
    {
        printf("---\nAdvanced Employee Management System v1.0\n---\n%s\n", BANNER);
        printf("\nOptions:\n\n 1. New Employee\n 2. Remove Employee\n 3. Access Secret HR Files\n 4. List Employees\n 5. Exit\n\n> ");
        scanf("%1d", &opt);
        switch(opt)
        {
            case 1:
                add();
                break;
            case 2:
                delete();
                break;
            case 3:
                view_secrets();
                break;
            case 4:
                print();
                break;
            case 5:
                exit(0);
        }
    }
}
    