#include <iostream>
#include "aa.hpp"

template<>
void A<X>::print() {
    std::cout << "X" << std::endl;
}

template<>
void A<Y>::print() {
    std::cout << "Y" << std::endl;
}

int main() {
    A<X> x;
    A<Y> y;
    x.print();
    y.print();
}
