#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int m, n;
	cin >> m >> n;
	vector<string> a(m);
	for (string &s: a) cin >> s;

	vector<vector<double>> dp(2*m+1, vector<double>(2*n+1, 1e10));
	double arc = acos(0);
	dp[0][0] = 0;
	for (int i = 0; i <= 2*m; i++) {
		for (int j = 0; j <= 2*n; j++) {
			if (i > 0 && j%2 == 0) {
				dp[i][j] = min(dp[i][j], dp[i-1][j] + 1);
				if (i%2 == 1 && j > 0 && a[i/2][j/2-1] == 'O')
					dp[i][j] = min(dp[i][j], dp[i-1][j-1] + arc);
			}
			if (j > 0 && i%2 == 0) {
				dp[i][j] = min(dp[i][j], dp[i][j-1] + 1);
				if (j%2 == 1 && i > 0 && a[i/2-1][j/2] == 'O')
					dp[i][j] = min(dp[i][j], dp[i-1][j-1] + arc);
			}
		}
	}
	cout << fixed << setprecision(20) << 10*dp[2*m][2*n]/2 << '\n';
}
