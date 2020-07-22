

#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(void)
{
    pid_t pid;
    int numero;
    int resultado = 0;

scanf("%d",&numero);

    pid = fork();
while(numero >1){
    pid = fork();
    if (pid == 0){
        resultado = (numero*(numero-1)) + resultado;
        printf("%d\n",resultado);
        numero=numero-1;
    }
    else
    printf("resultado2 %d\n",resultado);
}



return resultado;
}