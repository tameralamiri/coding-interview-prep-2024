# Big O: O(n) time, O(n) space
def is_palindrome(s: str) -> bool:
    cleaned = ''.join([c for c in s.lower() if c.isalnum()])
    return cleaned == cleaned[::-1]

# Big O: O(n) time, O(1) space
def is_palindrome(s: str) -> bool:
    # check for empty string
    if not s: return True
    left, right = 0, len(s) - 1
    while left < right:
        # skip non-alphanumeric characters
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -=1

        # Check if charecters are equal
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1

    return True

assert(is_palindrome("A man, a plan, a canal, Panama"))
assert(is_palindrome(""))
assert(is_palindrome("a"))
assert not (is_palindrome('hello'))
assert(is_palindrome('racecar'))
