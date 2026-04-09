class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> newNums(nums.size() * 2);
        for(int i = 0; i < nums.size(); i++){
            newNums[i] = nums[i];
            newNums[nums.size() + i] = nums[i];
        }
        return newNums;
    }
};