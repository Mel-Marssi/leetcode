#include <iostream>
using namespace std;

class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string merged;
        int j = 0;
        if (word1.length() >= word2.length())
        {
            for (size_t i = 0; i < word1.length(); i++)
            {
                merged.insert(j++, word1, i, 1);
                if (i < word2.length() )
                    merged.insert(j++, word2, i, 1);
            }
        }
        else
        {
            for (size_t i = 0; i < word2.length(); i++)
            {
                if (i < word1.length())
                    merged.insert(j++, word1, i, 1);
                merged.insert(j++, word2, i, 1);
            }
        }
        return merged;
    }
};
