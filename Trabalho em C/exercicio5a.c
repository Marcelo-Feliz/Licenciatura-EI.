#include <stdio.h>

int main()  {
        //
        //

        int a = 33;
        int b = 55;
        int *ap=&a;

        //
        //


        printf("Valor a: %d\n", a);
        printf("Endereço a: %d\n", &a);
        printf("Valor apontador: %d\n", ap);
        printf("Endereço apontador: %d\n", &ap);
        printf("Valor na memória apontada pelo apontador: %d\n", *ap);
}
