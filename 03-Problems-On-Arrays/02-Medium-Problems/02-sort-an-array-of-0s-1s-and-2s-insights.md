# 📄 Sort an Array of 0s, 1s and 2s Insights

---

## 🧠 Problem Understanding

Given array `nums` jisme sirf:

```
0, 1, 2
```

👉 Task:

```
In-place sort karna hai (no extra array)
```

---

## 🔍 Problem Classification

👉 Signals:

* Limited values (0,1,2)
* Rearrangement / partition
* Sorting without extra space

👉 Possible approaches:

```
Sorting / Counting / Two Pointer (DNF)
```

---

# ⚙️ Approach 1: Brute Force (Sorting)

## 💡 Idea

```
Normal sorting algorithm use karo
```

---

## 🧠 Pseudo Code

```
Sort the array using built-in sort
Return array
```

---

## ⏱️ Complexity

```
Time → O(n log n)
Space → depends
```

---

## 🚫 Problem

* Overkill solution
* Pattern miss ho jata hai ❌

---

# ⚡ Approach 2: Counting (Two Pass)

## 💡 Core Idea

```
Count number of 0s, 1s, 2s
Then overwrite array
```

---

## 🧠 Pseudo Code

```
Initialize count0, count1, count2 = 0

Loop array:
    count values

idx = 0

Fill 0 count times:
    nums[idx] = 0
    idx++

Fill 1 count times:
    nums[idx] = 1
    idx++

Fill 2 count times:
    nums[idx] = 2
    idx++
```

---

## 🔥 Dry Run

```
nums = [1,0,2,1,0]
```

### Count phase:

```
count0 = 2
count1 = 2
count2 = 1
```

---

### Fill phase:

```
Index: 0 1 2 3 4
Array: [0 0 1 1 2]
```

---

## ⏱️ Complexity

```
Time → O(n)
Space → O(1)
```

---

## ⚠️ Important Concept

👉 `idx` pointer:

```
Next position jahan likhna hai
```

---

# 🚀 Approach 3: Optimal (Dutch National Flag)

## 💡 Core Idea

```
3 partitions maintain karo:

0 → left side
1 → middle
2 → right side
```

---

## 🧠 Pseudo Code

```
low = 0
mid = 0
high = n-1

while mid <= high:

    if nums[mid] == 0:
        swap(low, mid)
        low++
        mid++

    else if nums[mid] == 1:
        mid++

    else:
        swap(mid, high)
        high--
```

---

## 🔥 Dry Run (VERY IMPORTANT ⭐)

```
nums = [2,0,1]
```

```
low=0 mid=0 high=2
```

---

### Step 1:

```
nums[mid] = 2
swap(mid, high)

[1,0,2]
high = 1
```

---

### Step 2:

```
nums[mid] = 1
mid++
```

---

### Step 3:

```
nums[mid] = 0
swap(low, mid)

[0,1,2]
low++, mid++
```

---

## ⏱️ Complexity

```
Time → O(n)
Space → O(1)
Single pass ✅
```

---

# ⚠️ Beginner Mistakes (VERY IMPORTANT 🚨)

## ❌ Mistake 1: Wrong iteration

```
for i in nums:
    nums[i]
```

👉 Value ko index treat kar diya ❌

---

## ❌ Mistake 2: While loop misuse

```
while count0 > 0:
```

👉 Same index overwrite ho raha tha ❌

---

## ❌ Mistake 3: idx increment before assignment

```
idx += 1
nums[idx] = X
```

👉 First index skip ho gaya ❌

---

## ❌ Mistake 4: Infinite loop

```
while n >= 0
```

👉 n change hi nahi ho raha ❌

---

# 🔁 Future Mistakes (1 Month Later 🚩)

👉 Tu ye mistakes dobara karega:

* ❌ `for i in nums` vs `range(len(nums))` confusion
* ❌ pointer movement bhool jayega (low/mid/high)
* ❌ swap ke baad mid increment kab karna hai bhool jayega
* ❌ idx ka role confuse hoga

---

# 🧠 Memory Tricks

### Counting approach:

```
Count → Fill → Done
```

---

### DNF approach:

```
0 → left
1 → skip
2 → right
```

---

# 🚩 Interview Signals

👉 Agar interviewer bole:

* “in-place sort”
* “only 0,1,2”
* “single pass?”

👉 Direct signal:

```
DNF Algorithm 🔥
```

---

# 🎯 Comparison Table

| Approach | Time    | Pass     | Idea         |
| -------- | ------- | -------- | ------------ |
| Brute    | n log n | multiple | sorting      |
| Counting | n       | 2 pass   | count + fill |
| DNF      | n       | 1 pass   | partition    |

---

# 📘 Revision Points

* Limited values → counting ya DNF
* idx → next write position
* DNF → 3 pointers (low, mid, high)
* swap logic clear hona chahiye

---

# 🎤 Interview Answer (Short)

👉 “We can solve this using Dutch National Flag algorithm in O(n) time and O(1) space by maintaining three pointers for 0s, 1s, and 2s partitions.”

---

# 🧠 FINAL SUMMARY

* Brute → easy but slow
* Counting → simple and clean
* DNF → best (single pass)
* Pointer movement = key 🔥

---

# 🚀 Challenge 😏

👉 Batao:

👉 DNF me jab `nums[mid] == 2` hota hai:

👉 **mid increment kyu nahi karte?**

👉 Yeh samajh gaya → expert level pe aa gaya 💀
