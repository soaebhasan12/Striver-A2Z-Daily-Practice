---

# 📝 `Left Rotate By K Insight`

---

# 1️⃣ 🧠 Core Idea

```text
Left rotate by k = first k elements end me shift
```

👉 Target:

```text
[1,2,3,4,5,6], k=2 → [3,4,5,6,1,2]
```

---

# 2️⃣ 🔥 Most Important Insight

```text
Actual k = k % n
```

👉 Reason:

* full rotation useless
* extra work avoid

---

# 3️⃣ 🧩 Approach Thinking

## 🟡 Brute Force (Intuition)

👉 “1 step rotate” ko k times repeat karo

```text
Save first → shift → place at end
```

👉 Problem:

```text
Time = O(n * k) ❌
```

---

## 🟢 Optimal (Reverse Trick)

👉 Direct movement mushkil hai ❌
👉 Reverse karke indirectly place karte hain ✔️

---

# 4️⃣ 🧠 Why Reverse Works

👉 Reverse se:

```text
groups automatically ban jaate hain
```

Example:

```text
[1,2,3,4,5,6]
→ reverse → [6,5,4,3,2,1]
```

👉 Ab:

* `[3,4,5,6]` ka reverse → `[6,5,4,3]`
* `[1,2]` ka reverse → `[2,1]`

👉 Dono already present hain → bas fix karna hai 🔥

---

# 5️⃣ ⚙️ Final Steps

```text
1. Reverse full array
2. Reverse first (n-k)
3. Reverse last k
```

---

# 6️⃣ 🧪 Visualization

```text
[1,2,3,4,5,6], k=2

Step-1 → [6,5,4,3,2,1]
Step-2 → [3,4,5,6,2,1]
Step-3 → [3,4,5,6,1,2]
```

---

# 7️⃣ 🧠 Reverse Logic (Core Concept)

👉 Swap pattern:

```text
0 ↔ n-1
1 ↔ n-2
```

👉 Stop when:

```text
left > right
```

---

# 8️⃣ 💻 Code (Understand, don’t memorize)

```python
class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)

    def reverse(self, nums, start, end):
        left = start
        right = end

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

---

# 9️⃣ ⚠️ Common Mistakes (Your Learnings)

❌ `k = n % k`
✔ `k = k % n`

❌ slicing = in-place
❌ shifting instead of swapping
❌ reverse function scope issue

---

# 🔟 ⏱️ Complexity

```text
Time = O(n)
Space = O(1)
```

---

# 🚩 Interview Signals

👉 Keywords:

* rotate by k
* in-place
* large input

👉 Immediately think:

```text
k % n + reverse trick
```

---

# 🎯 Memory Trick

```text
Reverse all → Fix left → Fix right
```

---

# 🧠 Final Summary

* brute → slow
* reverse → optimal
* swap > shift
* think in blocks, not steps

---