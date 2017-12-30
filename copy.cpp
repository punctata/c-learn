#include <bits/stdc++.h>

using namespace std;

struct P {
    int x, y;
};

void change(const P &p) {
    p.x = 0;
}

int main()
{
    P p0;
    p0.x = 5, p0.y = 10;
    change(p0);
    cout << p0.x << " " << p0.y << endl;
    return 0;
}
