class Solution {
public:
    bool vis[307][307];

    void dfs(int i, int j, vector<vector<char>> &grid, int m, int n) {
        if (i < 0 or j < 0 or i >= m or j >= n) return;
        if (vis[i][j] or grid[i][j] == '0') return;
        vis[i][j] = true;
        dfs(i + 1, j, grid, m, n);
        dfs(i - 1, j, grid, m, n);
        dfs(i, j + 1, grid, m, n);
        dfs(i, j - 1, grid, m, n);
    }

    int numIslands(vector<vector<char>>& grid) {
        int cnt = 0;
        int m, n;
        m = grid.size();
        n = grid[0].size();
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if(vis[i][j] or grid[i][j] != '1') continue;
                dfs(i, j, grid, m, n);
                cnt++;
            }
        }
        return cnt;
    }
};