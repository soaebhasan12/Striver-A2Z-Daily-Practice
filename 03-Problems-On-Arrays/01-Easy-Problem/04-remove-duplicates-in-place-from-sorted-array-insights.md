# 📘 Remove Duplicates Insight

## 1️⃣ Core Idea (Two Pointer Pattern)

```
i → last unique element
j → next element to explore
```

👉 Memory line:

```
Find new → move i → place element
```

---

## 2️⃣ Algorithm Thinking

👉 Start:

```
i = 0
j runs from 1 → n-1
```

👉 Condition:

```
if nums[j] != nums[i]
```

👉 Action:

```
move i
place nums[j] at nums[i]
```

---

## 3️⃣ Key Insight (Most Important)

👉 `i` always points to:

```
last unique element
```

👉 Left side:

```
[0 → i] = unique elements
```

👉 Right side:

```
[i+1 → end] = irrelevant
```

---

## 4️⃣ Visualization

```
[1,1,2,2,3]

Step:
i=0

j=1 → skip
j=2 → new → i=1 → place 2
j=3 → skip
j=4 → new → i=2 → place 3
```

Final:

```
[1,2,3,_,_]
```

---

## 5️⃣ Return Logic (Exam Trap 🚨)

👉 `i` = last index
👉 answer =

```
i + 1
```

---

## 6️⃣ Common Mistakes

❌ using `i+1` while placing
❌ returning array instead of count
❌ forgetting sorted property
❌ off-by-one error (very common)

---

## 7️⃣ Pattern Recognition (IMPORTANT 🔥)

👉 Ye question belongs to:

```
Two Pointer → In-place array modification
```

👉 Future me similar problems:

* remove duplicates II
* move zeroes
* remove element
* compress string

---

## 🎯 Final Memory Trick

```
Slow pointer = unique tracker
Fast pointer = explorer
```

---