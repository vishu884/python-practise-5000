# 🐍 Python Complete Notes

A deep, structured reference covering Python fundamentals — from variables to string slicing. Perfect for revision, GitHub portfolio, or teaching.

---

## 📑 Table of Contents

1. [Variables](#1-variables)
2. [Data Types](#2-data-types)
3. [Type Conversion](#3-type-conversion)
4. [Type Casting](#4-type-casting)
5. [Input / Output](#5-input--output)
6. [print() Formatting](#6-print-formatting)
7. [f-strings](#7-f-strings)
8. [Arithmetic Operators](#8-arithmetic-operators)
9. [Comparison Operators](#9-comparison-operators)
10. [Logical Operators](#10-logical-operators)
11. [Assignment Operators](#11-assignment-operators)
12. [Bitwise Operators](#12-bitwise-operators)
13. [Identity Operators](#13-identity-operators)
14. [Membership Operators](#14-membership-operators)
15. [if / elif / else](#15-if--elif--else)
16. [Nested Conditions](#16-nested-conditions)
17. [for Loop](#17-for-loop)
18. [while Loop](#18-while-loop)
19. [break / continue / pass](#19-break--continue--pass)
20. [range()](#20-range)
21. [Nested Loops](#21-nested-loops)
22. [String Methods](#22-string-methods)
23. [String Indexing](#23-string-indexing)
24. [String Slicing](#24-string-slicing)

---

## 1. Variables

A variable is a name used to store data in memory. Python is **dynamically typed** — you don't declare a type, it's inferred at runtime.

```python
name = "Alex"       # string
age = 25             # integer
height = 5.9         # float
is_student = True    # boolean

# Multiple assignment
x, y, z = 1, 2, 3

# Same value to multiple variables
a = b = c = 10
```

**Rules for naming variables:**
- Must start with a letter or underscore (`_`), not a digit
- Can contain letters, digits, underscores
- Case-sensitive (`age` ≠ `Age`)
- Cannot use Python keywords (`if`, `for`, `class`, etc.)

---

## 2. Data Types

| Category | Type | Example |
|---|---|---|
| Numeric | `int`, `float`, `complex` | `10`, `3.14`, `2+3j` |
| Text | `str` | `"hello"` |
| Sequence | `list`, `tuple`, `range` | `[1,2]`, `(1,2)`, `range(5)` |
| Mapping | `dict` | `{"a": 1}` |
| Set | `set`, `frozenset` | `{1,2,3}` |
| Boolean | `bool` | `True`, `False` |
| Binary | `bytes`, `bytearray`, `memoryview` | `b"abc"` |
| None | `NoneType` | `None` |

```python
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hi"))      # <class 'str'>
print(type([1,2,3]))   # <class 'list'>
```

---

## 3. Type Conversion

**Implicit** conversion — Python automatically converts one data type to another without user involvement, usually to avoid data loss.

```python
a = 5        # int
b = 2.5      # float
c = a + b    # int automatically converted to float
print(c)     # 7.5
print(type(c))  # <class 'float'>
```

---

## 4. Type Casting

**Explicit** conversion — the programmer manually converts one type to another using functions like `int()`, `float()`, `str()`, `bool()`, `list()`.

```python
x = "10"
y = int(x)        # string → int
z = float(x)      # string → float

num = 5
text = str(num)   # int → string

lst = list("abc") # string → list => ['a', 'b', 'c']

print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False
print(bool("hi"))  # True
```

⚠️ Casting invalid values raises errors: `int("abc")` → `ValueError`.

---

## 5. Input / Output

```python
# Output
print("Hello, World!")

# Input — always returns a string
name = input("Enter your name: ")
age = int(input("Enter your age: "))   # cast to int

print("Name:", name, "Age:", age)
```

---

## 6. print() Formatting

```python
print("A", "B", "C")                     # A B C
print("A", "B", "C", sep="-")            # A-B-C
print("Hello", end=" ")                  # no newline after
print("World")                            # Hello World

# % formatting (old style)
name = "Tom"
print("Name: %s" % name)

# .format() method
print("Name: {}".format(name))
print("Name: {0}, Age: {1}".format(name, 25))
```

---

## 7. f-strings

Introduced in Python 3.6 — the fastest, cleanest way to embed expressions inside strings.

```python
name = "Sara"
age = 21

print(f"My name is {name} and I am {age} years old.")

# Expressions inside f-strings
print(f"Next year I will be {age + 1}")

# Formatting numbers
pi = 3.14159
print(f"Pi rounded: {pi:.2f}")     # Pi rounded: 3.14

# Padding & alignment
print(f"{name:>10}")   # right aligned in 10 spaces
print(f"{name:<10}|")  # left aligned
print(f"{name:^10}|")  # center aligned
```

---

## 8. Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `5 + 2 = 7` |
| `-` | Subtraction | `5 - 2 = 3` |
| `*` | Multiplication | `5 * 2 = 10` |
| `/` | Division (float) | `5 / 2 = 2.5` |
| `//` | Floor Division | `5 // 2 = 2` |
| `%` | Modulus (remainder) | `5 % 2 = 1` |
| `**` | Exponent (power) | `5 ** 2 = 25` |

---

## 9. Comparison Operators

Return `True` or `False`.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

```python
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True
```

---

## 10. Logical Operators

| Operator | Meaning |
|---|---|
| `and` | True if both are True |
| `or` | True if at least one is True |
| `not` | Reverses the boolean value |

```python
a, b = True, False
print(a and b)   # False
print(a or b)    # True
print(not a)     # False
```

---

## 11. Assignment Operators

| Operator | Example | Same as |
|---|---|---|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=`, `\|=`, `^=`, `>>=`, `<<=` | Bitwise assignment | — |

---

## 12. Bitwise Operators

Work on the binary representation of integers.

| Operator | Meaning | Example |
|---|---|---|
| `&` | AND | `5 & 3 = 1` |
| `\|` | OR | `5 \| 3 = 7` |
| `^` | XOR | `5 ^ 3 = 6` |
| `~` | NOT | `~5 = -6` |
| `<<` | Left Shift | `5 << 1 = 10` |
| `>>` | Right Shift | `5 >> 1 = 2` |

```python
a = 5   # 0101
b = 3   # 0011
print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6
```

---

## 13. Identity Operators

Check whether two variables point to the **same object in memory** (not just equal value).

| Operator | Meaning |
|---|---|
| `is` | True if both refer to the same object |
| `is not` | True if they don't |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (same value)
print(a is b)   # False (different objects)
print(a is c)   # True (same object)
```

---

## 14. Membership Operators

Check if a value exists within a sequence (string, list, tuple, dict, set).

| Operator | Meaning |
|---|---|
| `in` | True if value exists |
| `not in` | True if value doesn't exist |

```python
nums = [1, 2, 3, 4]
print(3 in nums)       # True
print(10 not in nums)  # True
print("a" in "cat")    # True
```

---

## 15. if / elif / else

```python
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

- Only one block executes.
- `elif` = "else if", checked in order.
- `else` runs when no condition above is True.

---

## 16. Nested Conditions

An `if` statement inside another `if` statement.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage, entry denied")
```

---

## 17. for Loop

Used to iterate over a sequence (list, tuple, string, dict, range, etc.).

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)   # 0 1 2 3 4

for char in "Python":
    print(char)
```

---

## 18. while Loop

Repeats as long as a condition is `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1

# while with else
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print("Loop finished")
```

⚠️ Be careful of infinite loops — always make sure the condition eventually becomes False.

---

## 19. break / continue / pass

```python
# break -> exits the loop completely
for i in range(10):
    if i == 5:
        break
    print(i)   # 0 1 2 3 4

# continue -> skips current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)   # 0 1 3 4

# pass -> does nothing, placeholder
for i in range(5):
    if i == 2:
        pass    # placeholder, code to be added later
    print(i)
```

---

## 20. range()

Generates a sequence of numbers.

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # with step

print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(2, 8)))      # [2, 3, 4, 5, 6, 7]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(10, 0, -1))) # [10, 9, ... 1]
```

---

## 21. Nested Loops

A loop inside another loop. The inner loop completes all its iterations for each single iteration of the outer loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# Multiplication table example
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

---

## 22. String Methods

Common built-in methods for string manipulation.

```python
s = "  Hello World  "

print(s.upper())        # "  HELLO WORLD  "
print(s.lower())        # "  hello world  "
print(s.strip())        # "Hello World" (removes whitespace)
print(s.replace("World", "Python"))  # "  Hello Python  "
print(s.split())        # ['Hello', 'World']
print("-".join(["a","b","c"]))  # "a-b-c"
print(s.find("World"))  # index of substring
print(s.count("l"))     # count occurrences
print("hello".capitalize())  # "Hello"
print("hello".title())       # "Hello"
print("Hello".startswith("He"))  # True
print("Hello".endswith("lo"))    # True
print("hello".isalpha())     # True
print("123".isdigit())       # True
print(len("hello"))          # 5
```

---

## 23. String Indexing

Each character in a string has a position (index), starting at `0`. Negative indexing starts from the end (`-1`).

```python
s = "Python"
#     P  y  t  h  o  n
#     0  1  2  3  4  5
#    -6 -5 -4 -3 -2 -1

print(s[0])    # 'P'
print(s[5])    # 'n'
print(s[-1])   # 'n' (last character)
print(s[-6])   # 'P' (first character)
```

⚠️ Strings are **immutable** — you cannot do `s[0] = "J"`.

---

## 24. String Slicing

Extract a portion (substring) using `s[start:stop:step]`. `start` is inclusive, `stop` is exclusive.

```python
s = "Python Programming"

print(s[0:6])     # "Python"
print(s[7:])      # "Programming" (till end)
print(s[:6])      # "Python" (from start)
print(s[:])       # full string (copy)
print(s[-11:])    # "Programming"
print(s[::-1])    # reversed string: "gnimmargorP nohtyP"
print(s[::2])     # every 2nd character
print(s[0:6:2])   # "Pto"
```

---

## 🧠 Quick Revision Cheatsheet

| Topic | Key Point to Remember |
|---|---|
| Variables | Dynamically typed, no declaration needed |
| Type Conversion | Automatic (implicit) |
| Type Casting | Manual (explicit) using `int()`, `str()`, etc. |
| f-strings | `f"{variable}"` — fastest & cleanest formatting |
| `/` vs `//` | `/` gives float, `//` gives floor int |
| `is` vs `==` | `is` checks identity, `==` checks value |
| `break` | Exits loop entirely |
| `continue` | Skips to next iteration |
| `pass` | Does nothing, placeholder |
| Slicing | `[start:stop:step]`, stop is exclusive |
| Indexing | `0` based, negative counts from end |

---

📌 *Made for quick revision & GitHub reference — keep practicing by writing small code snippets for each topic!*