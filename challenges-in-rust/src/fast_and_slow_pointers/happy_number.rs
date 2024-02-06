// Solving the Happy Number Challenge
// Problem Statement:
// A happy number is a number which eventually reaches 1 when replaced
//  by the sum of the square of each digit. 
// For example, 23 is a happy number:
// Input: 23
// 2^2 + 3^2 = 4 + 9 = 13
// 1^2 + 3^2 = 1 + 9 = 10
// 1^2 + 0^2 = 1 + 0 = 1
// Output: true

fn square_digit_sum(mut n: i32) -> i32 {
    let mut sum: i32 = 0;
    while n > 0 {
        let digit: i32 = n % 10; // 23 % 10 = 3
        sum += digit * digit; // 3 * 3 = 9
        n /= 10; // 23 / 10 = 2
    }
    sum
}

// Big O Analysis:
// Time complexity: O(log n) | Space complexity: O(1)
pub fn is_happy(n: i32) -> bool {
    let mut slow: i32 = n;
    let mut fast: i32 = square_digit_sum(n); // 23 -> 13
    while fast != 1 && slow != fast {
        slow = square_digit_sum(slow); // 23 -> 13 -> 10 -> 1
        fast = square_digit_sum(square_digit_sum(fast)); // 23 -> 13 -> 10 -> 1
    }
    fast == 1
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_happy() {
        assert!(is_happy(23));
        assert!(is_happy(19));
        assert!(!is_happy(2));
    }

    #[test]
    fn test_square_digit_sum() {
        assert_eq!(square_digit_sum(23), 13);
        assert_eq!(square_digit_sum(13), 10);
        assert_eq!(square_digit_sum(10), 1);
    }
}

