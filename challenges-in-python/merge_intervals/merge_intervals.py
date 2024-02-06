# Solving the "Merge Intervals" Challenge
# Challenge Description:
# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, 
# and return an array of the non-overlapping intervals 
# that cover all the intervals in the input.

# Approach:
# Sort the intervals based on their start times.
# Iterate through the intervals, and if an interval 
# overlaps with the previous one (its start time is less than or equal 
# to the end time of the previous interval), merge them. Otherwise, add it to the output.

def merge(intervals: list[list[int]]) -> list[list[int]]:
    # if intervals is empty return empty list
    if not intervals:
        return []
    
    # Sort the intervals based on their start times
    intervals.sort(key=lambda x: x[0])

    # Initialize merged list with the first interval
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        # if the current interval overlaps with the last merged interval
        # merge them by updating the end time of the previous interval
        if intervals[i][0] <= merged[-1][1]:
            # merge them by updating the end time of the previous interval
            merged[-1][1] = max(intervals[i][1], merged[-1][1])
        else:
            # add it to the output
            merged.append(intervals[i])
    
    return merged

# Testing the function
def test_merge():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    assert merge([[1,4],[5,6]]) == [[1,4], [5,6]]
    # empty list
    assert merge([]) == []
    # single interval
    assert merge([[1,4]]) == [[1,4]]

test_merge()