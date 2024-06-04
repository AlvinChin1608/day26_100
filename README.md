# day26_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

-------------------------------------------------

## List Comprehension, Dictionary Comprehension, and Pandas List Comprehension

**List Comprehension**
List comprehension is a concise and powerful way to create lists in Python. It provides a one-line syntax that combines iterating over an iterable (like a string, list, or tuple) and creating a new list based on a condition or transformation applied to each element.

Here is an example of the normal For loop method:
```python
number = [1,2,3]
new_list = []
for n in number:
  add_1 = n+1
  new_list.append(add_1)
```

And, the same but using List Comprehension would look like:
```python
number = [1,2,3]
new_list = [n+1 for n in number]
```

**Dictionary Comprehension**
Dictionary comprehension is similar to list comprehension but is used to create dictionaries. It allows for the creation of a new dictionary by specifying keys and values in a single concise statement.
```python
# Creating a dictionary of squares
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

**Pandas List Comprehension**
In pandas, list comprehension can be used to create or modify DataFrame columns efficiently. It combines the power of list comprehension with the capabilities of pandas for data manipulation and analysis.

```python
import pandas as pd

# Creating a DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Using list comprehension to create a new column
df['age_squared'] = [x**2 for x in df['age']]
print(df)

#Output:
      name  age  age_squared
0    Alice   25          625
1      Bob   30          900
2  Charlie   35         1225
```








