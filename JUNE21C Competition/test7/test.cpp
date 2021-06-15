#include <bits/stdc++.h>

using namespace std;

vector<int> adj[500001];

int visA[500001], visB[500001], disA[500001], disB[500001];

void dfs1(int node, int d)
{
    visA[node] = 1;
    disA[node] = d;
    for (int child : adj[node])
    {
        if (visA[child] == 0)
        {
            dfs1(child, disA[node] + 1);
        }
    }
}

void dfs2(int node, int d)
{
    visB[node] = 1;
    disB[node] = d;
    for (int child : adj[node])
    {
        if (visB[child] == 0)
        {
            dfs2(child, disB[node] + 1);
        }
    }
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, a, b, q;
        cin >> n >> q;
        for (int i = 1; i < n; i++)
        {
            cin >> a >> b;
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        while (q--)
        {
            int sum = 0;
            cin >> a >> b;
            dfs1(a, 0);
            dfs2(b, 0);
            for (int i = 1; i <= n; i++)
            {
                sum += min(disA[i], disB[i]);
            }
            cout << sum << endl;
            for (int i = 1; i <= n; i++)
            {
                disB[i] = 0;
                disA[i] = 0;
                visA[i] = 0;
                visB[i] = 0;
            }
        }
        for (int i = 1; i <= n; i++)
        {
            adj[i].clear();
            disB[i] = 0;
            disA[i] = 0;
            visA[i] = 0;
            visB[i] = 0;
        }
    }
}