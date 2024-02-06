mod top_kth_element;
mod sliding_window;
mod two_pointers;
mod fast_and_slow_pointers;
mod merge_intervals;
mod inplace_linkedlist_reversal;
mod two_heaps;
mod k_way_merge;
mod top_k_elements;
mod modified_binary_search;

fn main() {
    println!("Hello, world!");
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];
    let largest: Option<i32> = top_kth_element::largest_number::find_largest(&numbers);
    let max_sum_contiguous_subarray: Option<i32> = sliding_window::max_sum_contiguous_subarray::max_sum_contiguous_subarray(&numbers, 3);
    let max_sum: Option<i32> = sliding_window::max_sum::max_sum(&numbers);
    println!("largest: {:?}", largest);
    println!("max_sum_contiguous_subarray: {:?}", max_sum_contiguous_subarray);
    println!("max_sum: {:?}", max_sum);

    // Summing the values:
    let total = largest.unwrap_or(0) + max_sum_contiguous_subarray.unwrap_or(0) + max_sum.unwrap_or(0);
    println!("total: {:?}", total);

    // Checking for Palindrome
    // A palindrome is a string that reads the same forward and backward.
    let is_palindrome: bool = two_pointers::palindrome::is_palindrome("A man, a plan, a canal: Panama");
    println!("is_palindrome: {:?}", is_palindrome);

    // Solving the Happy Number Challenge
    let is_happy: bool = fast_and_slow_pointers::happy_number::is_happy(23);
    println!("is_happy: {:?}", is_happy);

    // Solving the "Repeated DNA Sequences" Challenge
    let find_repeated_dna_sequences: Vec<String> = sliding_window::dna_squences::find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT");
    println!("find_repeated_dna_sequences: {:?}", find_repeated_dna_sequences);

    // Solving the "Merge Intervals" Challenge
    let merge_intervals: Vec<Vec<i32>> = merge_intervals::merge_intervals::merge(vec![vec![1, 3], vec![2, 6], vec![8, 10], vec![15, 18]]);
    println!("merge_intervals: {:?}", merge_intervals);

    // Solving the "Reverse linked list" Challenge
    let revesed_list = inplace_linkedlist_reversal::reverse_list::reverse_list(vec![1, 2, 3, 4, 5]);
    println!("revesed_list: {:?}", revesed_list);

    // Solving the "Maximize Capital" Challenge
    let maximize_capital = two_heaps::maximize_capital::find_maximum_capital(vec![0, 1, 2], vec![1, 2, 3], 1, 2);
    println!("maximize_capital: {:?}", maximize_capital);

    // Solving the "Merge Sorted Arrays" Challenge
    let mut nums1 = vec![1, 2, 3, 0, 0, 0];
    let m = 3;
    let mut nums2 = vec![2, 5, 6];
    let n = 3;
    k_way_merge::merge_sorted_array::merge(&mut nums1, m, &mut nums2, n);
    println!("merge_sorted_array: {:?}", nums1);

    // Solving the "Kth Largest Element" Challenge
    let mut kth_largest = top_k_elements::kth_largest_element::KthLargest::new(3, vec![4, 5, 8, 2]);
    println!("kth_largest: {:?}", kth_largest.add(3));


    // Solving the "Binary Search" Challenge
    let binary_search = modified_binary_search::binary_search::binary_search(vec![-1, 0, 3, 5, 9, 12], 9);
    println!("binary_search: {:?}", binary_search);


    
}