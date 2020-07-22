#include <stdio.h>

void funcaoTeste(char* array) {
        printf("\n teste a fazer print de dentro da funcao: %s", array);
}


main()
{
  char* string;
  printf("\n insira o texto para a string\n");
  scanf("%[0-9a-zA-Z]s", string);
  printf("\n texto inserido: %s \n", string);

  printf("\n ########## \n");

  //chamada da funcao q recebe a string para testar
  funcaoTeste(string);
}
