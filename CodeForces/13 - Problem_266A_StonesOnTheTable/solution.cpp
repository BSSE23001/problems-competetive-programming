#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, x =0;
    string c;
    cin >> n >> c;
    int r = 0,b = 0,g = 0;
    for(auto ch: c) {
        if(ch == 'R') {
            if(r>0) ++x; else ++r;
            if(b>0) --b;
            if(g>0) --g;
        } else if(ch == 'B') {
            if(b>0) ++x; else ++b;
            if(r>0) --r;
            if(g>0) --g;
        } else if(ch == 'G') {
            if(g>0) ++x; else ++g;
            if(r>0) --r;
            if(b>0) --b;
        }
    }
    cout << x << endl;
    return 0;
}