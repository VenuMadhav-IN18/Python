# Python Coding Practice Problems with Solutions

## Problem Difficulty Levels
- 🟢 **Easy**: Basic syntax and simple logic
- 🟡 **Medium**: Requires multiple concepts
- 🔴 **Hard**: Complex logic and edge cases

---

## 🟢 Easy Problems

### Problem 1: Sum of Two Numbers
**Problem**: Write a function that takes two numbers and returns their sum.

```python
def sum_numbers(a, b):
    return a + b

# Test cases
print(sum_numbers(5, 3))      # 8
print(sum_numbers(-1, 1))     # 0
print(sum_numbers(0.5, 1.5))  # 2.0
```

---

### Problem 2: Check Even or Odd
**Problem**: Write a function to check if a number is even or odd.

```python
def is_even(num):
    return num % 2 == 0

# Test cases
print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(0))   # True
```

---

### Problem 3: Find Maximum
**Problem**: Find the maximum of three numbers.

```python
def find_max(a, b, c):
    return max(a, b, c)

# Alternative without using max()
def find_max_manual(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Test cases
print(find_max(10, 20, 15))  # 20
print(find_max(3, 3, 3))     # 3
print(find_max(-5, -2, -10)) # -2
```

---

### Problem 4: Reverse a String
**Problem**: Reverse a given string.

```python
def reverse_string(s):
    return s[::-1]

# Test cases
print(reverse_string("hello"))    # "olleh"
print(reverse_string("python"))   # "nohtyp"
print(reverse_string("a"))        # "a"
```

---

### Problem 5: Count Vowels
**Problem**: Count the number of vowels in a string.

```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Alternative using sum and list comprehension
def count_vowels_alt(s):
    return sum(1 for char in s if char in "aeiouAEIOU")

# Test cases
print(count_vowels("hello"))       # 2
print(count_vowels("PYTHON"))      # 1
print(count_vowels("aEiOu"))       # 5
```

---

## 🟡 Medium Problems

### Problem 6: Remove Duplicates from List
**Problem**: Remove duplicate elements from a list while preserving order.

```python
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Alternative using dict (Python 3.7+)
def remove_duplicates_alt(lst):
    return list(dict.fromkeys(lst))

# Test cases
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4]))  # [1, 2, 3, 4]
print(remove_duplicates([1, 1, 1, 1]))           # [1]
print(remove_duplicates([1, 2, 3]))              # [1, 2, 3]
```

---

### Problem 7: Find Sum of List Elements
**Problem**: Calculate the sum of all elements in a list.

```python
def sum_list(lst):
    return sum(lst)

# Alternative using loop
def sum_list_loop(lst):
    total = 0
    for item in lst:
        total += item
    return total

# Alternative using reduce
from functools import reduce
def sum_list_reduce(lst):
    return reduce(lambda x, y: x + y, lst, 0)

# Test cases
print(sum_list([1, 2, 3, 4, 5]))     # 15
print(sum_list([]))                   # 0
print(sum_list([-1, 2, -3, 4]))       # 2
```

---

### Problem 8: Check if List is Palindrome
**Problem**: Check if a list reads the same forwards and backwards.

```python
def is_palindrome_list(lst):
    return lst == lst[::-1]

# Alternative
def is_palindrome_list_alt(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - 1 - i]:
            return False
    return True

# Test cases
print(is_palindrome_list([1, 2, 3, 2, 1]))  # True
print(is_palindrome_list([1, 2, 3, 4, 5]))  # False
print(is_palindrome_list([1]))               # True
```

---

### Problem 9: Merge Two Lists
**Problem**: Merge two sorted lists into one sorted list.

```python
def merge_sorted_lists(lst1, lst2):
    result = []
    i = j = 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

# Simple alternative
def merge_sorted_lists_simple(lst1, lst2):
    return sorted(lst1 + lst2)

# Test cases
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2], [3, 4]))        # [1, 2, 3, 4]
print(merge_sorted_lists([], [1, 2]))            # [1, 2]
```

---

### Problem 10: Find Second Largest
**Problem**: Find the second largest element in a list.

```python
def find_second_largest(lst):
    unique_elements = list(set(lst))
    unique_elements.sort(reverse=True)
    return unique_elements[1] if len(unique_elements) >= 2 else None

# Alternative
def find_second_largest_alt(lst):
    if len(set(lst)) < 2:
        return None
    lst_copy = sorted(set(lst), reverse=True)
    return lst_copy[1]

# Test cases
print(find_second_largest([1, 2, 3, 4, 5]))      # 4
print(find_second_largest([5, 5, 5, 5]))         # None
print(find_second_largest([1, 2]))               # 1
```

---

### Problem 11: Count Words in String
**Problem**: Count the number of words in a string.

```python
def count_words(s):
    return len(s.split())

# Test cases
print(count_words("Hello World Python"))    # 3
print(count_words("   "))                   # 0
print(count_words("Single"))                # 1
```

---

### Problem 12: Convert List to Dictionary
**Problem**: Convert a list of key-value pairs to a dictionary.

```python
def list_to_dict(lst):
    return dict(lst)

# Alternative
def list_to_dict_alt(lst):
    result = {}
    for key, value in lst:
        result[key] = value
    return result

# Test cases
print(list_to_dict([('a', 1), ('b', 2), ('c', 3)]))  # {'a': 1, 'b': 2, 'c': 3}
print(list_to_dict([]))                              # {}
```

---

### Problem 13: Find Common Elements
**Problem**: Find common elements between two lists.

```python
def find_common(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Alternative preserving order
def find_common_ordered(lst1, lst2):
    set2 = set(lst2)
    return [x for x in lst1 if x in set2]

# Test cases
print(find_common([1, 2, 3, 4], [3, 4, 5, 6]))      # [3, 4] or [4, 3]
print(find_common([1, 1, 2, 2], [2, 2, 3, 3]))      # [2]
print(find_common([1, 2], [3, 4]))                  # []
```

