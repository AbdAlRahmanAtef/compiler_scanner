import re

# Define token types and their regex patterns
token_patterns = [
    ("KEYWORD", r"\b(int|float|return|if|else)\b"),
    ("IDENTIFIER", r"\b[a-zA-Z_]\w*\b"),
    ("NUMBER", r"\b\d+(\.\d+)?\b"),
    ("OPERATOR", r"[+\-*/=<>!]+"),
    ("SPECIAL_CHAR", r"[;{}(),]"),
    ("WHITESPACE", r"\s+"),
    ("STRING_LITERAL", r'"([^"\\]|\\.)*"'),
]

# Compile patterns into regex objects
token_regex = [(name, re.compile(pattern)) for name, pattern in token_patterns]


# Scanner function
def scanner(code):
    pos = 0
    tokens = []
    while pos < len(code):
        match = None
        for token_type, pattern in token_regex:
            match = pattern.match(code, pos)
            if match:
                if token_type != "WHITESPACE":  # Ignore whitespace
                    tokens.append((token_type, match.group()))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Unexpected character: {code[pos]}")
    return tokens


# Test the scanner with a small piece of code
sample_code = "int main() {int x = 10; return 42; }"
tokens = scanner(sample_code)
for token in tokens:
    print(token)
