#include<bits/stdc++.h>

using namespace std;
#define ll long long int
#define vl vector<ll>
#define vvl vector<vl>
#define pll pair<ll, ll>

struct hash_pair {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2>& p) const{
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ hash2;
    }
};
#define umap_pll_l  unordered_map<pll, ll, hash_pair>

void dfs1(ll nod, ll par, vvl&G, vl &S, vl &P, vl &C, vl &L, ll curlev){
  C[nod] = 1; P[nod] = par;
  L[nod] = curlev;
  for(auto cnod: G[nod]){
    if(cnod != par){
      dfs1(cnod, nod, G, S, P, C, L, curlev+1);
      C[nod] += C[cnod];
      S[nod] += S[cnod] + C[cnod];
    }
  }
}

void dfs2(ll nod, ll par, vvl&G, vl &T, vl &S, vl &C, umap_pll_l & Contdp, umap_pll_l & Cdp, ll n){
  T[nod] = T[par] + n - 2*C[nod];
  for(auto cnod: G[nod])
    if(cnod != par){
      dfs2(cnod, nod, G, T, S, C, Contdp, Cdp, n);
      Cdp[make_pair(nod,cnod)] = C[cnod];
      Contdp[make_pair(nod, cnod)] = S[cnod];
      Contdp[make_pair(cnod, nod)] = T[nod] - S[cnod] - C[cnod];
    }
  Cdp[make_pair(nod, par)] = n - C[nod];

}

void goUpBy(ll& u, ll dist, vvl & Pdp){
  for(ll i=20; i>=0; i--)
    if((1<<i) <= dist){
      dist -= (1<<i);
      u = Pdp[u][i];
    }
}

ll getLca(ll a, ll b, vvl &Pdp, vl & L){
  ll u = a, v = b;
  //cout << "nodes " << u << " " << v << endl;
  //cout << "level " << L[u] << " " << L[v] << endl;
  if(L[u] > L[v]) goUpBy(u, L[u]-L[v], Pdp);
  if(L[u] < L[v]) goUpBy(v, L[v]-L[u], Pdp);

  // u and v are at the same place
  if (u==v) return u;

  //cout << "mid\nnodes " << u << " " << v << endl;
  //cout << "level " << L[u] << " " << L[v] << endl;
  for(int i=19; i>=0; i--)
    if(Pdp[u][i] != 0 && Pdp[u][i] != Pdp[v][i])
      u = Pdp[u][i], v = Pdp[v][i];
  //cout << "One last time " << u << " " << v << "\n";
  u = Pdp[u][0];
  return u;
}

void getMidProps(ll &a, ll &b, vvl& Pdp, vl &L, vl & v){
  ll lca = getLca(a, b, Pdp, L);
  //cout << "LCA FOR " << a <<" " << b << " is "<< lca << "\n";
  ll dist = abs(L[lca] - L[a]) + abs(L[lca] - L[b]);
  //cout << "dist " << dist << "\n";
  ll mva = (dist-1)/2, mvb;
  ll m1 = a, m2;
  // move m1
  goUpBy(m1, mva, Pdp);

  //cout <<"[ A Mid_1 ] "<< a << " " << m1 << " " <<L[m1] << "\n";
  // for mvb  if b is lca them
  mvb = dist - 1 - mva; m2 = b;
  if(m1 != lca) m2 = Pdp[m1][0];
  else{
    goUpBy(m2, mvb, Pdp);
  }
  //cout <<"[ B Mid_2 ] "<< b << " " << m2 <<" " << L[m2]<< "\n";
  //cout << "Parent " << Pdp[m2][0] << "\n";
  v[0] = m1; v[1] = m2;  v[2] = mva; v[3] = mvb;
}

void showRoute(ll a, ll b, vvl & Pdp){
  cout << "[A] " << a << " ";
  while(Pdp[a][0] != 0){
    a = Pdp[a][0];
    cout << a << " ";
  } cout << "\n";

  cout << "[B] " << b << " ";
  while(Pdp[b][0] != 0){
    b = Pdp[b][0];
    cout << b << " ";
  } cout << "\n";
}
void solve(vvl &G, int n, int q){
  // preprocess
  vl S(n+1, 0), P(n+1, 0), C(n+1, 0), T(n+1, 0), L(n+1, 0);
  //vl Contdp(n+1, 0), Cdp(n+1, 0);
  umap_pll_l Contdp, Cdp;
  dfs1(1, 0, G, S, P, C, L, 1);

  T[0] = S[1] + C[1];
  dfs2(1, 0, G, T, S, C, Contdp, Cdp, n);
  
// lca precomputation
  vvl Pdp(n+1, vl(20, 0));
  for(int nod=1; nod<=n; nod++) Pdp[nod][0] = P[nod];
  for(int j=1; j<20; j++)
    for(int nod=1; nod<=n; nod++)
    Pdp[nod][j] = Pdp[Pdp[nod][j-1]][j-1];
/*cout << "CONT DP\n\n";
  for(auto pi: Contdp) cout << pi.first.first << " " << pi.first.second << " " << pi.second<<endl;
  cout << "\nC DP \n\n";
  for(auto pi: Cdp) cout << pi.first.first << " " << pi.first.second << " " << pi.second<<endl;
  cout << "\n";
*/
  vector<ll> v(4, 0);
  ll a, b, ans=0;
  while(q--){
    //cout << "\n";
    cin>>a>>b;
    //showRoute(a, b, Pdp);
    if (L[a] < L[b]) swap(a, b); // a always remain at a depth
    getMidProps(a, b, Pdp, L, v);
    ll m1 = v[0], m2 = v[1], da=v[2], db=v[3];
    //for(auto it: v) cout << it << " "; cout << "\n";
    ll conta = T[a] - (da+1)*Cdp[{m1, m2}] - Contdp[{m1, m2}];
    ll contb = T[b] - (db+1)*Cdp[{m2, m1}] - Contdp[{m2, m1}];
    //cout << "[CONT] " << conta << " " << contb << "\n";
    ans = conta + contb;
    cout <<ans << "\n";
  }
}

int main(){
    ios::sync_with_stdio(false);  cin.tie(NULL);
  int t; cin>>t;
  ll n, q;
  while(t--){
    cin>>n>>q;
    vvl G(n+1);
    ll u, v;
    for(int i=1; i<n; i++){
      cin>>u>>v;
      G[u].push_back(v);
      G[v].push_back(u);
    }
    solve(G, n, q);
  }
return 0;
}