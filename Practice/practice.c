#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <string.h>

void operatorUnderstand(){
    
    int x = INT_MIN;
    printf("Number Play\n\n");
    printf("%d\n", x - 1);
    printf("x = %d\n", x);
    printf("%d\n", x + 1); 
    printf("\nleft shift\n");
    printf("%d\n", x << 1);
    printf("%d\n", x << 2);
    printf("\nright shift\n");
    printf("%d\n", x >> 1);
    printf("%d\n", x >> 2);
}

void switchCase(){
    // int a = 0 ? 0/0 : -1;
    // printf("a = %d\n", a);

    // int b = 10/2.5;
    // printf("b = %d\n", b);

    int y = 2;
    char x = 'A';
    switch (x+2) {
        default:
            printf("x = default\n");
            break;
        case 65:
            printf("x = A\n");
            break;
        case 'C':
            printf("x = 67\n");
            break;
    }

}

void loopPlay(){
    int i = 6;
    // for (printf("Meow\n");
    //     printf("\tHi %d", i) < printf(" < 10\n");
    //     printf("Let's go again\n"))
    //     {
    //         i++;
    //         printf("Inside for loop\n\n");
    //     }
    // printf("Outside for loop\n\n");

    for(printf("Meow\n"), i = 0, i=5; i < 10 && printf("\tcondition\t"); i++, printf("Let's go again\n")){
        printf("Inside for loop\n\n");
    }
}

void arrayPlay(){

    // int a = 100, x;
    // char b = 90, y;
    // x = a + b; 
    // y = a + b;
    // printf("x: %d, y: %d\n", x, y);

    int arr[4] = {1, 7};
    printf("\nSize of arr: %d\n", sizeof(arr));
    printf("Hexadecimal\t\tDecimal\t\tValue\n");
    for (int i = 0; i < 4; i++) {
        printf("%p\t->\t%u\t->\t%d\n", &arr[i], &arr[i], arr[i]);
    }
    // int (*p1)[4] = &arr;
    int *p2 = arr;

    // printf("\nPointer p1\t: %p -> %d\n", p1, *p1);
    // printf("Pointer p1+1\t: %p -> %d\n", p1 + 1, *(p1 + 1));
    // printf("Pointer p1+2\t: %p -> %d\n", p1 + 2, *(p1 + 2));
    printf("\nPointer p2\t: %p -> %d\n", p2, *p2);
    printf("Pointer p2+1\t: %p -> %d\n", p2 + 1, *(p2 + 1));
    printf("Pointer p2+2\t: %p -> %d\n", p2 + 2, *(p2 + 2)); 
    printf("\nAddress &arr\t: %p -> %u\n", &arr, &arr);
    printf("Address &arr+1\t: %p -> %u\n", &arr + 1, &arr + 1);
    printf("Address &arr+2\t: %p -> %u\n", &arr + 2, &arr + 2);
    
}

void arrayPointer(){
    int i, a[] = {1,2,3,4};
    for (i = 0; i < 4; i++) {
        printf("%d ", a[i]);
    }
    printf("\n\n");

    int *p = a;
    p[2] = 7;
    p++;
    p[-1] = -10;
    a[3] = 0;

    for (i = 0; i < 4; i++) {
        printf("%d ", a[i]);
    }
}

int *return_pointer() {
    int a = 10;
    int *p = &a;

    printf("Inside function: %d\n", *p);
    return p;
}

void pointerPlay(){
    // int *ptr;
    // ptr = return_pointer();
    // printf("Outside function: %d\n", *ptr+1); 

    int *p, a;
    char *q, b;
    double *r, c;

    // printf("\nSize of int pointer: %zu\n", sizeof(p));
    // printf("Size of int: %zu\n", sizeof(a));
    // printf("\nSize of char pointer: %zu\n", sizeof(q));
    // printf("Size of char: %zu\n", sizeof(b));
    // printf("\nSize of double pointer: %zu\n", sizeof(r));
    // printf("Size of double: %zu\n", sizeof(c));

    // int x = printf("%zu", sizeof(p));
    // printf("\nx = %d\n", x);

    a = 1000;
    p = &a;
    printf("p = %p -> %d\n", p, *p);
    printf("p+1 = %p -> %d\n", p+1, *(p+1));
    q = &a;
    printf("\nq = %p -> %d\n", q, *q);
    printf("q+1 = %p -> %d\n", q+1, *(q+1));
    printf("q+2 = %p -> %d\n", q+2, *(q+2));
    printf("q+3 = %p -> %d\n", q+3, *(q+3));
}

void stringPlay(){
    char name[] = "Nigga";
    int x = sizeof(name);
    // printf("Size of name: %d\n", x);
    // printf("\nname: %s\n", name);
    // printf("name[0]: %c\n", name[0]);
    // printf("name[5]: %c\n", name[5]);

    // name[0] = 'G';
    // printf("\nname: %s\n", name);

    // name[5] = 'G';
    // printf("\nname[5]: %c\n", name[5]);

    // name[5] = '\0';
    // printf("\nname: %s\n", name);

    // char *n = "Hello";
    // printf("n: %p -> %s\n", n, n);
    // n = "World";
    // printf("n: %p -> %s\n", n, n);

    // printf("%p -> %s\n", "Hello", "Hello");
    // printf("%p -> %c\n", &"Hello"[0], "Hello"[0]);
    // printf("%p -> %c\n", &"Hello"[1], "Hello"[1]);
    // printf("%p -> %c\n", &"Hello"[2], "Hello"[2]);
    // printf("%p -> %c\n", &"Hello"[3], "Hello"[3]);
    // printf("%p -> %c\n", &"Hello"[4], "Hello"[4]);
    // printf("%p -> %d\n", &"Hello"[5], "Hello"[5]);
    // printf("%p -> %c\n", &"Hello"[6], "Hello"[6]);
    // printf("%p -> %c\n", &"Hello"[7], "Hello"[7]);
}

union unionA {
    int a;
    char b;
};

struct structA {
    int a;
    char b;
};

void structureUnionPlay(){
    union unionA u;
    struct structA s;

    printf("Size of union: %zu\n", sizeof(u));
    printf("Size of struct: %zu\n", sizeof(s));
}