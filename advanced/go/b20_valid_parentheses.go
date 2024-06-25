/*
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
*/

package main

func isValidParentheses(s string) bool {
	// Map to hold matching pairs
	matchingBracket := map[rune]rune{')': '(', '}': '{', ']': '['}
	// Stack to keep track of opening brackets
	stack := []rune{}

	// Iterate through each character in the string
	for _, char := range s {
		// If the character is a closing bracket
		if match, found := matchingBracket[char]; found {
			// Check if the stack is not empty and if the top element matches the expected opening bracket
			if len(stack) > 0 && stack[len(stack)-1] == match {
				// Pop the top element from the stack
				stack = stack[:len(stack)-1]
			} else {
				// If no match is found, return false
				return false
			}
		} else {
			// If it's an opening bracket, push it onto the stack
			stack = append(stack, char)
		}
	}

	// If the stack is empty, all brackets were matched properly
	return len(stack) == 0
}
