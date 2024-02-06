pub fn max_sum(numbers: &[i32]) -> Option<i32> {
    if numbers.is_empty() {
        return None;
    }
    let mut max_current: i32 = numbers[0];
    let mut max_global: i32 = numbers[0];

    for &number in numbers.iter().skip(1) {
        max_current = std::cmp::max(number, max_current + number);
        max_global = std::cmp::max(max_global, max_current);
    }

    Some(max_global)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_sum() {
        assert_eq!(max_sum(&[1, 2, 3, 4, 5]), Some(15));
        assert_eq!(max_sum(&[1, 2, 3, 4, 5, 6]), Some(21));
        assert_eq!(max_sum(&[1, 2, -1, 3, 4, 10, 10, -10, -1]), Some(29));
        assert_eq!(max_sum(&[-1, -2, -3, -4]), Some(-1));
    }
}