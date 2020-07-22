#include <stdio.h>
int main()
{
FILE *ficheiro;
ficheiro = fopen("file.txt","a"); // faz apend ou cria um novo ficheiro caso ainda nao exista um

char* texto = "A escrita em ficheiros é bastante simples \n";
fprintf(ficheiro,"%s", texto);
printf("Foi escrito: %s", texto);

fclose(ficheiro);
}
