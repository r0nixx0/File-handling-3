# Python File Handling 3
 
Python File handling
https://drive.google.com/file/d/1sIv9rb6PizW9sfts9eVu0BkLYWLjysiT/view

**Rules**

- Always `close()` a file after you finish with it.
- Pick the right mode. `"w"` **erases** the file first. `"a"` **adds** to the end.
  `"r"` only reads.
- `filename` is given to you as a parameter — never type a file name inside
  your function.
- Every line you write must end with `"\n"`.


## Exercise 1

**Problem:**

`read_line(filename, line_number)`

Return line number `line_number` (starting at 1) from the file, without the
`"\n"` at the end.

You **must** use `readline()` — not `readlines()` or `read()`.

If the file does not have that line (or `line_number` is 0 or less), return `""`.

**Example:**

    Example File Content (days.txt):
        Mon
        Tue
        Wed

    Example Input:
        line_number = 2

    Program Output:
        "Tue"

    Example Input:
        line_number = 4

    Program Output:
        ""

*Hint:* every time you call `readline()` it gives you the **next** line. When
there are no lines left, it gives `""`. So to get line 2, call it 2 times.

---

## Exercise 2

**Problem:**

`reverse_lines(source, destination)`

Read the file `source` and write a **new** file `destination` with the same
lines in **reverse order** — the last line first.
Return how many lines you wrote.

The `source` file must not be changed.

**Example:**

    Example File Content (in.txt):
        one
        two
        three

    File Output (out.txt):
        three
        two
        one

    Program Output:
        3

*Hint:* be careful — the last line of a file sometimes has **no** `"\n"` at
the end. `.strip()` every line, then add your own `"\n"`.

---

## Exercise 3

**Problem:**

`merge_files(first, second, destination)`

Two classes each have a file of student names. Write all the names from
`first`, then all the names from `second`, into the file `destination`.
Return the total number of names written.

If `destination` already exists, the old content must be **replaced**.
The `first` and `second` files must not be changed.

**Example:**

    Example File Content (class_a.txt):
        Bat
        Saraa

    Example File Content (class_b.txt):
        Anu
        Dorj

    File Output (all.txt):
        Bat
        Saraa
        Anu
        Dorj

    Program Output:
        4

*Hint:* three files means three `open()` calls and three `close()` calls.

---

## Exercise 4

**Problem:**

`find_score(filename, name)`

Every line of the file looks like `name,score`. Use **linear search** to find
the student called `name` and return their score as an **integer**.

Return `-1` if the student is not in the file.
Capital letters matter: `"bat"` does **not** match `"Bat"`.

**Example:**

    Example File Content (scores.txt):
        Bat,78
        Saraa,91
        Tuguldur,65
        Anu,88

    Example Input:
        name = "Anu"

    Program Output:
        88

    Example Input:
        name = "Dorj"

    Program Output:
        -1

*Hint:* `"Anu,88".split(",")` gives `["Anu", "88"]`. Compare the first part
with `name`, and use `int()` on the second part.

---

## Exercise 5

**Problem:**

`update_score(filename, name, new_score)`

Change the score of the student called `name` to `new_score`, and save the
file. Every other line must stay **exactly** the same.
Return `True` if the student was found and updated.

If the student is not in the file, do **not** change the file, and return `False`.

**Example:**

    Example File Content (scores.txt):
        Bat,78
        Saraa,91
        Tuguldur,65
        Anu,88

    Example Input:
        name      = "Saraa"
        new_score = 95

    File Content afterwards (scores.txt):
        Bat,78
        Saraa,95
        Tuguldur,65
        Anu,88

    Program Output:
        True

    Example Input:
        name      = "Dorj"
        new_score = 50

    File Content afterwards (scores.txt):
        (unchanged)

    Program Output:
        False

*Hint:* read **all** the lines and `close()` the file first. Change the one
line in your list, then open the file again with `"w"` and write every line
back. Remember the new line needs `"\n"` at the end.

---
