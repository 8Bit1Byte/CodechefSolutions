#include <bits/stdc++.h>

using namespace std;
#define ll long long int

ll solve(vector<vector<ll>> &P, int n)
{
    unordered_map<ll, ll> min_X, max_X, min_Y, max_Y;
    ll x, y;
    for (auto vec : P)
    {
        x = vec[0], y = vec[1];
        if (min_X.find(y) == min_X.end())
        {
            min_X[y] = x;
            max_X[y] = x;
        }
        if (min_Y.find(x) == min_Y.end())
        {
            min_Y[x] = y;
            max_Y[x] = y;
        }

        min_X[y] = min(min_X[y], x);
        max_X[y] = max(max_X[y], x);
        min_Y[x] = min(min_Y[x], y);
        max_Y[x] = max(max_Y[x], y);
    }
    vector<ll> X, Y;
    for (auto pi : min_Y)
        X.push_back(pi.first);
    for (auto pi : min_X)
        Y.push_back(pi.first);
    ll xlen = X.size(), ylen = Y.size();

    sort(X.begin(), X.end());
    sort(Y.begin(), Y.end());
    ll area = LLONG_MAX;

    // Vertical DP
    vector<ll> pref, suff;
    ll mn = LLONG_MAX, mx = LLONG_MIN;
    for (auto x : X)
    {
        mn = min(mn, min_Y[x]);
        mx = max(mx, max_Y[x]);
        pref.push_back((x - X[0]) * (mx - mn));
    }
    reverse(X.begin(), X.end());
    mn = LLONG_MAX, mx = LLONG_MIN;
    for (auto x : X)
    {
        mn = min(mn, min_Y[x]);
        mx = max(mx, max_Y[x]);
        suff.push_back((X[0] - x) * (mx - mn));
    }
    reverse(X.begin(), X.end());
    reverse(suff.begin(), suff.end());
    suff.push_back(0);

    for (int i = 0; i < xlen; i++)
        area = min(area, pref[i] + suff[i + 1]);

    // Horizontal DP
    pref.clear();
    suff.clear();
    mn = LLONG_MAX, mx = LLONG_MIN;
    for (auto y : Y)
    {
        mn = min(mn, min_X[y]);
        mx = max(mx, max_X[y]);
        pref.push_back((y - Y[0]) * (mx - mn));
    }
    reverse(Y.begin(), Y.end());
    mn = LLONG_MAX, mx = LLONG_MIN;
    for (auto y : Y)
    {
        mn = min(mn, min_X[y]);
        mx = max(mx, max_X[y]);
        suff.push_back((Y[0] - y) * (mx - mn));
    }
    reverse(Y.begin(), Y.end());
    reverse(suff.begin(), suff.end());
    suff.push_back(0);
    for (int i = 0; i < ylen; i++)
        area = min(area, pref[i] + suff[i + 1]);

    return area;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<vector<ll>> p;
        int x, y;
        for (int i = 0; i < n; i++)
        {
            cin >> x >> y;
            vector<ll> v = {x, y};
            p.push_back(v);
        }
        cout << solve(p, n) << "\n";
    }
    return 0;
}