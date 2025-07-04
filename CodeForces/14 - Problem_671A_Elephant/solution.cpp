#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, x =0;
    cin >> n;
    if (n <= 5) x = 1;
    else {
        x = ceil((float)x/5.0);
    }
    cout << x << endl;
    return 0;
}