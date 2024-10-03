#include <iostream>

float area(int a, int b) {
    return a * b * 0.5;
}

int perimeter(int a, int b, int c) {
    return a + b + c;
}

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    std::cout << "area: " << a << " perimeter: " << b;
}

