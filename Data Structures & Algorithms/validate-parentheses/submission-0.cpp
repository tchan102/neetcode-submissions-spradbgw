class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for(char c : s){
            switch (c) {
                case '(':
                    stack.push_back(')');
                    break;
                case '[':
                    stack.push_back(']');
                    break;
                case '{':
                    stack.push_back('}');
                    break;
                default:
                    if (stack.empty() || stack.back() != c){
                        return false;
                    }
                    stack.pop_back();
            }
        }
        return stack.empty();
    }
};
