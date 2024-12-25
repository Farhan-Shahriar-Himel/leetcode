class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++)
        {
            int setBit = 0;
            for (auto num: nums)
            {
                if (num & (1 << i))
                {
                    setBit += 1;
                }
            }
            if (setBit % 3 == 1)
            {
                ans |= (1 << i);
            }
        }

        return ans;
    }
};