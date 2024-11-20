class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s == " ") return 1;
        map < char , int > mp;
        for (char ch = 'a'; ch <= 'z'; ch++) mp[ch] = -1;
        int strt = -1, ans = 0;
        for (int i = 0; i < s.size(); i++) {
            if (mp[s[i]] > strt) 
                strt = mp[s[i]];
            mp[s[i]] = i;
            ans = max(ans, i - strt);
        }
        return ans;
    }
};