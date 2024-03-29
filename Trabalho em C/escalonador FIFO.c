/* Simulador de Escalonamento de Processos*/
#include <stdio.h>
#include <stdlib.h>
/* Estrutura */
struct processos {
    int id;                   /* Identifição do processo*/              
 int surto;                /* Tempo de duração do processo*/
    int prioridade;           
    int execucao;             /* Tempo de execução do processo*/
    int espera;               /* Tempo de espera do processo*/
    struct processos *prox;
};
/* Declarações de Protótipo de função */
struct processos *init_processos (int id, int surto, int prioridade);
void fcfs (struct processos *proc);
void listprocs (struct processos *proc);
void prioridade (struct processos *proc);
void rr (struct processos *proc, int quantum);
void sjf (struct processos *proc);
 
int main (void) {
    
    struct processos *plist, *ptmp;
    plist       = init_processos(1, 10, 3);
    plist->prox = init_processos(2,  1, 1); ptmp = plist->prox;
    ptmp->prox  = init_processos(3,  2, 3); ptmp = ptmp->prox;
    ptmp->prox  = init_processos(4,  1, 4); ptmp = ptmp->prox;
    ptmp->prox  = init_processos(5,  5, 2);
    /* Simulações executadas*/
    listprocs(plist);
    fcfs(plist);
    sjf(plist);     
    prioridade(plist);
    rr(plist,0);
    
    while (plist != NULL) {
        ptmp = plist;
        plist = plist->prox;
        free(ptmp);
    };
    return(0);
};
/* Inicialização de entrada da lista de processos*/
struct processos *init_processos (int id, int surto, int prioridade) {
    struct processos *proc;
 proc = (struct processos*)malloc(sizeof(struct processos)); 
  if (proc == NULL) {
        printf("Erro Fatal: Falha Alocacao de memoria.\nFinalizar.\n");
        exit(1);
    };
    proc->id = id;
    proc->surto = surto;
    proc->prioridade = prioridade;
    proc->execucao = 0;
    proc->espera = 0;
    proc->prox = NULL;
    return(proc);
};

/* Escalonamento FCFS - o primeiro que chega 
/* é o primeiro a sair, ou seja, será executado primeiro */
void fcfs (struct processos *proc) {
    int tempo = 0, inicio, fim;
  struct processos *tmp = proc;
  printf("\tEscalonamento FCFS\n");
    printf("\n");
  while (tmp != NULL) {
    inicio = tempo;
    tempo += tmp->surto;
    fim = tempo;
    printf("Processo: %d\tSurto: %d\tEspera: %d\tRetorno: %d\n", tmp->id, tempo, inicio, fim);
    tmp = tmp->prox;
  };
    printf("\n\n");
};

/* Listando Processos */
void listprocs (struct processos *proc) {
  struct processos *tmp = proc;
  printf("\tListagem de Processos\n");
  printf("\n");
  while (tmp != NULL) {
    printf("Processo: %d\tPrioridade: %d\tSurto: %d\n", tmp->id, tmp->prioridade, tmp->surto);
    tmp = tmp->prox;
  };
  printf("\n\n");
 };
/* Simulação de Processos por Prioridade
 * Obs: O processo de menor valor de prioridade obtem
 * prioridade maior na fila de processos */
void prioridade (struct processos *proc) {
  int tempo, inicio, fim, maior;
  struct processos *copia, *tmpsrc, *tmp, *maiorprimeiro;
  printf("\tEscalonamento por Prioridade\n");
   printf("\n");
  
     /* Replicando Lista de Processos */
  tmpsrc = proc;
  copia = tmp = NULL;
  while (tmpsrc != NULL) {
    if (copia == NULL) {
    copia = init_processos(tmpsrc->id, tmpsrc->surto, tmpsrc->prioridade);
    tmp = copia;
    } else {
    tmp->prox = init_processos(tmpsrc->id, tmpsrc->surto, tmpsrc->prioridade);
    tmp = tmp->prox;
    };
    tmpsrc = tmpsrc->prox;
  };
  /* Programa Principal */
  tempo = 0;
  while (copia != NULL) {
    
          /* Localiza o proximo processo */
    maiorprimeiro = NULL;
    maior = copia->prioridade;
    tmp = copia->prox;
    tmpsrc = copia;
    while (tmp != NULL) {
    if (tmp->prioridade < maior) {
      maior = tmp->prioridade;
      maiorprimeiro = tmpsrc;
    };
    tmpsrc = tmp;
    tmp = tmp->prox;
    };
     if (maiorprimeiro == NULL) {
    /* Verifica se o primeiro processo possui maior prioridade */
    inicio = tempo;
    tempo += copia->surto;
    fim = tempo;
    printf("Processo: %d\tSurto: %d\tEspera: %d\tRetorno: %d\n", copia->id, tempo, inicio, fim);
    tmpsrc = copia->prox;
    free(copia);
    copia = tmpsrc;
    } else {
    /* Verifica se o primeiro processo não possui maior prioridade */
    tmp = maiorprimeiro->prox;
    inicio = tempo;
    tempo += tmp->surto;
    fim = tempo;
    printf("Processo: %d\tSurto: %d\tEspera: %d\tRetorno: %d\n", tmp->id, tempo, inicio, fim);
    maiorprimeiro->prox = tmp->prox;
    free(tmp);
    };
  };
  printf("\n\n");
};
