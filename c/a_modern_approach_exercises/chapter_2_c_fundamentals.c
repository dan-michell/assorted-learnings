#include <stdio.h>

#define PI 3.14159f

void ex_one_hello_world(void);
void ex_four_unassigned_var(void);
void proj_two_sphere(int r);
void proj_four_tax(float tax);

int main(void)
{
    // one_hello_world();
    // ex_four_unassigned_var();
    // proj_two_sphere(4);
    proj_four_tax(5.0);

    return 0;
}

void ex_one_hello_world(void)
{
    printf("hello, world\n");
}

void ex_four_unassigned_var(void)
{
    int a;
    float b;
    int c;
    float d;

    printf("%i\n", a);
    printf("%f\n", b);
    printf("%i\n", c);
    printf("%f\n", d);
}

void proj_two_sphere(int r)
{
    float v = (4.0f / 3.0f) * PI * (r * r * r);

    printf("Volume of %im sphere: %f", r, v);
}

void proj_four_tax(float tax)
{
    float amount;

    printf("Enter amount: ");
    scanf("%f", &amount);

    float with_tax = amount * (1 + tax / 100.0);

    printf("Amount with %.2f%% tax: %.2f", tax, with_tax);
}