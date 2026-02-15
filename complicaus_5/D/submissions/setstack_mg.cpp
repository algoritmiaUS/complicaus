/* NWERC 2006
 * Sample solution to setstack
 * By Mikael Goldmann
 */
#include<vector>
#include<set>
#include<map>
#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

bool debug=false;

#define dout debug && cerr 

const int MAX=11000;

typedef set<int>::const_iterator setit;

vector< set<int> > sets;

map<set<int>, int> mp;
int stk[MAX];
int top=0;

int setID(const set<int> &s) 
{
  int id = mp[s];
  if (!id) {
    id = mp[s]=sets.size();    
    sets.push_back(s);
  }
  return id;
}

void intersect()
{
  int x=stk[--top], y=stk[top-1];
  if (x==y) return;
  set<int>u;
  set_intersection(sets[x].begin(), sets[x].end(),
	    sets[y].begin(), sets[y].end(),
	    inserter(u, u.begin()));
  stk[top-1]=setID(u);  
}


void Union()
{
  dout << "start union\n";
  int x=stk[--top], y=stk[top-1];
  if (x==y) return;
  set<int>u;
  set_union(sets[x].begin(), sets[x].end(),
	    sets[y].begin(), sets[y].end(),
	    inserter(u, u.begin()));
  stk[top-1]=setID(u);  
  dout << "stop union\n";
}


void add() 
{
  dout << "start add\n";
  
  set<int> u;
  u.insert(stk[top-1]);
  stk[top-1]=setID(u);  
  Union();  
  dout << "end add\n";
}

void product()
{
  set<int> X=sets[stk[--top]], Y=sets[stk[top-1]];
  setit sx=X.begin(), ex=X.end(), sy=Y.begin(), ey=Y.end();  
  set<int> p,res;
  for (setit ix=sx; ix!=ex; ++ix)
    for (setit iy= (sx != sy) ? sy : ix; iy!=ey; ++iy) {
      p.clear();
      p.insert(*ix);
      p.insert(*iy);
      res.insert(setID(p));
    }
  stk[top-1]=setID(res);  
}


void printset(int s) 
{
  cerr << '{';
  if (s != 1) {
    cerr << ' ';
    for (setit i = sets[s].begin(); i != sets[s].end(); ++i) printset(*i);    
      
  }  
  cerr << "} ";  
}

void solve()
{
  string cmd;
  set<int> empty, dummy;
  sets.clear();  
  mp.clear();  
  sets.push_back(dummy); // 0 is not ID of any set.
  sets.push_back(empty); // 1 is ID of empty set
  mp[empty]=1;
  
  int N;
  cin >> N;  
  while (N-->0) {
    cin>>cmd;    
    dout << cmd << endl;
    
    if (cmd=="PUSH")   stk[top++]=1; // push (ID of) empty set
    else if (cmd=="DUP") { stk[top] = stk[top-1]; ++top; }    
    else if (cmd=="ADD") add();
    else if (cmd=="UNION") Union();
    else if (cmd=="INTERSECT") intersect();
    else if (cmd=="X") product();
    else cerr << "UNKNOWN COMMAND" << endl;    
    cout << sets[stk[top-1]].size() << "\n";
    if (debug) { printset(stk[top-1]); cerr << endl; }
  }

}

int main()
{
  int T;
  cin >> T;  
  for (int i=0; i<T; ++i) {
    dout << "Case " << i+1 << endl;    
    solve();    
    dout << "Done " << i+1 << endl;    
    cout << "***"<<endl;    
  }
  
  return 0;
}

  

