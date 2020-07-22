#include <pthread.h>
#include <stdio.h>
#include <math.h>
#define N 2
int n = N/2;

void* print_xs (void* unused)
{
    double numero = 0;


    for (double i = 1; i<n; i++){
        numero = numero + sqrt(i);
    }

    pthread_exit(&numero);
}

void* print_xs1 (void* unused)
{
    double numero = 0;
    

    for (double i = n; i<=N; i++){
        numero = numero + sqrt(i);
    }

    pthread_exit(&numero);
}
/* The main program. */
int main ()
{
  void *resultado1;
  void *resultado2;

  pthread_t thread_id;
  pthread_t thread_id1;

  double numero;  
  double n;

  n=100;


  pthread_create (&thread_id, NULL, &print_xs, NULL);
  pthread_create (&thread_id1, NULL, &print_xs1, NULL);

   pthread_join(thread_id, resultado1);
   pthread_join(thread_id1, resultado2);

    printf("%lf\n",*(double*)resultado1 + *(double*)resultado2);

 
  return 0;
}