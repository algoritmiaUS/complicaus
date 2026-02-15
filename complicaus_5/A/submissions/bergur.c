#include <stdio.h>
#include <assert.h>
#include <math.h>
#define MAXN 1000
#define rep(E, F) for (E = 0; E < (F); E++)
#define per(E, F) for (E = (F) - 1; E >= 0; E--)
int get_int()
{
	int r = 0, c = getchar(), s = 1;
	while (c != '-' && c < '0' || c > '9') c = getchar();
	while (c == '-') s *= -1, c = getchar();
	while (c >= '0' && c <= '9') r = r*10 + c - '0', c = getchar();
	return s*r;
}

int get_string(char* b, char t)
{
	int i = 0;
	b[i++] = getchar();
	while (b[i - 1] != t) b[i++] = getchar();
	b[i - 1] = '\0';
	return i - 1;
}

int r, c;
char s[MAXN][MAXN + 1];
double d[2*MAXN][2*MAXN];
double foo(int x, int y)
{
	if (x == 2*r && y == 2*c) return 0.0;
	if (x%2 == 1 && y%2 == 1) return 1e9;
	if (x == 2*r || y == 2*c) return (2*r - x + 2*c - y)*5.0;
	if (d[x][y] > -0.5) return d[x][y]; 
	d[x][y] = fmin(foo(x + 1, y) + 5.0, foo(x, y + 1) + 5.0);
	if (x%2 == 1 && s[x/2][y/2] == 'O') d[x][y] = fmin(d[x][y], foo(x + 1, y + 1) + 5.0/2.0*M_PI);
	if (y%2 == 1 && s[x/2][y/2] == 'O') d[x][y] = fmin(d[x][y], foo(x + 1, y + 1) + 5.0/2.0*M_PI);
	return d[x][y];
}

int main()
{
	int i, j;
	r = get_int(), c = get_int();
	rep(i, r) get_string(s[i], 10);
	rep(i, 2*MAXN) rep(j, 2*MAXN) d[i][j] = -1.0;
	printf("%.8f\n", foo(0, 0));
	return 0;
}
