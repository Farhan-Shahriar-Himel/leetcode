#include <bits/stdc++.h>

class Solution {
public:
    unordered_set < int > foundBoxes;
    vector < bool > vis;

    int dfs(int src, vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes)
    {
            int cnd = 0;
            if (status[src]) cnd += candies[src];
            else {
                foundBoxes.insert(src);
                return 0;
            }
            
            vis[src] = true;

            for (auto bx: keys[src])
            {
                status[bx] = 1;
                if (foundBoxes.count(bx) and !vis[bx])
                {
                    cnd += dfs(bx, status, candies, keys, containedBoxes);
                }
            }

            for (auto nei: containedBoxes[src])
            {
                if (!vis[nei])
                {
                    cnd += dfs(nei, status, candies, keys, containedBoxes);
                }
            }

            return cnd;
    }

    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        
        int n = status.size();
        vis.resize(n);

        int res = 0;
        for (auto box: initialBoxes)
        {
            res += dfs(box, status, candies, keys, containedBoxes);
        }

        return res;
    }
};