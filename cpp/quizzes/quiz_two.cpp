#include "quiz_two.h"
#include <iostream>

int read_number()
{
    int x;

    std::cout << "Enter a number: ";
    std::cin >> x;

    return x;
}

void write_answer(int x)
{
    std::cout << "Answer: " << x << std::endl;
}

int user_sum()
{
    int x = read_number();
    int y = read_number();

    write_answer(x + y);

    return 0;
}
