#include <bits/stdc++.h>

using namespace std;

vector<int> subset;
int n;

void search(int k) {
    if (k == n) {
        for (auto i : subset)
            cout << i << " ";
        cout << "\n";
    }
    else {
        search(k + 1);
        subset.push_back(k);
        search(k + 1);
        subset.pop_back();
    }
}

int main() {
    n = 4;
    search(0);
    return 0;
}