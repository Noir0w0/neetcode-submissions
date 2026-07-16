class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> my_map;
        for (auto str : strs){
            string sorted_str = str;
            std::sort(sorted_str.begin(), sorted_str.end());
            my_map[sorted_str].push_back(str);
        }
        vector<vector<string>> result;
        for (auto& [key,val] : my_map){
            result.push_back(val);
        }
        return result;
    }    
};

