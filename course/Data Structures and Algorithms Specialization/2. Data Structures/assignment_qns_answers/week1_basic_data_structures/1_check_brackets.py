# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(input_str: str) -> None | int:
    stack = []
    for index, char in enumerate(input_str):
        if char in ['{', '[', '(']:
            stack.append((index,char))
        elif char in ['}', ']', ')']:
            if len(stack) == 0:
                return index+1
            latest_open_bracket_index, latest_open_bracket = stack.pop()
            if latest_open_bracket == '{':
                if char != '}':
                    return index+1
            elif latest_open_bracket == '[':
                if char != ']':
                    return index+1
            elif latest_open_bracket == '(':
                if char != ')':
                    return index+1
        else:
            continue
    
    if len(stack) == 0:
        return "Success"
    return stack[-1][0]+1

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
