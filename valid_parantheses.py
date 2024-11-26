def isValid(s: str) -> bool:
    stack = []
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for char in s:
        if char in pairs:
            stack.append(char)