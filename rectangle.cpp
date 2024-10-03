#include <iostream>

int area(int a, int b) {
    return a * b;
}

int perimeter(int a, int b) {
    return (a + b)*2;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << "area: " << area(a, b) << " perimeter: " << perimeter(a,b);

}

