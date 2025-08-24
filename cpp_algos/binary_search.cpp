#include <bits/stdc++.h>
using namespace std;

int binary_search(vector<int>& arr, int target) {
    int l = 0, r = arr.size() - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}

int main(int argc, char* argv[]) {
    // expects input like: ./binary_search 7
    vector<int> arr = {1, 2, 3, 7, 7, 9};
    if (argc < 2) {
        cout << "Usage: binary_search <number>" << endl;
        return 1;
    }
    int target = stoi(argv[1]);
    cout << binary_search(arr, target) << endl;
    return 0;
}
