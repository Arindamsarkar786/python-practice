

#include<bits/stdc++.h>
#define int long long
using namespace std;
void solve() {
   int n,s=0;
   string a,b;
   cin >> n >> a >> b;
   map<char,int> P,Q;
   for(char i:a) P[i]++;
   for(char i:b) Q[i]++;
   for(char i='a';i<='z';++i)
      s=max(s,min(P[i],Q[i]));
   cout << s << endl;
}
signed main() {
   int T;cin >> T;
   while(T--) solve();
}
    