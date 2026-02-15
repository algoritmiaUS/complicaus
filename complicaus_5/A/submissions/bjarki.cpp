#include <bits/stdc++.h>
using namespace std;

int TOP = 0,
    RIGHT = 1,
    BOTTOM = 2,
    LEFT = 3;

bool circ[710][710];
double mem[710][710][4];
bool comp[710][710][4];
int n, m;

double pi = acos(-1.0);
double clen = 10 * pi / 4.0;

double dp(int x, int y, int pos) {
	if (comp[x][y][pos]) {
		return mem[x][y][pos];
	}
	if (x == n-1 && y == m-1 && (pos == BOTTOM || pos == RIGHT)) {
		return 5;
	}
	double best = INFINITY;
	if (pos == TOP) {
		if (y+1 < m) best = min(best, 10 + dp(x,y+1,TOP));
		best = min(best, dp(x,y,RIGHT)+(circ[x][y] ? clen : 10));
	}
	if (pos == LEFT) {
		if (x+1 < n) best = min(best, 10 + dp(x+1,y,LEFT));
		best = min(best, dp(x,y,BOTTOM) + (circ[x][y] ? clen : 10));
	}
	if (pos == RIGHT) {
		if (x+1 < n) best = min(best, 10 + dp(x+1,y,RIGHT));
		if (y+1 < m) best = min(best, dp(x,y+1,BOTTOM) + (circ[x][y+1] ? clen : 10));
	}
	if (pos == BOTTOM) {
		if (x+1 < n) best = min(best, dp(x+1,y,RIGHT) + (circ[x+1][y] ? clen : 10));
		if (y+1 < m) best = min(best, 10 + dp(x,y+1,BOTTOM));
	}
	comp[x][y][pos] = true;
	return mem[x][y][pos] = best;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			char c;
			cin >> c;
			circ[i][j] = c == 'O';
		}
	}
	cout << setprecision(12) << 5 + min(dp(0,0,TOP), dp(0,0,LEFT)) << endl;
	return 0;
}
