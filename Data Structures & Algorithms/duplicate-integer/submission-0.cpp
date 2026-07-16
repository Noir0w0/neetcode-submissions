class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> my_set;
        for(const auto& num : nums){
            int pre_size = my_set.size();
            my_set.insert(num);
            if (my_set.size() == pre_size) {
                return true;
            }
        }
        return false;
    }
};