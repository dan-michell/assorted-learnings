#include "quiz_one.h" // Include related header file to enable compiler to catch errors
#include <iostream>

void add_and_subtract()
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
