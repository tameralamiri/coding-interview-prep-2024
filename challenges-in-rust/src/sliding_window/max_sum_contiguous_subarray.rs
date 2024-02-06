// Big O Analysis:
// Time: O(n) | Space: O(1) | n = length of input array
pub fn max_sum_contiguous_subarray(numbers: &[i32], window_size: usize) -> Option<i32> {
    if numbers.len() < window_size {
        return None;
    }

    let mut window_sum: i32 = 0;

    for i in 0..window_size {
        window_sum += numbers[i];
    }

    let mut max_sum = window_sum;

    for i in window_size..numbers.len() {
        window_sum += numbers[i] - numbers[i - window_size];
        max_sum = std::cmp::max(max_sum, window_sum);
    }

    Some(max_sum)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_sum_contiguous_subarray() {
        assert_eq!(max_sum_contiguous_subarray(&[1, 2, 3, 4, 5], 3), Some(12));
        assert_eq!(max_sum_contiguous_subarray(&[5, 2, 3, 4, 1], 3), Some(10));
        assert_eq!(max_sum_contiguous_subarray(&[1, 2, 3, 4, 5], 2), Some(9));
        assert_eq!(max_sum_contiguous_subarray(&[1, 2, 3, 4, 5], 1), Some(5));
    }
}