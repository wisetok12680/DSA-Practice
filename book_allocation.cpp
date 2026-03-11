bool isPossible(int arr[], int n, int m, int mid) {
    int studentCount = 1;
    int sum = 0;

    for(int i = 0; i < n; i++) {
        if(arr[i] > mid)
            return false;

        if(sum + arr[i] <= mid) {
            sum += arr[i];
        }
        else {
            studentCount++;
            sum = arr[i];

            if(studentCount > m)
                return false;
        }
    }

    return true;
}

int allocatePages(int arr[], int n, int m) {
    int s = 0;
    int e = 0;
    int ans = -1;

    for(int i = 0; i < n; i++)
        e += arr[i];

    while(s <= e) {
        int mid = (s + e) / 2;

        if(isPossible(arr, n, m, mid)) {
            ans = mid;
            e = mid - 1;
        }
        else {
            s = mid + 1;
        }
    }

    return ans;
}