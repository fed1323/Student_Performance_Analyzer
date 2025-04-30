# 🎓 Student Score Insights

This project analyzes the **Students Performance in Exams** dataset using Python's functional programming tools (`map`, `filter`, and `lambda`) and builds an interactive web dashboard using **Streamlit**.

## 📂 Dataset

We use the **Students Performance in Exams** dataset, which includes:
- Gender
- Race/ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Math score
- Reading score
- Writing score

📌 [Download Dataset from Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

---

## 🚀 Features

- Clean and preprocess the dataset
- Use `filter()` to select students based on specific criteria
- Use `map()` to apply calculations (like average scores) to each student
- Use `lambda` functions for quick and readable inline operations
- Display results and visualizations using **Streamlit**

---

## 🛠️ How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/student-score-insights.git
   cd student-score-insights

# `lambda`

## 📌What is `lambda` in Python?

A `lambda` function is an **anonymous (nameless)** function in Python. It's used when you need a **simple, short function** and don't want to formally define it using `def`.

### 🔧 Syntax:

```python
lambda arguments: expression
```

### ✅ Example:
```python
square = lambda x: x * x
print(square(5))  # Output: 25
```
This is the same as:
```python
def square(x):
    return x * x
```

### 💡 Use Cases:
- Used with functions like `map()`, `filter()`, `sorted()`, etc.
- Best for short, one-line functions.


# `map()`

## 📌 What is `map()` in Python?

`map()` applies a **function** to **every item** in an iterable (like a list or tuple).

### 🔧 Syntax:
```python
map(function, iterable)
```

### ✅ Example 1 — with `lambda`:
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8]
```

### ✅ Example 2 — with a defined function:
```python
def square(x):
    return x * x

nums = [1, 2, 3]
squared = list(map(square, nums))
print(squared)  # Output: [1, 4, 9]
```

---
# `filter()`

## 📌 What is `filter()` in Python?

`filter()` is used to **filter items** from an iterable using a **condition (function)** that returns `True` or `False`.

### 🔧 Syntax:
```python
filter(function, iterable)
```

### ✅ Example:
```python
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # Output: [2, 4]
```

### ✅ Another Example:
```python
def is_positive(n):
    return n > 0

nums = [-3, 1, 0, 5, -1]
positive_nums = list(filter(is_positive, nums))
print(positive_nums)  # Output: [1, 5]
```

---

