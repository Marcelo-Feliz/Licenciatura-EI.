#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define QUEUE_SIZE 20
#define MEM_SIZE 300
#define STRING_SIZE 20
#define ARRAY_SIZE 20
#define INSTANT_MAX 6
#define AUXILIAR_SIZE 100

int disco;

char gestor_mem[] = "Best Fit";

struct PCB
{
    int id; 
    int arrival; //tempo
    int pc;    //program counter
    int mem_start;  
    int mem_end;
    char estado_atual[STRING_SIZE];  
    int tempo_estado; // tempo em cada estado

   
};


struct Dados
{
    int arrival;
    int array[AUXILIAR_SIZE];
};


struct Queue
{   
    int head;
    int tail;
    int size;
    struct PCB *array[QUEUE_SIZE];
};


struct Queue *new_Queue()
{
    struct Queue *queue = malloc(sizeof(struct Queue));

    queue->head = 0;
    queue->tail = 0;
    queue->size = 0;

    return queue;
}


void enqueue(struct Queue* queue, struct PCB* process)
{

    if (queue->size == QUEUE_SIZE)
    {
        return;
    }

    queue->array[queue->tail] = process;
    queue->tail = queue->tail + 1;
    if (queue->tail == QUEUE_SIZE) 
    {
        queue->tail = 0;
    }
    
    queue->size = queue->size + 1;

}

struct PCB* dequeue(struct Queue* queue)
{

    queue->head = queue->head + 1;
    if (queue->head == QUEUE_SIZE) 
    {
        queue->head = 0;
    }
    queue->size = queue->size - 1;

    return queue->array[queue->head - 1];
}

struct PCB* front(struct Queue* queue)
{
    if (queue->size == 0 ) 
    {
        return NULL;
    }
    
    return queue->array[queue->head];
}



struct Dados *new_Dados(char* linha)
{
    struct Dados *dados = malloc(sizeof(struct Dados)); // aloca espaco na memoria


    for (int i = 0; i < AUXILIAR_SIZE; i++)
    {
        dados->array[i] = -1;
    }
    

    char* token = strtok(linha, " ");
    dados->arrival = atoi(token);

    int val;
    token = strtok(NULL, " ");
    int pos = 0;
    
    while (token != NULL) 
    { 
        val = atoi(token);
        dados->array[pos] = val;
        token = strtok(NULL, " ");
        pos++;
    }    

    return dados;

}


struct PCB *new_PCB(int mem[MEM_SIZE], struct Dados* auxiliar[ARRAY_SIZE], int id, int j, int bitmap[MEM_SIZE], int next_fit_count)
{
    struct PCB *processo = malloc(sizeof(struct PCB)); // aloca espaco na memoria

    processo->id = id;
    processo->arrival = auxiliar[j]->arrival;

    
    int count = 0;
    int index = 0;
    int espaco_total;

    while (auxiliar[j]->array[index] != -1)
    {
        count++;
        index++;
    }

    espaco_total = 10 + count;


    int size;
    int end;

    int size_b[ARRAY_SIZE];
    int end_b[ARRAY_SIZE];
    


    /*
    if (strcmp(gestor_mem, "Next Fit") ==0)
    {
       end = 0;
       size = 0;

        for (int i = next_fit_count; i <= MEM_SIZE; i++)
        {           
            if(bitmap[i] == 0)
            {
                size++;
                if (size == espaco_total)
                {   
                    end = i;
                    break;         
                }
            }    
            if (i == MEM_SIZE)
            {
                for (int i = next_fit_count; i <= MEM_SIZE; i++)
                {
                    if(bitmap[i] == 0)
                    {
                        size++;
                        if (size == espaco_total)
                        {   
                            end = i;
                            break;         
                        }
                    }
                }       
            }
            else
            {
                count = 0;
            }
            
        }

    }   
    
    */

   //&&&&&&&&&&&&&&&&&&&&&&&&&& erro no best fit &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    int counter = 0;

