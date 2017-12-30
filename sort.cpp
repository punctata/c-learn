#include <bits/stdc++.h>

using namespace std;

#define N 2000000
int n, arr[N];

void merge_sort(int a, int b) {
    if (b - a == 1)
        return;
    else {
        int mid = (a + b) / 2;
        merge_sort(a, mid);
        merge_sort(mid, b);
        int r[b - a];
        for (int i = a, j = mid, k = 0; i != mid || j != b;) {
            if (i == mid)
                r[k++] = arr[j++];
            else if (j == b)
                r[k++] = arr[i++];
            else if (arr[i] <= arr[j])
                r[k++] = arr[i++];
            else
                r[k++] = arr[j++];
        }
        for (int k = 0; k < b - a; k++)
            arr[a + k] = r[k];
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    merge_sort(0, n);
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
