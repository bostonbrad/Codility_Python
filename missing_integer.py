"""
Task: MissingInteger
Goal: Find the smallest positive integer that does not occur in a given sequence.
Website: https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
-----------------------------------------------------------
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
"""

def solution(A):
    if max(A) > -1:
        largest = max(A)
        my_list = list(range(1,largest+2))
        for number in my_list:
            if number not in A:
                return number
                break
            
    else:
        return 1
