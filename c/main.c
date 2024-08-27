#include <stdio.h>

// Even though meow is defined after main, it is still recognized by the compiler by adding a function prototype before. A function prototype is a declaration of a function that tells the compiler about the number of arguments the function takes and the type of the return value. Essentially tells the compiler that it doesn't exist yet, but it will.
void meow(int);

int main(void)
{
    meow(3);

    return 0;
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("Meow!\n");
    }
}

int add(int x, int y)
{
    return x + y;
}