// Solving the "Repeated DNA Sequences" Challenge
// Problem Statement
// Find all the 10-letter-long sequences (substrings) 
// that occur more than once in a DNA molecule.

// Input: "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
// Output: ["AAAAACCCCC", "CCCCCAAAAA"]

// implementation:
// 1. Create a HashMap to store the frequency of each substring
// 2. Iterate through the string, and store the frequency of each substring
// 3. Iterate through the HashMap, and store the substrings that occur more than once
// 4. Return the substrings that occur more than once

// Big O Analysis:
// Time complexity: O(n) | Space complexity: O(n)
use std::collections::HashMap;

pub fn find_repeated_dna_sequences(s: &str) -> Vec<String> {
    // check if the string is empty or less than 10 characters
    if s.is_empty() || s.len() < 10 {
        return Vec::new();
    }
    let mut seen: HashMap<&str, i32> = HashMap::new(); // store the frequency of each substring
    let mut result: Vec<String> = Vec::new(); // store the substrings that occur more than once

    for i in 0..=s.len().saturating_sub(10) { // saturating_sub() returns 0 if the string is less than 10 characters
        let substring: &str = &s[i..i + 10]; // get the substring
        let count = seen.entry(substring).or_insert(0); // get the frequency of the substring
        *count += 1; // increment the frequency

        if *count == 2 { // if the frequency is 2, add the substring to the result
            result.push(substring.to_string());
        }
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_no_repetitions() {
        let input = "AGCTAGCTAG";
        let result = find_repeated_dna_sequences(input);
        assert!(result.is_empty());
    }

    #[test]
    fn test_single_repetition() {
        let input = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
        let result = find_repeated_dna_sequences(input);
        assert_eq!(result, vec!["AAAAACCCCC".to_string(), "CCCCCAAAAA".to_string()]);
    }

    #[test]
    fn test_multiple_repetitions() {
        let input = "AAAAAAAAAAA";
        let result = find_repeated_dna_sequences(input);
        assert_eq!(result, vec!["AAAAAAAAAA".to_string()]);
    }

    #[test]
    fn test_empty_string() {
        let input = "";
        let result = find_repeated_dna_sequences(input);
        assert!(result.is_empty());
    }

    #[test]
    fn test_short_string() {
        let input = "AGCT";
        let result = find_repeated_dna_sequences(input);
        assert!(result.is_empty());
    }
}