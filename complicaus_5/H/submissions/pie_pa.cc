/* Sample solution for NWERC'06: Pie
 * Author: Per Austrin
 * Algorithm: Binary search
 */
#include <cstdio>
int main(void) {
  double A[12345],l,h,m; int T,n,f,p,i;
  for (scanf("%d", &T); scanf("%d%d", &n, &f), T--; printf("%.6lf\n", l))
    for (++f, l = p = i = 0, m = h = 9e9; h-l > 1e-7; ++i, (p<f?h:l) = m) 
      if (i < n) scanf("%lf",A+i), A[i] *= A[i]*3.1415926535897932384626;
      else for (m = (l+h)/2, p = i = 0; i < n; ++i) p += (int)(A[i] / m);
  return 0;
}
