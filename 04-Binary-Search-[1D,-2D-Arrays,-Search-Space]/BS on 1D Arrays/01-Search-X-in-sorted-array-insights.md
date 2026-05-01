# 01 - Search X in Sorted Array (Binary Search Insights)

---

## 1. Problem Overview

Given a **sorted array**, the task is to find the index of a target element. If the element is not present, return `-1`.

This is the most basic and important Binary Search problem and builds the foundation for all advanced variations.

---

## 2. Why Binary Search?

### Brute Force

* Check each element one by one
* Time Complexity: O(n)

### Optimized Approach

* Use sorted property
* Reduce search space by half each step
* Time Complexity: O(log n)

---

## 3. Core Intuition

Binary Search is based on one simple decision:

* Compare target with middle element
* Decide direction:

  * Go left → if target is smaller
  * Go right → if target is larger

Each step eliminates half of the remaining search space.

---

## 4. Search Space Thinking (Most Important Concept)

Always think in terms of a **range**, not the entire array:

Search Space = [low, high]

* Initial range:

  * low = 0
  * high = n - 1

* After each comparison:

  * Either left half survives
  * Or right half survives

Binary Search is fundamentally about **shrinking this range**.

---

## 5. Pseudo Code (Iterative)

```
Initialize low = 0
Initialize high = n - 1

While low <= high:
    mid = (low + high) // 2

    If nums[mid] == target:
        return mid

    Else if target > nums[mid]:
        move to right half
        low = mid + 1

    Else:
        move to left half
        high = mid - 1

Return -1
```

---

## 6. Pseudo Code (Recursive)

```
Function BinarySearch(nums, low, high, target):

    If low > high:
        return -1

    mid = (low + high) // 2

    If nums[mid] == target:
        return mid

    Else if target > nums[mid]:
        search in right half
        return BinarySearch(nums, mid+1, high, target)

    Else:
        search in left half
        return BinarySearch(nums, low, mid-1, target)
```

---

## 7. Dry Run Strategy (How to Practice Properly)

Do not try to track everything.

Only track:

(low, high) → mid → decision

Example:

nums = [-1,0,3,5,9,12], target = 9

Step 1:
(0,5) → mid=2 → value=3 → go right

Step 2:
(3,5) → mid=4 → value=9 → found

---

## 8. Common Mistakes (Very Important)

### 1. Wrong High Initialization

* Using `high = len(nums)` instead of `len(nums) - 1`
* Leads to invalid index access

---

### 2. Infinite Loop

* Not updating low or high correctly
* Wrong loop condition

---

### 3. Not Understanding Search Space

* Thinking in terms of elements instead of range
* Binary search is about shrinking boundaries

---

### 4. Mixing Slicing with Indices

* Using subarrays and still tracking original indices
* Causes mismatch and incorrect results

---

### 5. Off-by-One Errors

* Very common in binary search
* Happens when adjusting low/high incorrectly

---

### 6. Confusion During Dry Run

* Trying to track entire array every step
* Not writing steps clearly

---

### 7. Weak Base Case Understanding (Recursion)

* Forgetting `low > high` condition
* Leads to infinite recursion

---

## 9. Edge Cases

| Case               | Expected         |
| ------------------ | ---------------- |
| Empty array        | Return -1        |
| Single element     | Direct check     |
| Target not present | Return -1        |
| Target at start    | Handle correctly |
| Target at end      | Handle correctly |

---

## 10. Complexity

| Type              | Value    |
| ----------------- | -------- |
| Time              | O(log n) |
| Space (Iterative) | O(1)     |
| Space (Recursive) | O(log n) |

---

## 11. Pattern Recognition

This problem belongs to:

* Binary Search (Exact Match)
* Divide and Conquer

### Signals:

* Sorted array
* Need faster than linear search
* Direct element lookup

---

## 12. Interview Perspective

### What is expected:

* Correct binary search template
* No off-by-one errors
* Clear dry run explanation
* Understanding of why it works

### Possible follow-ups:

* First occurrence
* Last occurrence
* Lower bound / upper bound
* Rotated sorted array

---

## 13. Mental Model

Think like this:

“I am reducing a search range step by step.”

Not:

“I am checking random elements.”

---

## 14. Revision Notes (Memory Friendly)

* low = 0, high = n - 1
* Loop until low <= high
* mid = (low + high) // 2
* Right → low = mid + 1
* Left → high = mid - 1
* Not found → return -1

---

## 15. Final Takeaway

Binary Search is not about remembering code.

It is about:

* Understanding range reduction
* Making correct decisions
* Avoiding small logical mistakes

Once this is clear, advanced binary search problems become much easier to solve.

---
