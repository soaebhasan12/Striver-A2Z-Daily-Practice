# 📄 Find the Majority Element (> n/2 times) Insights


## 🧠 Problem Understanding

Given array `nums`:

👉 Find element jo:

```id="n3j5ks"
frequency > n/2
```

👉 Guaranteed:

```id="x9q2kz"
always ek majority element exist karega
```

---

## 🔍 Problem Classification

👉 Signals:

* Frequency based problem
* “more than n/2” condition
* Majority guaranteed

👉 Possible approaches:

```id="kz8w2p"
Hashing / Voting Algorithm
```

---

# ⚙️ Approach 1: Hashing (Frequency Count)

## 💡 Idea

```id="c9b8t7"
Har element ka count store karo
Phir check karo kaun > n/2 hai
```

---

## 🧠 Pseudo Code

```id="f4m1kq"
Initialize empty map

Loop array:
    increase frequency

Loop map:
    if freq > n/2:
        return element
```

---

## 🔥 Dry Run

```id="k1x9op"
nums = [1,1,1,2,1,2]
```

### Map:

```id="d3v8re"
{1:4, 2:2}
```

👉 Check:

```id="n2p7bz"
4 > 6/2 → YES
```

👉 Answer:

```id="u7q3wa"
1
```

---

## ⏱️ Complexity

```id="y7n2xa"
Time → O(n)
Space → O(n)
```

---

## ⚠️ Insight

👉 Fast but extra space use karta hai ❌

---

# 🚀 Approach 2: Moore’s Voting Algorithm (Optimal)

## 💡 Core Idea

```id="z8q2lm"
Majority element kabhi completely cancel nahi hota
```

👉 Pair-wise cancellation logic 🔥

---

## 🧠 Pseudo Code

```id="b7x4ks"
candidate = None
count = 0

Loop array:

    if count == 0:
        candidate = current
        count = 1

    else if current == candidate:
        count++

    else:
        count--
        
Return candidate
```

---

## 🔥 Dry Run (VERY IMPORTANT ⭐)

```id="r2y7qp"
nums = [2,2,1,1,1,2,2]
```

---

### Step Flow:

```id="c6z3xa"
2 → new → (2,1)
2 → same → (2,2)
1 → diff → (2,1)
1 → diff → (2,0) ❗ cancel
1 → new → (1,1)
2 → diff → (1,0) ❗ cancel
2 → new → (2,1)
```

👉 Final candidate:

```id="g5p1mn"
2
```

---

## ⏱️ Complexity

```id="a9k2lw"
Time → O(n)
Space → O(1)
```

---

## ⚠️ Important Concept

👉 Cancellation effect:

```id="y2z8qa"
same → +1
different → -1
```

---

# ⚠️ Beginner Mistakes (VERY IMPORTANT 🚨)

## ❌ Mistake 1: Wrong comparison

```id="h3k8az"
if count == nums[i]
```

👉 count vs value compare kar diya ❌

---

## ❌ Mistake 2: Candidate update galat

```id="w4v9nx"
candidate += 1
```

👉 candidate value hai, counter nahi ❌

---

## ❌ Mistake 3: count update bhool gaye

```id="m7p2kx"
if count == 0:
    candidate = nums[i]
```

👉 count = 1 karna bhool gaye ❌

---

## ❌ Mistake 4: Wrong return

```id="p6z8qa"
return count
```

👉 element return karna hota hai ❌

---

# 🔁 Future Mistakes (1 Month Later 🚩)

👉 Tum likely yeh galti karega:

* ❌ candidate vs nums[i] comparison bhool jayega
* ❌ count reset logic miss karega
* ❌ “why it works” bhool jayega
* ❌ verification step (non-guaranteed case) ignore karega

---

# 🧠 Memory Tricks

```id="t2w8qs"
Zero → new candidate
Same → +1
Different → -1
```

---

# 🚩 Interview Signals

👉 Agar interviewer bole:

* “majority element”
* “> n/2”
* “optimize space”

👉 Direct signal:

```id="x7q9wr"
Moore’s Voting Algorithm 🔥
```

---

# 🎯 Comparison Table

| Approach | Time | Space | Idea         |
| -------- | ---- | ----- | ------------ |
| Hashing  | n    | n     | count freq   |
| Moore    | n    | 1     | cancel pairs |

---

# 📘 Revision Points

* Majority → freq > n/2
* Hashmap → easy but space heavy
* Moore → best (O(1) space)
* Candidate ≠ count

---

# 🎤 Interview Answer (Short)

👉 “We can solve this using Boyer-Moore Voting Algorithm in O(n) time and O(1) space by canceling out non-majority elements.”

---

# 🧠 FINAL SUMMARY

* Brute → unnecessary
* Hashing → simple
* Moore → optimal
* Cancellation logic = key 🔥

---

# 🚀 Next Level Thinking

👉 Agar majority guarantee **na ho**…

👉 kya Moore direct answer dega? 🤔

👉 YES / NO ?
