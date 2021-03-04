#!/bin/env python3
import sys

# Implement a stack
# Use stack structure to validate that parenthesis are matched.


class Stack:
    def __init__(self):
        self._size = 0
        self._stack = []

    def empty(self):
        if self._size == 0:
            return True
        return False

    def size(self):
        return self._size

    def push(self, elem):
        self._stack.append(elem)
        self._size += 1

    def pop(self):
        if not self.empty():
            self._size -= 1
            return self._stack.pop()

    def peek(self):
        if not self.empty():
            return self._stack[self._size - 1]


# List of tuples of syntax string, and is_valid?
test_cases = [
    ("()", True),
    ("(", False),
    ("[{()}]", True),
    ("[{)(}]", False),
    ("[}", False),
    ("[[}", True),  # intentional failure
    ("[asdf(asdf)wer;{ii}][0];", True)]


def check_if_valid(syntax_str):
    left_parenths = {
        "(": ")",
        "[": "]",
        "{": "}"}
    right_parenths = {
        "}": "{",
        "]": "[",
        ")": "("}

    stack = Stack()

    # When we encounter a left hand parenth, we push the right
    # hand parenth onto the stack. Later, then we encounter a
    # right hand parent, we look at the top of the stack to confirm
    # that our current right hand parenth matches whats on the stack.
    for char in syntax_str:
        left_compliment = left_parenths.get(char, None)

        if left_compliment is not None:
            stack.push(left_compliment)
            continue

        if right_parenths.get(char, None) is not None:
            if stack.peek() == char:
                stack.pop()
                continue
            return False

    if stack.empty():
        return True

    return False


def run_tests():
    for syntax_str, is_valid in test_cases:
        sys.stdout.write(
            f"Running test case: {syntax_str}: "
            f"Exp: {is_valid}")
        ret = check_if_valid(syntax_str)
        if ret == is_valid:
            print(f", Obs: {ret} - PASSED")
        else:
            print(f", Obs: {ret} - FAILED")


run_tests()
