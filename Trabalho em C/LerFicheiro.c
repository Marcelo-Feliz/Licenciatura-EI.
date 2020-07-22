#include <stdio.h>
#include <stdlib.h>
main()
{
        FILE* ficheiro;
        char* linha = NULL;
        size_t len = 0;
        ssize_t read;

        ficheiro = fopen("texto.txt", "r");
        if (ficheiro == NULL) {
          printf("\nFicheiro não encontrado!");
        }
        else{
                  while ((read = getline(&linha, &len, ficheiro)) != -1) {
                    printf("Linha lida: %s", linha);
                  }
        }

        fclose(ficheiro);
}
