since array is sorted, we can perform binary search to find any instance of target
once we find the target value, we perform another binary search where we increment our
*left* pointer and decrement our *right* pointer whenever the value at that index != the target
- since we increment/decrement the left and right pointer whenever the value != the target, we can assume that it'll **only** increment/decrement whenever the value != target so the left pointer will always stop at the first index and the right will always stop at the last index