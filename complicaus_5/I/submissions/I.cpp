#include <bits/stdc++.h>
using namespace std;

string dutch(string s) {
    for (int i = 0; i < int(s.size()); i++) {
        if ('A' <= s[i] && s[i] <= 'Z') {
            return s.substr(i);
        }
    }
    assert(false);
    return "";
}

int main() {
    int n;
    cin >> n;
    cin.ignore();
    vector<string> s(n);
    for (int i = 0; i < n; i++) {
        getline(cin, s[i]);
    }
    sort(s.begin(), s.end(), [&](string x, string y) {
        return dutch(x) < dutch(y);
    });
    for (string t : s) {
        cout << t << '\n';
    }
    return 0;
}
