#include <pthread.h>
#include <stdio.h>

/* Prints x’s to stderr. The parameter is unused. Does not return. */
void* print_xs (void* unused)
{
    int i = 0;
  while (i<10) {
    fputc ('x', stderr);
    i++;
  }
  return NULL;
}

/* The main program. */
int main ()
{
  pthread_t thread_id;
  /* Create a new thread. The new thread will run the print_xs() function. */
  pthread_create (&thread_id, NULL, &print_xs, NULL);
  int i =0;
  /* Print o’s continuously to stderr. */
  while (i<50) {
    fputc ('o', stderr);
    i++;
  }
  (void) pthread_join(thread_id, NULL);

  return 0;
}