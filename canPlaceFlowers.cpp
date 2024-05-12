#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
	bool canPlaceFlowers(vector<int> &flowerbed, int n)
	{
		bool skip = false;
		int count_of_place = 0;
		vector<int>::iterator it_left = flowerbed.begin();
		for (vector<int>::iterator it = flowerbed.begin(); it != flowerbed.end(); it++)
		{
			if (skip)
			{
				skip = false;
				continue;
			}
			if (it != flowerbed.begin())
				it_left = it - 1;
			if (*it == 0 && *it_left == 0&& (it + 1 != flowerbed.end()  || *(it + 1) == 0))
			{
				count_of_place++;
				skip = true;
			}
		}		
		return (count_of_place >= n);
	}
};

int main()
{
	Solution s;
	vector<int> flowerbed = {1, 0, 0, 0, 1, 0, 0};
	int n = 2;
	cout << s.canPlaceFlowers(flowerbed, n) << endl;
	cout << true << endl;
	return 0;
}