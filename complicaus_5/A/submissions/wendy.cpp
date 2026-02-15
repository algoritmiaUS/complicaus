#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#define f(i, s, k, l) for (int i = s; i < k; i += l)
#define for0(i, k) f(i, 0, k, 1)

#define pl pair<long long, long long>
#define pb push_back

#define vl vector<long long>
#define vi vector<int>
#define sz(x) (ll)(x).size()

using namespace std;
using ll = long long;
using ld = long double;

int main() {
    ll w, h;
    char sq;
    cin >> h >> w;

    vector<vector<ld>> square(2 * h + 1, vector<ld>(2 * w + 1, 0));
    for0(i, h) {
        for0(j, w) {
            cin >> sq;
            sq == 'X' ? square[2 * i + 1][2 * j + 1] = 1.0 : square[2 * i + 1][2 * j + 1] = M_PI / 4.0;
        }
    }

    vector<vector<ld>> dp(2 * h + 1, vector<ld>(2 * w + 1));

    for0(i, 2 * w + 1) dp[0][i] = i * 0.5;
    for0(i, 2 * h + 1) dp[i][0] = i * 0.5;

    for(ll i = 1; i <= 2 * h; i++) {
        for(ll j = 1; j <= 2 * w; j++) {
            if((i + j) % 2 == 0) continue;
            if(i == 1) dp[i][j] = dp[i - 1][j - 1] + square[i][j - 1];
            else if(j == 1) dp[i][j] = dp[i - 1][j - 1] + square[i - 1][j];
            else if(i % 2 == 1) dp[i][j] = min(dp[i - 2][j] + 1.0, dp[i - 1][j - 1] + square[i][j - 1]);
            else dp[i][j] = min(dp[i][j - 2] + 1.0, dp[i - 1][j - 1] + square[i - 1][j]);
        }
    }
    cout << fixed << setprecision(10) << 10*(min(dp[2 * h][2 * w - 1], dp[2 * h - 1][2 * w]) + 0.5) << endl;
}
