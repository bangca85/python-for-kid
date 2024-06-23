'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def is_valid_parentheses(s):
    # Dictionary to hold matching pairs
    matching_bracket = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []

    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        print("stack", stack)
        print(char);
        if char in matching_bracket:
            # Pop the topmost element from the stack if it's not empty; otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            print(stack)
            print("top_element", top_element)
            if matching_bracket[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched properly
    print(stack)
    return not stack

def main():
    # print(is_valid_parentheses("12()"))        # Output: true
    # print(is_valid_parentheses("()[]{}"))    # Output: true
    # print(is_valid_parentheses("(]"))        # Output: false
    # print(is_valid_parentheses("([)]"))      # Output: false
    print(is_valid_parentheses("{[]}"))      # Output: true

if __name__ == "__main__":
    main()

