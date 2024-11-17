class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector < int > left(n), right(n);

        left[0] = height[0];
        right[n - 1] = height[n - 1];

        for (int i = 1; i < n; i++) {
            int ele = max(height[i], left[i - 1]);
            left[i] = ele;
        }
        for (int i = n - 2; i >= 0; i--) {
            int ele = max(height[i], right[i + 1]);
            right[i] = ele;
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += abs(height[i] - min(left[i], right[i]));
        }
        return ans;
    }
};