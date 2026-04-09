class Solution {
public:
    bool isValid(string input) {
        stack<char> brackets; // Stack to store expected closing brackets
        for (char bracket : input) {
            switch (bracket) {
                case '(':
                    brackets.push(')');
                    break;
                case '[':
                    brackets.push(']');
                    break;
                case '{':
                    brackets.push('}');
                    break;
                default:
                    // Return false for non-bracket characters or mismatched brackets
                    if (brackets.empty() || brackets.top() != bracket) {
                        return false;
                    }
                    brackets.pop();
            }
        }
        return brackets.empty(); // Valid if all brackets are matched
    }
};