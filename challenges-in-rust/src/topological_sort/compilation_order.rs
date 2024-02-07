// Solving the "Compilation Order" Challenge
// Problem Statement
// Given a list of source code files and a list of dependencies 
// (where each dependency is a pair of files [a, b] indicating that file a depends on file b), 
// determine a valid order in which the files can be compiled. Assume there is at least one valid order.

// Implementation Strategy
// Graph Representation: Represent the files and their dependencies as a graph, 
// where each file is a vertex and each dependency is a directed edge.
// Detect Cycles: Ensure the graph is a DAG (Directed Acyclic Graph), as cyclic dependencies cannot be resolved.
// Apply Topological Sort: Use topological sorting to find a valid compilation order.


// Approach
// We can solve this problem using the following approach:
// Create a graph from the given list of files and dependencies.
// Detect cycles in the graph using depth-first search (DFS).
// If the graph contains a cycle, return an empty list, as cyclic dependencies cannot be resolved.
// Otherwise, apply topological sorting to find a valid compilation order.
// Return the valid compilation order as the result.

// Let's implement the solution step by step.
use std::collections::{HashMap, VecDeque};

// Big O Analysis:
// Time Complexity: O(V + E) | Space Complexity: O(V + E) ,where V is the number of files and E is the number of dependencies.
pub fn compile_order(files: Vec<char>, dependencies: Vec<(char, char)>) -> Vec<char> {
    let mut graph: HashMap<char, Vec<char>> = HashMap::new();
    let mut in_degree: HashMap<char, usize> = HashMap::new();

    for &file in &files {
        graph.entry(file).or_insert(Vec::new());
        in_degree.entry(file).or_insert(0);
    }
    for (file, dependency) in dependencies {
        graph.entry(file).or_insert(Vec::new());
        graph.entry(dependency).or_insert(Vec::new()).push(file);
        *in_degree.entry(file).or_insert(0) += 1;
    }
    let mut queue: VecDeque<char> = VecDeque::new();
    for (file, &degree) in &in_degree {
        if degree == 0 {
            queue.push_back(*file);
        }
    }
    let mut order: Vec<char> = Vec::new();
    while let Some(file) = queue.pop_front() {
        order.push(file);
        for &dependency in graph.get(&file).unwrap() {
            *in_degree.get_mut(&dependency).unwrap() -= 1;
            if *in_degree.get(&dependency).unwrap() == 0 {
                queue.push_back(dependency);
            }
        }
    }
    if order.len() == files.len() {
        order
    } else {
        Vec::new()
    }

}


// ToDo: Refactor the code to use the following implementation
// fn create_graph(files: &[&str], dependencies: &[(&str, &str)]) -> HashMap<&str, Vec<&str>> {
//     let mut graph: HashMap<&str, Vec<&str>> = HashMap::new();
//     for file in files {
//         graph.entry(file).or_insert(Vec::new());
//     }
//     for (file, dependency) in dependencies {
//         graph.entry(file).or_insert(Vec::new());
//         graph.entry(dependency).or_insert(Vec::new()).push(file);
//     }
//     graph
// }

// fn has_cycle(graph: &HashMap<&str, Vec<&str>>, file: &str, visited: &mut HashSet<&str>, stack: &mut HashSet<&str>) -> bool {
//     if stack.contains(file) {
//         return true;
//     }
//     if visited.contains(file) {
//         return false;
//     }
//     visited.insert(file);
//     stack.insert(file);
//     for &dependency in graph.get(file).unwrap() {
//         if has_cycle(graph, dependency, visited, stack) {
//             return true;
//         }
//     }
//     stack.remove(file);
//     false
// }

// fn detect_cycle(graph: &HashMap<&str, Vec<&str>>) -> bool {
//     let mut visited: HashSet<&str> = HashSet::new();
//     let mut stack: HashSet<&str> = HashSet::new();
//     for file in graph.keys() {
//         if has_cycle(graph, file, &mut visited, &mut stack) {
//             return true;
//         }
//     }
//     false
// }

// fn topological_sort(graph: &HashMap<&str, Vec<&str>>) -> Vec<&str> {
//     let mut in_degree: HashMap<&str, usize> = HashMap::new();
//     for (_, dependencies) in graph.iter() {
//         for &dependency in dependencies {
//             *in_degree.entry(dependency).or_insert(0) += 1;
//         }
//     }
//     let mut queue: VecDeque<&str> = VecDeque::new();
//     for (file, &degree) in in_degree.iter() {
//         if degree == 0 {
//             queue.push_back(file);
//         }
//     }
//     let mut order: Vec<&str> = Vec::new();
//     while let Some(file) = queue.pop_front() {
//         order.push(file);
//         for &dependency in graph.get(file).unwrap() {
//             *in_degree.get_mut(dependency).unwrap() -= 1;
//             if *in_degree.get(dependency).unwrap() == 0 {
//                 queue.push_back(dependency);
//             }
//         }
//     }
//     order
// }

// pub fn compilation_order(files: &[&str], dependencies: &[(&str, &str)]) -> Vec<&str> {
//     let graph = create_graph(files, dependencies);
//     if detect_cycle(&graph) {
//         return Vec::new();
//     }
//     topological_sort(&graph)
// }



// Let's test the implementation using the sample test cases.
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_compile_order() {
        let files = vec!['a', 'b', 'c', 'd'];
        let dependencies = vec![('d', 'a'), ('b', 'a'), ('c', 'b'), ('a', 'c')];
        assert_eq!(compile_order(files, dependencies), vec![]);

        let files = vec!['a', 'b', 'c', 'd'];
        let dependencies = vec![('d', 'a'), ('b', 'a'), ('c', 'd')];
        let result = compile_order(files, dependencies);
        // Valid order: ['a', 'b', 'd', 'c'] or any order that respects dependencies.
        assert!(result.contains(&'a') && result.contains(&'b') && result.contains(&'c') && result.contains(&'d'));
        assert!(result.iter().position(|&r| r == 'a') < result.iter().position(|&r| r == 'b'));
        assert!(result.iter().position(|&r| r == 'a') < result.iter().position(|&r| r == 'd'));
        assert!(result.iter().position(|&r| r == 'c') > result.iter().position(|&r| r == 'd'));
    }
}