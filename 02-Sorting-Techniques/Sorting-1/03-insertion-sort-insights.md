# 📘 Insertion Sort – Key Insights

## 1️⃣ Core Idea

Insertion Sort builds the sorted array **one element at a time** by inserting the current element into its correct position in the already sorted part of the array.

Memory anchor:

```
Shift → Insert → Sorted portion grows
```

Har step me **current element ko correct position par insert kiya jata hai**.

---

# 2️⃣ Algorithm Intuition

Array gradually divide hota hai:

```
Left  → Sorted
Right → Unsorted
```

Example

```
[7,4,1,5,3]

Step 1
[7] | [4,1,5,3]

Step 2
[4,7] | [1,5,3]

Step 3
[1,4,7] | [5,3]

Step 4
[1,4,5,7] | [3]
```

Left side ka **sorted portion continuously grow karta hai**.

---

# 3️⃣ Loop Structure (Important)

Outer loop:

```
Start from index 1 → len(nums)-1
```

Reason:

```
First element already sorted hota hai.
```

Inner loop idea:

```
Move left while elements are larger than key.
```

Condition:

```
while j >= 0 and key < nums[j]
```

---

# 4️⃣ Key Concept (Important)

Insertion sort me current element ko **key** bola jata hai.

```
key = nums[i]
```

Comparison hota hai:

```
key vs nums[j]
```

Agar left element bada hai:

```
shift element right
```

---

# 5️⃣ Shifting Pattern

Insertion sort **swap use nahi karta**.

Instead:

```
nums[j+1] = nums[j]
```

Meaning:

```
larger element ko right move karo
```

Example

```
[7,4,1]

Insert 1

[7,4,7]
[7,4,4]
[1,4,7]
```

---

# 6️⃣ Insert Position

Loop stop hone par correct position hoti hai:

```
nums[j+1] = key
```

Reason:

```
j last index represent karta hai jahan element key se chhota tha.
```

Isliye insertion always hota hai:

```
j + 1
```

---

# 7️⃣ Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n)       |
| Average | O(n²)      |
| Worst   | O(n²)      |

Reason:

```
Worst case me har element ko poore sorted part me shift karna padta hai.
```

Example worst case:

```
[5,4,3,2,1]
```

---

# 8️⃣ Space Complexity

```
O(1)
```

Reason:

```
In-place sorting
```

Extra memory use nahi hoti.

---

# 9️⃣ Important Observations

1️⃣ Sorting left side se build hoti hai
2️⃣ Elements swap nahi hote — shift hote hain
3️⃣ Key ko correct position par insert kiya jata hai
4️⃣ Nearly sorted arrays me algorithm fast hota hai

Correct mental pattern:

```
Take element → Shift larger elements → Insert key
```

---

# 🔟 Memory Shortcut

```
Insertion Sort =
Insert element into sorted part
```

Or simply:

```
Shift → Insert → Repeat
```

---

# 🎯 One-Line Interview Explanation

Insertion sort repeatedly takes the next element and **inserts it into its correct position in the already sorted portion of the array** by shifting larger elements to the right.

---
