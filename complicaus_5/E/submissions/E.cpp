#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    unordered_map<string, int> d;
    for (int i = 0; i < n; i++) {
        string t;
        cin >> t;
        d[t]++;
    }

    for (auto &[k, v] : d) {
    if (v > n - v) {
        cout << k << endl;
        return 0;
    }
    }
    cout << "NONE\n";
    return 0;
}
