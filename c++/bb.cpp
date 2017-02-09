#include <iostream>

class A {
public:
	A() {
		std::cout << "Constructing A..." << std::endl;
	}
	~A() {
		std::cout << "Deconstructing A..." << std::endl;
	}
	int print() {
		std::cout << data << std::endl;
	}
	int data = 10;
};

class B {
public:
	B(A &a): data(a) {
		std::cout << "Constructing B..." << std::endl;
	}
	B(A &&a): data(a) {
		std::cout << "Constructing B..." << std::endl;
	}
	~B() {
		std::cout << "Deconstructing B..." << std::endl;
	}
	int print() {
		std::cout << data.data << std::endl;
	}
	int a(int i) {
		data.data = i;
	}
private:
	A &data;
};

int main() {
	A a;
	B b(a);

	std::cout << "b.print: ";
	b.print();
	std::cout << "a.print: ";
	a.print();

	std::cout << "b.a(5)..." << std::endl;
	b.a(5);

	std::cout << "b.print: ";
	b.print();
	std::cout << "a.print: ";
	a.print();

	return 0;
}








