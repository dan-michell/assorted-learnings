#include "quiz_four.h"
#include <iostream>

double read_double() {
    double x;

    std::cout << "Enter a double: ";
    std::cin >> x;

    return x;
}

double calculate_result(double x, double y, char symbol) {
    switch (symbol) {
    case '+':
        return x + y;
    case '-':
        return x - y;
    case '*':
        return x * y;
    case '/':
        return x / y;
    default:
        std::cout << "Invalid input!\n";
        return 0.0;
    }
}

int four_two() {
    double x{read_double()};
    double y{read_double()};

    char symbol{};
    std::cout << "Enter a symbol (+, -, *, or /): ";
    std::cin >> symbol;

    std::cout << x << ' ' << symbol << ' ' << y << ' ' << "is " << calculate_result(x, y, symbol)
              << '\n';

    return 0;
}

int four_three() {
    double x{};
    std::cout << "Enter height (m): ";
    std::cin >> x;

    for (int i = 0; i <= 5; i++) {
        double distance_travelled{9.8 * (i * i / 2.0)};

        std::cout << "At " << i << (distance_travelled >= 0)
            ? " seconds, the ball is at height: " << x - distance_travelled << " metres\n";
    }

    return 0;
}
