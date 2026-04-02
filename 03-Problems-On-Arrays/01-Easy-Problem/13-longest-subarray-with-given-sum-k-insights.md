# 📄 Longest Subarray With Given Sum k Insights

---

## 🧠 Problem Understanding

Given an array `nums` and integer `k`, find the **length of longest subarray** whose sum = `k`.

👉 Subarray = continuous elements

---

## 🔍 Key Insight

```

We are not checking all subarrays manually,
we are converting problem into prefix sum problem.

````

---

# ⚙️ Approach 1: Brute Force (Nested Loop)

## 💡 Idea

- Start from every index
- Try all possible subarrays
- Keep calculating sum

---

## 🧪 Code

```python
for i in range(n):
    curr_sum = 0
    for j in range(i, n):
        curr_sum += nums[j]
        if curr_sum == k:
            max_len = max(max_len, j - i + 1)
````

---

## ⏱️ Time Complexity

```
O(n²)
```

---

## 🚫 Problems

* Slow for large inputs
* Repeated calculations
* Not optimal

---

# ⚡ Approach 2: Optimal (Prefix Sum + HashMap)

## 💡 Core Idea

```
If current_sum - k exists before,
then subarray between them has sum k
```

---

## 🧠 Logic Breakdown

### Step 1: Maintain running sum

```
curr_sum += nums[i]
```

---

### Step 2: Case 1 → From index 0

```
if curr_sum == k:
    length = i + 1
```

---

### Step 3: Case 2 → Using hashmap

```
if (curr_sum - k) in map:
    length = i - map[curr_sum - k]
```

---

### Step 4: Store prefix sum

```
if curr_sum not in map:
    map[curr_sum] = i
```

👉 Store only first occurrence (important)

---

## 🧪 Code

```python
class Solution:
    def longestSubarray(self, nums, k):
        prefix_map = {}
        curr_sum = 0
        max_len = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum == k:
                max_len = i + 1

            if (curr_sum - k) in prefix_map:
                length = i - prefix_map[curr_sum - k]
                max_len = max(max_len, length)

            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i

        return max_len
```

---

## ⏱️ Time Complexity

```
O(n)
```

---

## 📦 Space Complexity

```
O(n)
```

---

# 🔥 Dry Run Insight

Example:

```
nums = [10, 5, 2, 7, 1, 9]
k = 15
```

👉 Longest subarray:

```
[5, 2, 7, 1] → length = 4
```

---

# 🧠 Important Observations

* Prefix sum converts problem into lookup problem
* HashMap stores previous sums
* First occurrence store karna important hai (max length ke liye)

---

# 🧠 Memory Trick

```
current_sum - k → check map
```

---

# ⚠️ Common Mistakes

* ❌ Map me overwrite kar dena
* ❌ curr_sum == k case miss karna
* ❌ length formula galat likhna

---

# 🎯 Final Insight

```
Brute force → try all subarrays
Optimal → use math (prefix sum)
```

---

# 🧠 Summary

* Problem can be optimized using prefix sum
* HashMap helps in O(1) lookup
* Two cases:

  1. From index 0
  2. From previous prefix

---

# 🚀 Interview Point

👉 “We use prefix sum + hashmap to reduce time complexity from O(n²) to O(n)”

---
