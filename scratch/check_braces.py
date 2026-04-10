import os

def check_braces(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stack = []
    for i, char in enumerate(content):
        if char == '{':
            stack.append(i)
        elif char == '}':
            if not stack:
                print(f"Excessive closing brace at index {i}")
                return False
            stack.pop()
    
    if stack:
        for pos in stack:
            print(f"Unclosed open brace at index {pos}")
            # Peek some context
            start = max(0, pos - 20)
            end = min(len(content), pos + 20)
            print(f"Context: {content[start:end]}")
        return False
    
    print("Braces are balanced.")
    return True

if __name__ == "__main__":
    check_braces('static/script.js')
