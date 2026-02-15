#include <cmath>
#include <iomanip>
#include <iostream>
#include <queue>
using namespace std;

string b[710];
double g[1410][1410];

const double s = acos(-1) / 2;

int main() {
	iostream::sync_with_stdio(false);
	cin.tie(nullptr);

	int h, w;
	cin >> h >> w;
	for(int r = 0; r < h; ++r) cin >> b[r];
	for(int r = 0; r <= 2 * h; ++r)
		for(int c = 0; c <= 2 * w; ++c) g[r][c] = -1e9;

	priority_queue<pair<double, pair<int, int>>> pq;
	pq.push({-1, {0, 1}});
	pq.push({-1, {1, 0}});

	while(!pq.empty()) {
		auto [d, p] = pq.top();
		auto [r, c] = p;
		pq.pop();
		if(d < g[r][c]) continue;
		if(r + c == 2 * h + 2 * w - 1) {
			cout << setprecision(10) << 5 * (-d + 1) << endl;
			return 0;
		}
		if(r + 1 <= 2 * h && c + 1 <= 2 * w) {
			auto e = d - (b[r / 2][c / 2] == 'O' ? s : 2);
			if(g[r + 1][c + 1] < e) {
				g[r + 1][c + 1] = e;
				pq.push({e, {r + 1, c + 1}});
			}
		}
		if(r % 2 == 1) {
			if(r + 2 <= 2 * h) {
				if(g[r + 2][c] < d - 2) {
					g[r + 2][c] = d - 2;
					pq.push({d - 2, {r + 2, c}});
				}
			}
		} else {
			if(c + 2 <= 2 * w) {
				if(g[r][c + 2] < d - 2) {
					g[r][c + 2] = d - 2;
					pq.push({d - 2, {r, c + 2}});
				}
			}
		}
	}
}
