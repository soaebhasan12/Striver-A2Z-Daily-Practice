# 📄 Next Permutation Insights

---

## 🧠 Problem Understanding

Given array `nums`:

👉 Find:

```text
Next lexicographically greater permutation
```

👉 Agar possible nahi:

```text
Return smallest permutation (sorted ascending)
```

---

## 🔍 Problem Classification

👉 Signals:

* Permutation
* Lexicographical order
* Rearrangement in-place

👉 Pattern:

```text
Greedy + Observation + Reverse
```

---

# 🧠 1️⃣ Intuition (MOST IMPORTANT ⭐)

👉 Soch:

```text
Hume next “bada” number banana hai using same digits
```

---

## 🔥 Example:

```text
[1,2,3] → [1,3,2]
[1,3,2] → [2,1,3]
```

---

## 💡 Golden Observation

👉 Right side pe focus karo:

```text
Left part stable hota hai
Right part change hota hai
```

---

## ❗ Special Case

```text
[3,2,1] → no bigger permutation
→ answer = [1,2,3]
```

---

# 🧠 2️⃣ Core Idea (3 Steps)

```text
1. Breakpoint find karo
2. Swap karo
3. Reverse suffix
```

---

# ⚙️ Step-by-Step Breakdown

---

## 1️⃣ Breakpoint Find

👉 Right se pehla index jahan:

```text
nums[i] < nums[i+1]
```

---

### Example:

```text
[1,2,3]
     ↑ breakpoint (2 < 3)
```

---

## 2️⃣ Swap

👉 Right side se next greater element dhundo

```text
[1,2,3] → swap 2 with 3 → [1,3,2]
```

---

## 3️⃣ Reverse Suffix

👉 Right part ko ascending bana do

```text
[1,3,2] → already sorted suffix
```

---

# 🔥 Dry Run (VERY IMPORTANT ⭐)

```text
nums = [2,1,5,4,3,0,0]
```

---

### Step 1: Breakpoint

```text
1 < 5 → index = 1
```

---

### Step 2: Swap

```text
swap 1 with 3 → [2,3,5,4,1,0,0]
```

---

### Step 3: Reverse

```text
[2,3,0,0,1,4,5]
```

---

# ⚡ Approach 1: Brute Force

## 💡 Idea

```text
Generate all permutations
→ sort
→ find next
```

---

## 🧠 Pseudo Code

```text
Generate all permutations
Sort them
Find current index
Return next index
```

---

## 🧪 Code (Beginner Friendly)

```python
from itertools import permutations

def nextPermutation(nums):
    perms = list(permutations(nums))
    perms = [list(p) for p in perms]
    
    perms.sort()
    
    for i in range(len(perms)):
        if perms[i] == nums:
            if i+1 < len(perms):
                return perms[i+1]
            else:
                return perms[0]
```

---

## ⏱️ Complexity

```text
O(n! * n) ❌
```

---

# 🚀 Approach 2: Optimal

## 💡 Core Idea

```text
Right se smallest increase karo
```

---

## 🧠 Pseudo Code

```text
Find breakpoint from right

If found:
    find next greater element
    swap

Reverse remaining part
```

---

## ⏱️ Complexity

```text
Time → O(n)
Space → O(1)
```

---

# ⚠️ Beginner Mistakes 🚨

## ❌ Mistake 1: Reverse wrong likhna

```text
sirf ek swap kar dena ❌
```

---

## ❌ Mistake 2: Breakpoint samajh na aana

👉 Direction galat le lena (left se search ❌)

---

## ❌ Mistake 3: Next greater galat choose karna

👉 smallest greater choose karna hota hai

---

## ❌ Mistake 4: Reverse bhool jana

👉 output incorrect ho jayega ❌

---

## ❌ Mistake 5: Edge case ignore

```text
[3,2,1] → reverse full array
```

---

# 🧠 Memory Tricks

```text
Right → Break → Swap → Reverse
```

---

# 🚩 Interview Signals

👉 Agar interviewer bole:

* “next permutation”
* “lexicographically next”
* “in-place”

👉 Direct signal:

```text
Greedy + Reverse pattern 🔥
```

---

# 🎯 Comparison Table

| Approach | Time | Idea         |
| -------- | ---- | ------------ |
| Brute    | n!   | generate all |
| Optimal  | n    | greedy       |

---

# 📘 Revision Points

* Right se breakpoint
* Swap with next greater
* Reverse suffix
* Edge case → full reverse

---

# 🎤 Interview Answer (Short)

👉 “We find a breakpoint from the right, swap it with the next greater element, and reverse the suffix to get the next permutation in O(n) time.”

---

# 🧠 FINAL SUMMARY

* Next permutation = next bigger arrangement
* Right side important hai
* Reverse = smallest suffix

---

# 🚀 Next Thinking

👉 Agar kth permutation nikalna ho…

👉 kaise karoge? 🤔

---