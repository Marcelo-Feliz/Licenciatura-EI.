#include <pthread.h>
#include <stdio.h>

/* Prints x’s to stderr. The parameter is unused. Does not return. */
void* print_xs (void* unused)
{
  int x = 0;
  while (x < 10) {
    printf ("x");
    x = x+ 1;
  }
  return NULL;
}

/* The main program. */
int main ()
{
  int o = 0;
  pthread_t thread_id;
  /* Create a new thread. The new thread will run the print_xs() function. */
  pthread_create (&thread_id, NULL, &print_xs, NULL);

  /* Print o’s continuously to stderr. */
  while (o < 50) {
    printf ("o");
    o = o + 1;
  }

  return 0;
}
