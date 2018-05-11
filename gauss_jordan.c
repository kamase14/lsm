#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 3
#define EPS 0.001

int main(void)
{
  double a[N][N+1] = {
    {2,1,3,13},
    {1,3,2,13},
    {3,2,1,10}
  };
  double pivot, del;
  int i, j, k, l;

  for (i=0; i<N; i++) {
    pivot = a[i][i];
    if (fabs(pivot) < EPS) {
      printf("ピボットが許容誤差以下\n");
      return 1;
    }
    
    for (j=i; j<N+1; j++) {
      a[i][j] = a[i][j]/pivot;
    }

    for (k=0; k<N; k++) {
      del = a[k][i];
      for (j=i; j<N+1; j++) {
	if (k != i) {
	  a[k][j] -= del*a[i][j];
	}
      }
    }

  }

  for (l=0; l<N; l++) {
    printf("X%d = %f\n", l, a[l][N]);
  }

  return 0;
}
