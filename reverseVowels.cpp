#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

class Solution
{
private:
	int first_index;

public:
	Solution()
	{
		first_index = 0;
	}
	string reverseVowels(string s)
	{
		for (size_t i = s.length() - 1; i > 0; i--)
		{
			if (strchr("aeiouAEIOU", s[i]) != NULL)
			{
				for (; first_index < i; first_index++)
				{
					if (strchr("aeiouAEIOU", s[first_index]) != NULL)
					{
						std::swap(s[first_index], s[i]);
						first_index++;
						break;
					}
				}
			}
		}
		return s;
	}
};

int main()
{
	Solution s;
	cout << s.reverseVowels("race car") << endl;
}