    if (strcmp(gestor_mem, "Best Fit") ==0)
    {   
        size = 0;
        

        for (int i = 0; i < ARRAY_SIZE; i++)
        {
            end_b[i] = 0;
            size_b[i] = 0;
        }

     

        for (int i = 0; i <= MEM_SIZE; i++)
        {           
            if(bitmap[i] == 0)
            {
                size++;
            
            }
            if(bitmap[i] == 1 || i == MEM_SIZE)
            {   
                if (size >= espaco_total)
                {
                    size_b[counter] = size;
                    end_b[counter] = i - 1; 
                    printf("%d\n", size);
                    counter++;

                }
            
                size = 0;
                

                printf("%d\n", size);
            }
        }

        for (int i = 0; i < ARRAY_SIZE; i++)
        {
            printf("%d", size_b[i]);
            printf(" %d\n", end_b[i]);
        }
        


        size = 300;
        int j = 0;  

        for (int i = 0; i < ARRAY_SIZE; i++)
        {
            if (size_b[i] > 0 )
            {   
                
                if (size_b[i] < size)
                {
                    printf("oof\n");
                    size = size_b[i];
                    printf("i=%d\n", i);
                    j = i;
                    printf("j=%d\n", j);
                }

            }
            else
            {
                break;
            }
        }

        printf("hey%d\n", j);
        
        end = end_b[j];

          printf("hey\n");
    }   

   




    processo->mem_start = end - size + 1;

    printf("end %d\n", end);


    printf("size %d\n", size);
   
    printf("hey\n");
    for (int i = processo->mem_start; i < processo->mem_start + size; i++)
    {
        bitmap[i] = 1;
    
        
    }

     printf("hey\n");
     
    int c = 0;

     for (int i = processo->mem_start ; i < processo->mem_start + 10; i++)
    { 
        mem[i] = 0;
            
    }
    
    for (int i = processo->mem_start + 10 ; i < processo->mem_start + size; i++)
    { 
        mem[i] = auxiliar[j]->array[c];
        c++; 
    
        
    }


    processo->pc = processo->mem_start + 10;
    processo->mem_end = end;


    strcpy(processo->estado_atual, " ");
    processo->tempo_estado = 0;

    return processo;

}

void controlo_chegada_block(struct Queue* BLOCK, int mem[MEM_SIZE])
{   

    if(front(BLOCK) != NULL)
    {   
    
        front(BLOCK)->tempo_estado = front(BLOCK)->tempo_estado  + 1;

        int inst = mem[front(BLOCK)-> pc - 3];
        int v1 = mem[front(BLOCK)-> pc - 2];
        int valor = mem[v1 - 1];

        if (front(BLOCK)->tempo_estado == 3 && inst == 8)
        {   
            disco = valor;

        }

         if (front(BLOCK)->tempo_estado == 3 && inst == 9)
        {   
            mem[v1 -1] = disco;
        
        }
    }

}

void controlo_chegada_exit(struct Queue* EXIT, int mem[MEM_SIZE],int bitmap[MEM_SIZE])
{

    if(front(EXIT) != NULL && front(EXIT)->tempo_estado == 1)
    {   
        int start = front(EXIT)->mem_start; 
        int end =   front(EXIT)->mem_end;
        
        for (int i = start; i <= end; i++)
        {   
            mem[i] = -1;
        
        }

        for (int i = start; i < end; i++)
        {
            bitmap[i] = 0;
        }
        

        strcpy(front(EXIT)->estado_atual, " ");
        dequeue(EXIT);



    }

    if(front(EXIT) != NULL)
    {   
        
        front(EXIT)->tempo_estado = front(EXIT)->tempo_estado  + 1;
    }



    
}


void controlo_chegada_new(struct PCB* processos[ARRAY_SIZE], int instante, struct Queue* NEW, int n_processos)
{   
    

    for(int i = 0; i < n_processos; i++)
    {   
        if (processos[i]->arrival == instante) 
        {   
            enqueue(NEW, processos[i]);
            strcpy(processos[i]->estado_atual, "NEW");
            processos[i]->tempo_estado =  processos[i]->tempo_estado + 1;

        }
    }


}