---

### Problem 14: Capitalize First Letter
**Problem**: Capitalize the first letter of each word in a string.

```python
def capitalize_words(s):
    return s.title()

# Alternative
def capitalize_words_alt(s):
    return " ".join(word.capitalize() for word in s.split())

# Test cases
print(capitalize_words("hello world python"))  # "Hello World Python"
print(capitalize_words("python"))              # "Python"
```

---

### Problem 15: Filter Positive Numbers
**Problem**: Filter out negative numbers and keep only positive ones.

```python
def filter_positive(lst):
    return [x for x in lst if x > 0]

# Alternative using filter
def filter_positive_alt(lst):
    return list(filter(lambda x: x > 0, lst))

# Test cases
print(filter_positive([-1, 2, -3, 4, 0, 5]))  # [2, 4, 5]
print(filter_positive([-1, -2, -3]))           # []
```

---

## 🔴 Hard Problems

### Problem 16: Rotate List
**Problem**: Rotate a list by n positions to the right.

```python
def rotate_list(lst, n):
    if not lst:
        return lst
    n = n % len(lst)  # Handle n > len(lst)
    return lst[-n:] + lst[:-n] if n != 0 else lst

# Test cases
print(rotate_list([1, 2, 3, 4, 5], 2))    # [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3, 4, 5], 7))    # [4, 5, 1, 2, 3] (7 % 5 = 2)
print(rotate_list([1, 2, 3, 4, 5], 0))    # [1, 2, 3, 4, 5]
```

---

### Problem 17: Check Anagram
**Problem**: Check if two strings are anagrams of each other.

```python
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# Alternative using Counter
from collections import Counter
def is_anagram_counter(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

# Test cases
print(is_anagram("listen", "silent"))      # True
print(is_anagram("hello", "world"))        # False
print(is_anagram("Abc", "cab"))            # True
```

---

### Problem 18: Find Longest Word
**Problem**: Find the longest word in a sentence.

```python
def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Alternative
def find_longest_word_alt(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Test cases
print(find_longest_word("Python is an amazing programming language"))  # "programming"
print(find_longest_word("Hello world"))  # "Hello"
```

---

### Problem 19: Fibonacci Sequence
**Problem**: Generate the first n Fibonacci numbers.

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Recursive approach (slower)
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test cases
print(fibonacci(5))   # [0, 1, 1, 2, 3]
print(fibonacci(7))   # [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(1))   # [0]
```

---

### Problem 20: Check Balanced Parentheses
**Problem**: Check if parentheses are balanced in a string.

```python
def is_balanced(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

# Test cases
print(is_balanced("()"))           # True
print(is_balanced("([{}])"))       # True
print(is_balanced("([)]"))         # False
print(is_balanced("("))            # False
```

---

### Problem 21: Flatten Nested List
**Problem**: Flatten a nested list structure.

```python
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# Test cases
print(flatten_list([1, [2, 3, [4, 5]]]))        # [1, 2, 3, 4, 5]
print(flatten_list([1, 2, [3, [4, [5]]]]))      # [1, 2, 3, 4, 5]
print(flatten_list([1, 2, 3]))                  # [1, 2, 3]
```

---

### Problem 22: Sum of Digits
**Problem**: Calculate the sum of all digits in a number.

```python
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# Alternative
def sum_of_digits_alt(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Test cases
print(sum_of_digits(123))   # 6
print(sum_of_digits(999))   # 27
print(sum_of_digits(-123))  # 6
```

---

### Problem 23: Find Duplicates
**Problem**: Find all duplicate elements in a list.

```python
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Test cases
print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))  # [2, 3]
print(find_duplicates([1, 1, 1]))               # [1]
print(find_duplicates([1, 2, 3]))               # []
```

---

### Problem 24: Check Prime Number
**Problem**: Check if a number is prime.

```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(17))   # True
print(is_prime(20))   # False
print(is_prime(2))    # True
print(is_prime(1))    # False
```

---

### Problem 25: Group By Key
**Problem**: Group elements by a key function.

```python
def group_by_length(lst):
    result = {}
    for item in lst:
        length = len(item)
        if length not in result:
            result[length] = []
        result[length].append(item)
    return result

# Alternative using defaultdict
from collections import defaultdict
def group_by_length_alt(lst):
    result = defaultdict(list)
    for item in lst:
        result[len(item)].append(item)
    return dict(result)

# Test cases
words = ["a", "bb", "ccc", "dd", "e"]
print(group_by_length(words))
# {1: ['a', 'e'], 2: ['bb', 'dd'], 3: ['ccc']}
```

---

## Practice Tips

### While Solving:
1. **Read carefully** - Understand what the problem asks
2. **Identify inputs/outputs** - What goes in, what should come out
3. **Think of edge cases** - Empty lists, single elements, negative numbers
4. **Write pseudocode first** - Plan before coding
5. **Test with examples** - Verify with test cases

### Common Python Patterns to Use:
- List comprehensions for filtering/mapping
- `for` loops for iteration
- `while` loops for conditions
- `sorted()` and `.sort()` for sorting
- `set()` for finding unique elements or intersections
- `dict()` for key-value relationships
- Built-in functions: `max()`, `min()`, `sum()`, `len()`, `any()`, `all()`

### Debugging Tips:
- Use `print()` statements to check values
- Test with simple examples first
- Verify loop indices are correct
- Check for off-by-one errors
- Test empty inputs and single-element inputs
- Make sure return statements are in the right place

---

**Remember**: The best way to learn is by doing. Try solving these problems without looking at the solutions first! 🚀
