#include <bits/stdc++.h>
using namespace std;
const int maxn=2e5+100;
#define ll long long
#define pi pair<int,int>
#define f first
#define s second
int sub[maxn],timer=0,res[maxn],n;
vector<int> g[maxn];
void dfs(int s,int p)
{
    sub[s]=1;
    for(auto it:g[s])
    {
        if(it==p)
        continue;
        dfs(it,s);
        sub[s]+=sub[it];
        res[s]+=res[it];
    }
    res[s]+=sub[s];
}
void dfs1(int s,int p)
{
    timer=max(timer,res[s]);
    for(auto it:g[s])
    {
        if(it==p)
        continue;
        res[it]=res[s]+n-2*sub[it];
        dfs1(it,s);
    }
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        timer=0;
        cin>>n;
        for(int i=1;i<=n;i++)
        {
            g[i].clear();
            res[i]=sub[i]=0;
        }
        for(int i=1;i<n;i++)
        {
            int x,y;
            cin>>x>>y;
            g[x].push_back(y);
            g[y].push_back(x);
        }
        dfs(1,0);
        dfs1(1,0);
        cout<<timer<<'\n';
    }
    return 0;
}
