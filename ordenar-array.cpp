#include <iostream>

// Imprimir el array actual
void imprimir(int* arr, int tam) {
    for (int i = 0; i < tam; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

// Bubble sort con punteros
void ordenar_lista(int* arr, int tam) {
    bool hubo_cambio;

    do {
        hubo_cambio = false;

        for (int* p = arr; p < arr + tam - 1; ++p) {
            if (*p > *(p + 1)) {
                // Intercambio
                int temp = *p;
                *p = *(p + 1);
                *(p + 1) = temp;

                hubo_cambio = true;

                // Imprimir después del cambio
                imprimir(arr, tam);
            }
        }

    } while (hubo_cambio);
}

int main() {
    int lista[] = {5, 2, 8, 1, 9, 4, 7, 3, 6};
    int tam = sizeof(lista) / sizeof(lista[0]);

    ordenar_lista(lista, tam);

    std::cout << "Lista ordenada: ";
    imprimir(lista, tam);

    return 0;
}