void controlo_instrucao(int mem [MEM_SIZE], struct Queue* RUN, struct Queue* BLOCK, struct Queue* EXIT,struct PCB* processos[ARRAY_SIZE], int n_processos)
{   
    int jump = 0;
    if (front(RUN) != NULL )
    {
        front(RUN)->tempo_estado = front(RUN)->tempo_estado + 1;

        //instruçao 0
        if (mem[front(RUN)->pc] == 0)
        {   
            int v1 = mem[front(RUN)->pc + 1];
            int v2 = mem[front(RUN)->pc + 2];
            int pos = front(RUN)->mem_start + v1 - 1;
            int pos2 = front(RUN)->mem_start +  v2 - 1;
            
            
            if(v1 == 1)
            {   
                mem[pos] = mem[pos2];
            
            }
            else if ( v2 == 1)
            {
                mem[pos] = mem[pos2];
            }
            else
            {   
                mem[pos] = mem[pos2];     
            }            
        }

        //instruçao 1
        if (mem[front(RUN)->pc] == 1)
        {
            int v1 = mem[front(RUN)->pc + 1];
            int valor = mem[front(RUN)->pc + 2];
            int pos = front(RUN)->mem_start;
            int pos2 = pos + v1 - 1;
           
    
            if(v1 == 1)
            {
                mem[pos] = valor;
                
            }
            else
            {   
                mem[pos2]= valor;
                
            }
        }

        //instruçao 2
        if (mem[front(RUN)->pc] == 2)
        {
            int v1 = mem[front(RUN)->pc + 1];
            int pos = front(RUN)->mem_start + v1 - 1;
        
            if(v1 == 1)
            {   
                mem[pos] = mem[pos] + 1;
                
            }
            else
            {  
                mem[pos] = mem[pos] + 1; 
            
            }
        }

        //instruçao 3
        if (mem[front(RUN)->pc] == 3)
        {
             int v1 = mem[front(RUN)->pc + 1];
            int pos = front(RUN)->mem_start + v1 - 1;
        
            if(v1 == 1)
            {   
                mem[pos] = mem[pos] - 1;
          
                
            }
            else
            {  
                mem[pos] = mem[pos] - 1; 
             ;
                
            }
        }

        //instruçao 4
        if (mem[front(RUN)->pc] == 4)
        {
            jump = 1;
            int n =  mem[front(RUN)->pc + 1];
    
            front(RUN)->pc = front(RUN)->pc - (n * 3);
          
        }
        
        //instruçao 5
        if (mem[front(RUN)->pc] == 5)
        {   
            jump = 1;
            int n =  mem[front(RUN)->pc + 1];
            
            front(RUN)->pc = front(RUN)->pc + (n * 3);
            
        }

        //instruçao 6
        if (mem[front(RUN)->pc] == 6)
        {   
            if (jump == 0)
            {
                int v1 =  mem[front(RUN)->pc + 1];
                int n =  mem[front(RUN)->pc + 2];
                int pos = front(RUN)->mem_start + v1 - 1;
            
                if (mem[pos] == 0)
                {
                    front(RUN)->pc = front(RUN)->pc + (n * 3);
                    jump = 1;  
                }
            
            }
            
            
        }

        //instruçao 7
        if (mem[front(RUN)->pc] == 7)
        {
            if (jump == 0)
            {
                /* code */
            }
            

        }

        //instruçao 8
        if (mem[front(RUN)->pc] == 8)
        {   
            if (jump == 0)
            {
                front(RUN)->pc = front(RUN)->pc + 3;
                front(RUN)->tempo_estado = -1;
                strcpy(front(RUN)->estado_atual, "BLOCK");
                enqueue(BLOCK, dequeue(RUN));
            
            }            
        }

        //instruçao 9    
        if (front(RUN) != NULL )
        {   
            if (jump == 0)
            {
                if (mem[front(RUN)->pc] == 9)
                {
                    front(RUN)->pc = front(RUN)->pc + 3;
                    front(RUN)->tempo_estado = -1;
                    strcpy(front(RUN)->estado_atual, "BLOCK");
                    enqueue(BLOCK, dequeue(RUN));        
                }
            }
        
            
        }

        //instruçao 10
        if (front(RUN) != NULL )
        {   
            if (jump == 0)
            {
                if (mem[front(RUN)->pc] == 10)
                {
                    int v1 = mem[front(RUN)->pc + 1];
                    int pos = front(RUN)->mem_start + v1 - 1;
               
                
                    printf("%d ",mem[pos]);
                }
            }        
        }
        
        //instruçao 11
        if (front(RUN) != NULL )
        {   
            if (jump == 0)
            {
                if (mem[front(RUN)->pc] == 11)
                {  
                    strcpy(front(RUN)->estado_atual, "EXIT");
                    enqueue(EXIT, dequeue(RUN));
                    front(EXIT)->tempo_estado = 0;
                }

                
            }
            
           
        }

    
        if (front(RUN) != NULL) 
        {
            if(jump == 0)
            {   
                front(RUN)->pc = front(RUN)->pc + 3;
                     
            }
            else
            {
                jump = 0; 
            }
              
        }
        
    }

}


