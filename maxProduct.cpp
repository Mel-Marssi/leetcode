#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution
{
public:
	int maxProduct(vector<int> &nums)
	{
		int max_product, min_product, tmp, result;
		max_product = min_product = result = nums[0];
		for (vector<int>::iterator it = nums.begin() + 1; it != nums.end(); it++)
		{
			if (*it == 0)
			{
				max_product = min_product = 1;
				// continue;
			}
			tmp = max_product;
			max_product = max(max(max_product * (*it), min_product * (*it)), *it);
			min_product = min(min(tmp * (*it), min_product * (*it)), *it);
			result = max(result, max_product);
		}
		return result;
	}
};

int main()
{
	Solution s;
	vector<int> v = {-2,0,-1};
	cout << s.maxProduct(v) << endl;
}