# 📝 `Move Zeroes Insights`

---

# 1️⃣ 🧠 Core Idea

```text
All non-zero → front
All zero → end (automatically)
```

👉 Order maintain karna hai (important)

---

# 2️⃣ 🧩 Pattern Recognition

```text
Two Pointer (Slow-Fast)
```
```
* j → traverse (fast)
* i → place non-zero (slow)
```
---

# 3️⃣ 🔥 Intuition

👉 Socho:

```text
[0,1,4,0,5,2]
```

👉 Goal:

```text
[1,4,5,2,_,_]
```

👉 Strategy:

```text
non-zero milte hi → front me push
zero → ignore
```

---

# 4️⃣ ⚙️ Key Logic

```text
if nums[j] != 0:
    swap(nums[i], nums[j])
    i++
```
```
👉 swap = safe movement
👉 overwrite = data loss ❌
```
---

# 5️⃣ 🧪 Visualization

```text
Index:  0 1 2 3 4 5
Array: [0 1 4 0 5 2]

Step:
j=1 → swap → [1 0 4 0 5 2]
j=2 → swap → [1 4 0 0 5 2]
j=4 → swap → [1 4 5 0 0 2]
j=5 → swap → [1 4 5 2 0 0]
```

---

# 6️⃣ ⚠️ Common Mistakes (YOUR LEARNINGS)
```
❌ checking `nums[i]` instead of `nums[j]`
❌ overwrite instead of swap
❌ wrong swap logic
❌ starting j from 1 (skip issue)
```
---

# 7️⃣ ⏱️ Complexity

```text
Time = O(n)
Space = O(1)
```
```
👉 single traversal
👉 no extra space
```
---

# 8️⃣ 🚩 Interview Signals

👉 Agar aaye:
```
* “move zeros”
* “maintain order”
* “in-place”
```
👉 Think:

```text
Two Pointer + Swap
```

---

# 9️⃣ 🎯 Memory Trick

```text
Find non-zero → bring forward → done
```

---

# 🔟 🧠 Final Summary
```
* j → scan
* i → place
* swap → move safely
* zero → ignore
```
---

# 💬 My Opinion

👉 Ye problem:

🔥 **Two Pointer mastery ka entry point hai**

👉 Agar ye clear hai:
```
→ remove duplicates
→ partition
→ Dutch flag
```
sab easy ho jayega 🚀