void print(int instante ,struct PCB* processos[ARRAY_SIZE],int n_processos)
{
    printf("%3d|", instante);

    for(int j = 0; j < n_processos; j++)
    {
        printf("%5s |",processos[j]->estado_atual);
        
    }
}


void controlo_estado(struct Dados* auxiliar[ARRAY_SIZE], int n_dados)
{ 
  
    struct Queue* NEW = new_Queue();
    struct Queue* READY = new_Queue();
    struct Queue* RUN = new_Queue();
    struct Queue* BLOCK = new_Queue();
    struct Queue* EXIT = new_Queue();

    int id = 1;
    int n_processos = 0;
    struct PCB* processos[ARRAY_SIZE];
    int bitmap[MEM_SIZE];
    int mem[MEM_SIZE];
    int next_fit_count = 0;

    for (int i = 0; i < MEM_SIZE; i++)
    {   
        bitmap[i] = 0; 
     
    }    

    for(int i = 0; i < MEM_SIZE; i++)
    {
        mem[i] = -1;
    }

   
    for(int i = 0; i < INSTANT_MAX; i++) 
    {   

        for (int j = 0; j < n_dados; j++)
        {   
            if(auxiliar[j]->arrival ==  i)
            {   
                
                struct PCB* processo = new_PCB(mem,auxiliar,id, j,bitmap, next_fit_count);
                next_fit_count = processo->mem_end;
                processos[n_processos] = processo;
                n_processos++;
                id++;
            

            }
         
        }
        
        if (front(BLOCK) != NULL && front(BLOCK)->tempo_estado == 3)  // Verificar se algum processo passa do block para o ready
        {   
            strcpy(front(BLOCK)->estado_atual, "READY");
            front(BLOCK)->tempo_estado = 0;
            enqueue(READY, dequeue(BLOCK));
            
              
        }       

        if(front(RUN) != NULL && front(RUN)->tempo_estado == 4) // Verificar se algum processo passa do run para o ready
        {   
            strcpy(front(RUN)->estado_atual, "READY");
            front(RUN)->tempo_estado = 0;
            enqueue(READY, dequeue(RUN));
            
              
        }

        
        if(front(NEW) != NULL && front(NEW)->tempo_estado == 1) // Verificar se algum processo passa do new para o ready
        {   
            strcpy(front(NEW)->estado_atual, "READY");
            front(NEW)->tempo_estado = 0; 
            enqueue(READY, dequeue(NEW));
        
        }
        
        
        if(RUN->size == 0 && READY->size >= 1) // Verificar se algum processo passa do ready para o run
        {   
            strcpy(front(READY)->estado_atual, "RUN");
            enqueue(RUN, dequeue(READY));
           
        }
            
        controlo_chegada_new(processos, i, NEW, n_processos); //instante no NEW

        //print(i,processos, n_processos);

        controlo_instrucao(mem, RUN, BLOCK, EXIT, processos, n_processos);  //instante no CPU

        controlo_chegada_block(BLOCK, mem);  //instante no BLOCK

        for (int i = 0; i < 150; i++)
        {
            //printf("%d",mem[i]);
            //printf(" %d\n",bitmap[i]);
        }
        
 


        controlo_chegada_exit(EXIT, mem,bitmap); // instante no EXIT

        printf("\n");

            
    }
    
}


int main()
{

    FILE *file;
    char* linha;
    size_t len = 0;
    size_t read;
    struct Dados* auxiliar[ARRAY_SIZE];
    int n_dados = 0;

    
    file = fopen("input1.txt", "r");

    if (file == NULL) 
    {
        printf("Ficheiro nao encontrado \n");
    }
    else
    {
        while ((read = getline(&linha, &len,file)) != EOF)
        {
    
            struct Dados* dados = new_Dados(linha);
            auxiliar[n_dados] = dados;
            n_dados ++;
        }
    }

    controlo_estado(auxiliar,n_dados);

    fclose (file); 
  

    return 0;
}




