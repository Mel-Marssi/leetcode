#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
		vector<bool> result;
		int max = *max_element(candies.begin(), candies.end());
		for(vector<int>::iterator it = candies.begin(); it != candies.end(); it++)
		{
			if(*it + extraCandies >= max)
				result.push_back(true);
			else
				result.push_back(false);
		}
		return result;
    }
};