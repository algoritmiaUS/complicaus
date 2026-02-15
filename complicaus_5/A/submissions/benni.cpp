#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(auto i = (a); i < (b); i++)
#define pb push_back
#define fs first
#define sc second
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;

double pi = acos(-1);
const double EPS = 1e-9;

double FC(double diam) {
    return (pi * diam) / 4;
}

vector<vector<char>> G;
int n,m;

bool C(int i, int j) {
    return (0 <= i && i < n*2+1 && 0 <= j && j < m * 2 + 1);
}
typedef pair<double,ii> dii;

int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,-1,1};

int Kx[4] = {1,1,-1,-1};

double djikstra() {
    double mx = 1'000'0000;
    vector<vector<double>> Dist(n*2+1, vector<double>(m*2+1, mx));
    vector<vector<int>> D(n*2+1, vector<int>(m*2+1, 0));
    Dist[0][0] = 0;
    priority_queue<dii, vector<dii>, greater<dii>> pq;
    pq.push(dii(0, ii(0,0)));
    while(!pq.empty()) {
        dii ok = pq.top();
        pq.pop();
        if(D[ok.sc.fs][ok.sc.sc]) continue;
        D[ok.sc.fs][ok.sc.sc] = 1;

        if(ok.sc.fs % 2 == 0 && ok.sc.sc % 2 == 0) {
            for(int i = 0; i < 4; i++) {
                ii nx = ii(ok.sc.fs + dx[i], ok.sc.sc + dy[i]);
                if(0 <= nx.fs && nx.fs < 2*n+1 && 0 <= nx.sc && nx.sc < 2*m+1) {
                    Dist[nx.fs][nx.sc] = min(Dist[nx.fs][nx.sc], ok.fs + 5);
                    pq.push(dii(Dist[nx.fs][nx.sc], nx));
                }
            }
        } else {
            if(ok.sc.fs% 2 == 1) {
                vector<dii> DL;
                for(int i = 0; i < 4; i++) {
                    if(dy[i] == 0) DL.pb(dii(5, ii(dx[i], dy[i])));
                }

                if(ok.sc.sc != 0) {
                    if(G[ok.sc.fs / 2][ok.sc.sc / 2 - 1] == 'O') {
                        DL.pb(dii(FC(10.0), ii(+1, -1)));
                        DL.pb(dii(FC(10.0), ii(-1, -1)));
                    }
                }
                if(ok.sc.sc != m*2) {
                    if(G[ok.sc.fs / 2][ok.sc.sc / 2] == 'O') {
                        DL.pb(dii(FC(10.0), ii(+1, +1)));
                        DL.pb(dii(FC(10.0), ii(-1, +1)));
                    }
                }

                for(int i = 0; i < DL.size(); i++) {
                    ii nx = ii(ok.sc.fs + DL[i].sc.fs, ok.sc.sc + DL[i].sc.sc);
                    if(0 <= nx.fs && nx.fs < 2*n+1 && 0 <= nx.sc && nx.sc < 2*m+1) {
                        Dist[nx.fs][nx.sc] = min(Dist[nx.fs][nx.sc], ok.fs + DL[i].fs);
                        pq.push(dii(Dist[nx.fs][nx.sc], nx));
                    }
                }
            } else {
                vector<dii> DL;
                for(int i = 0; i < 4; i++) {
                    if(dx[i] == 0) DL.pb(dii(5, ii(dx[i], dy[i])));
                }

                if(ok.sc.fs != 0) {
                    if(G[ok.sc.fs / 2 - 1][ok.sc.sc / 2] == 'O') {
                        DL.pb(dii(FC(10.0), ii(-1, +1)));
                        DL.pb(dii(FC(10.0), ii(-1, -1)));
                    }
                }
                if(ok.sc.fs != n*2) {
                    if(G[ok.sc.fs / 2][ok.sc.sc / 2] == 'O') {
                        DL.pb(dii(FC(10.0), ii(+1, -1)));
                        DL.pb(dii(FC(10.0), ii(+1, +1)));
                    }
                }
                for(int i = 0; i < DL.size(); i++) {
                    ii nx = ii(ok.sc.fs + DL[i].sc.fs, ok.sc.sc + DL[i].sc.sc);
                    if(0 <= nx.fs && nx.fs < 2*n+1 && 0 <= nx.sc && nx.sc < 2*m+1) {
                        Dist[nx.fs][nx.sc] = min(Dist[nx.fs][nx.sc], ok.fs + DL[i].fs);
                        pq.push(dii(Dist[nx.fs][nx.sc], nx));
                    }
                }
            }
        }
    }

    return Dist[n*2][m*2];

}

int main() {
    cin.sync_with_stdio(false);
    cin >> n >> m;
    G = vector<vector<char>>(n, vector<char>(m, '.'));
    rep(i,0,n) {
        rep(j,0,m) cin >> G[i][j];
    }
    cout << setprecision(10) << fixed << djikstra() << endl;
}

