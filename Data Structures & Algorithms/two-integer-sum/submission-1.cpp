class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++){
            int a = target - nums[i];
            auto result = std::find(nums.begin()+i+1,nums.end(),a);
            if (result != nums.end()) {
                int j = result - nums.begin();
                return {i, j};
            }
        }
    }
};
