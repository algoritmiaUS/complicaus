#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair
#define eb emplace_back
#define all(a) begin(a), end(a)
#define has(a, b) (a.find(b) != a.end())
#define fora(i, n) for(int i = 0; i < n; i++)
#define forb(i, n) for(int i = 1; i <= n; i++)
#define forc(a, b) for(const auto &a : b)
#define ford(i, n) for(int i = n; i >= 0; i--)
#define maxval(t) numeric_limits<t>::max()
#define minval(t) numeric_limits<t>::min()
#define imin(a, b) a = min(a, b)
#define imax(a, b) a = max(a, b)
#define sz(x) (int)(x).size()
#define pvec(v) copy(all(v), ostream_iterator<decltype(v)::value_type>(cout, " "))

#define dbgs(x) #x << " = " << x
#define dbgs2(x, y) dbgs(x) << ", " << dbgs(y)
#define dbgs3(x, y, z) dbgs2(x, y) << ", " << dbgs(z)
#define dbgs4(w, x, y, z) dbgs3(w, x, y) << ", " << dbgs(z)

using ll = long long;
using ld = long double;

double dist[1500][1500];

constexpr double inf = 2000;
constexpr double p = acos(0)/2;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int w, h;
	cin >> h >> w;
	vector<string> f(h);
	fora(i, h) cin >> f[i];

	fora(i, 2 * h + 1) fora(j, 2 * w + 1) {
		dist[i][j] = i == 0 && j == 0 ? 0 : inf;
		if (i % 2 == 0 && j % 2 == 0) {
			if (i > 0) {
				imin(dist[i][j], dist[i - 1][j] + 0.5);
			}
			if (j > 0) {
				imin(dist[i][j], dist[i][j - 1] + 0.5);
			}
		} else if (i % 2 == 0) {
			imin(dist[i][j], dist[i][j - 1] + 0.5);
			if (i > 0 && f[i / 2 - 1][j / 2] == 'O') {
				imin(dist[i][j], dist[i - 1][j - 1] + p);
			}
		} else if (j % 2 == 0) {
			imin(dist[i][j], dist[i - 1][j] + 0.5);
			if (j > 0 && f[i / 2][j / 2 - 1] == 'O') {
				imin(dist[i][j], dist[i - 1][j - 1] + p);
			}
		}
	}

	cout << setprecision(10) << 10*dist[2 * h][2 * w] << endl;
}

