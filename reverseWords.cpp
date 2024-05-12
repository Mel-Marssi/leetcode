#include <iostream>
#include <string>
#include <sstream>      // std::istringstream
#include <algorithm>
using namespace std;

class Solution
{
private:
	string reverse;

public:
	string reverseWords(string s)
	{
		istringstream ss(s);
		for (string word; ss >> word;)
		{
			reverse.insert(0, word + " ");
		}
		if(reverse[reverse.length() - 1] == ' ')
		{
			reverse.pop_back();
		}
		return reverse;
	}
};

int main()
{
	Solution s;
	cout << "|" << s.reverseWords("a good        example") << "|" << endl;
}