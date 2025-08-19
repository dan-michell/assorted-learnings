#include "chapter_one_quiz.h"
#include <iostream>

void chapter_one_quiz_challenge()
{
    // Take two integers. Print the result of adding and subtracting these.
    int x;
    int y;

    std::cout << "Enter an integer: ";
    std::cin >> x;

    std::cout << "Enter a second integer: ";
    std::cin >> y;

    std::cout << x << " + " << y << " is " << x + y << ".\n";
    std::cout << x << " - " << y << " is " << x - y << ".\n";
}
