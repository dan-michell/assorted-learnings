#include "quizzes/quiz_four.h"
#include "quizzes/quiz_one.h" // Double quotes for own file, angled brackets for external header.
#include "quizzes/quiz_two.h"
#include <iostream>

#define PRINT_HELLO

// void chapter_one_quiz_challenge(); // Declare function prototype to use before actual definition

void initialisation_techniques() {
    int a; // default-initialization (no initializer)

    std::cout << a << std::endl; // Should be random value already assigned to mem. loc. however
                                 // clang will initialise as 1 in debug build mode.

    // Traditional initialization forms:
    int b = 5; // copy-initialization (initial value after equals sign)
    int c(6);  // direct-initialization (initial value in parenthesis)

    // Modern initialization forms (preferred):
    int d{7}; // direct-list-initialization (initial value in braces)
    int e{};  // value-initialization (empty braces)

    // int w1 { 4.5 }; // compile error: list-init does not allow narrowing conversion

    // int w2 = 4.5; // compiles: w2 copy-initialized to value 4
    // int w3(4.5); // compiles: w3 direct-initialized to value 4
}

int double_int(int x) { return x * 2; }

int main() {
    // Quizzes

    // Chapter 1
    // add_and_subtract();

    // Chapter 2
    // user_sum();

    // Chapter 3

    // Chapter 4
    // four_two();
    four_three();

#if 0 // Easy way to enable / disable code
    initialisation_techniques();
#endif

#ifndef PRINT_HELLO
    /*
     * - '<<' is the insertion operator
     * - cout / cin output and take in data from buffers. FIFO.
     * -'::' is the scope resolution operator. The identifier to the left of the symbol declares
     * the namespace that the name to the right of the symbol belongs to.
     */
    std::cout << "Hello, World!" << std::endl;
#endif
}
