class Solution {
public:
    static bool cmp(string s1, string s2)
    {
        return s1.size() > s2.size();
    }

    bool isPresent(string s1, string s2)
    {
        int n = s1.size(), m = s2.size();
        for (int i = 0; i <= n - m; i++)
        {
            if (s1[i] == s2[0])
            {
                string sub = s1.substr(i, m);
                if (sub == s2) return true;
            }
        }
        return false;
    }

    vector<string> stringMatching(vector<string>& words) {
        vector < string > res;
        sort(words.begin(), words.end(), cmp);

        for (int i = 0; i < words.size(); i++)
        {
            for (int j = i - 1; j >= 0; j--)
            {
                if (isPresent(words[j], words[i]))
                {
                    res.push_back(words[i]);
                    break;
                }
            }
        }

        return res;
    }
};