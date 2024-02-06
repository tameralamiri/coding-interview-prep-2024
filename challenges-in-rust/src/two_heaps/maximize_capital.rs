// Solving the "Maximize Capital" Challenge
// Problem Statement
// Given two arrays: Capital and Profits of equal length and an integer k. 
// Each element in Capital shows the capital that must be invested to start the corresponding project in Profits. 
// You are given an initial amount of capital initial_capital. You can only start at most k projects. 
// You can only start a project if you have enough capital. 
// Once a project is started, you can assume you instantly gain its profit which can then be used to start other projects. 
// Find the maximum capital you can achieve after finishing at most k projects.

// Implementation Strategy
// Use two heaps (priority queues in Rust):

// A min-heap to keep track of projects available within the current capital (W).
// A max-heap to keep track of profitable projects that can be started.
// Rust Implementation
// Assuming Rust's standard library doesn't have a dedicated max-heap, 
// we use BinaryHeap with reversed profit values for the min-heap and tuples of (Profit, Capital) for sorting.

use std::collections::BinaryHeap;

pub fn find_maximum_capital(capital: Vec<i32>, profits: Vec<i32>, initial_capital: i32, k: i32) -> i32 {
    println!("capital: {:?}", capital);
    println!("profits: {:?}", profits);
    println!("initial_capital: {:?}", initial_capital);
    println!("k: {:?}", k);
    let mut available_capital = initial_capital;
    let mut projects = capital.into_iter().zip(profits).collect::<Vec<_>>();
    println!("projects: {:?}", projects);
    projects.sort_by_key(|x| x.0); // Sort by capital required in ascending order
    let mut available_projects = BinaryHeap::new();

    for _ in 0..k {
        while let Some(&next_project) = projects.iter().find(|&&(capital, _)| capital <= available_capital) { // Find the next project that can be started
            available_projects.push(std::cmp::Reverse(next_project.1)); // Push the profit value to a max-heap
            projects.retain(|&x| x != next_project); // Remove the project from the list
            println!("available_projects: {:?}", available_projects);
            println!("projects: {:?}", projects);
            println!("next_project: {:?}", next_project);
            println!("available_capital: {:?}", available_capital);
            println!("k: {:?}", k);
        }
        if let Some(std::cmp::Reverse(profit)) = available_projects.pop() { // Pop the max profit value
            available_capital += profit;
            println!("profit: {:?}", profit);
        } else {
            break; // No projects can be started
        }
    }

    available_capital
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_maximum_capital() {
        assert_eq!(find_maximum_capital(vec![0, 1, 2], vec![1, 2, 3], 1, 2), 4);
        assert_eq!(find_maximum_capital(vec![0, 1, 2, 3], vec![1, 2, 3, 5], 0, 3), 6);
    }
}