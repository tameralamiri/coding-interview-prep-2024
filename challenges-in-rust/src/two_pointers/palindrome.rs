// Checking for Palindrome
// A palindrome is a string that reads the same forward and backward. 

// Big O Analysis:
// Time complexity: O(n) | Space complexity: O(n)
pub fn is_palindrome(s: &str) -> bool {
    let s: Vec<char> = s.chars().filter(|c: &char| c.is_alphanumeric()).collect();
    let mut left: usize = 0;
    let mut right: usize = s.len().checked_sub(1).unwrap_or(0);
    
    while left < right {
        if s[left].to_lowercase().ne(s[right].to_lowercase()) {
            return false;
        }
        left += 1;
        right -= 1;
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_palindrome_simple() {
        assert!(is_palindrome("racecar"));
        assert!(!is_palindrome("rust"));
    }

    #[test]
    fn test_is_palindrome_complex() {
        assert!(is_palindrome("A man, a plan, a canal: Panama"));
        assert!(!is_palindrome("This is not a palindrome"));
    }

    #[test]
    fn test_is_palindrome_case_insensitive() {
        assert!(is_palindrome("RaceCar"));
        assert!(is_palindrome("No lemon, no melon"));
    }

    #[test]
    fn test_is_palindrome_empty_and_single_char() {
        assert!(is_palindrome(""));
        assert!(is_palindrome("a"));
    }
}