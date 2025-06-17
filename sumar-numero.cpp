#include <iostream>

//Escribir un programa que pida al usuario dos números y los sume.


int sumanumero(int a, int b) {
    return a + b;
}

int main() {

    using std::cin;
    using std::cout;
    using std::endl;

    int numero1;
    int numero2;
    int sumas;


    cout << "Escribe el primer numero: ";
    cin >> numero1;
    cout << "Escriba el segundo numero: ";
    cin >> numero2;

    
    sumas = sumanumero(numero1, numero2);
    cout << "La suma es: " << sumas;




    return 0;
}