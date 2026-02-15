#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

#define all(x) begin(x), end(x)
#define sz(x) (ll)(x).size()

using ll = long long;
using ld = long double;

constexpr ld pi4 = 0.7853981633974483096156608458198757210492923498437764552437361480;

void setmin(ld& a, ld b) {
	a = min(a, b);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	ld inf = 1.0/0.0;

	ll h, w;
	cin >> h >> w;
	vector<vector<ld>> res(2*h+7,vector<ld>(2*w+7, inf));
	res[0][1] = res[1][0] = 0;
	for (ll y = 0; y < h; y++) {
		for (ll x = 0; x < w; x++) {
			char c;
			cin >> c;
			if (c == 'X') {
				setmin(res[2*y+2][2*x+1], 1+res[2*y+1][2*x]);
				setmin(res[2*y+1][2*x+2], 1+res[2*y][2*x+1]);
			} else {
				setmin(res[2*y+2][2*x+1], pi4+res[2*y+1][2*x]);
				setmin(res[2*y+1][2*x+2], pi4+res[2*y][2*x+1]);

			}
			setmin(res[2*y+3][2*x], 1+res[2*y+1][2*x]);
			setmin(res[2*y][2*x+3], 1+res[2*y][2*x+1]);
		}
		setmin(res[2*y+3][2*w], 1+res[2*y+1][2*w]);
	}
	for (ll x = 0; x <= w; x++) {
		setmin(res[2*h][2*x+3], 1+res[2*h][2*x+1]);
	}

	cout << fixed << setprecision(10) << 10*(1+min(res[2*h][2*w-1], res[2*h-1][2*w])) << endl;
}
