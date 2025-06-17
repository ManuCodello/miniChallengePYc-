#include <iostream>
#include <string>
#include <algorithm> 

bool esPalindromo(const std::string& cadena) {
    int inicio = 0;
    int fin = cadena.length() - 1;

    while (inicio < fin) {
        if (cadena[inicio] != cadena[fin]) {
            return false;
        }
        ++inicio;
        --fin;
    }

    return true;
}

int main() {
    std::string texto;

    std::cout << "Ingrese una cadena: ";
    std::getline(std::cin, texto);  

    std::transform(texto.begin(), texto.end(), texto.begin(), ::tolower);

    if (esPalindromo(texto)) {
        std::cout << "Es un palindromo." << std::endl;
    } else {
        std::cout << "No es un palindromo." << std::endl;
    }

    return 0;
}
