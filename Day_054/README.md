# 🔍 The Master Guide to PyMongo Queries & Filters

This guide covers every major query operator you will need. Consider this your ultimate cheat sheet.

---

## The Golden Rule of PyMongo Queries

In PyMongo, a query (or filter) is just a **Python Dictionary**. You pass this dictionary into methods like `.find()` or `.find_one()`.

```python
# The basic syntax:
# collection.find({ "field_name": { "$operator": value } })
```

*Note: All MongoDB operators start with a dollar sign (`$`).*

---

## 1. Exact Matches (The Basics) 🎯

The simplest way to filter is by asking for an exact match. You don't even need a special operator for this.

```python
# Find all users exactly 25 years old
query = {"age": 25}
results = collection.find(query)

# Find users who live in "London" AND are exactly "Active"
# (Just separate them with a comma)
query = {"city": "London", "status": "Active"}
```

---

## 2. Comparison Operators (Math & Ranges) 🧮

What if you want users *older* than 18? Or prices *less than* $50? Use comparison operators.

*   `$eq`: **E**quals (Same as exact match above)
*   `$ne`: **N**ot **E**qual
*   `$gt`: **G**reater **T**han (`>`)
*   `$gte`: **G**reater **T**han or **E**qual to (`>=`)
*   `$lt`: **L**ess **T**han (`<`)
*   `$lte`: **L**ess **T**han or **E**qual to (`<=`)
*   `$in`: Is **IN** an array of values
*   `$nin`: Is **N**ot **IN** an array of values

### Examples:

```python
# Find users older than 18 (age > 18)
collection.find({"age": {"$gt": 18}})

# Find products between $50 and $100 (50 <= price <= 100)
collection.find({"price": {"$gte": 50, "$lte": 100}})

# Find users who are NOT from New York
collection.find({"city": {"$ne": "New York"}})

# Find users whose role is EITHER "admin" OR "moderator"
collection.find({"role": {"$in": ["admin", "moderator"]}})
```

---

## 3. Logical Operators (AND, OR, NOT) 🧠

Sometimes you have complex conditions. 

*   `$or`: Matches if **ANY** of the conditions are true.
*   `$and`: Matches if **ALL** conditions are true (Note: implicitly done by comma-separating dictionary keys, but `$and` is needed if filtering the same field twice).
*   `$nor`: Matches if **NONE** of the conditions are true.

### Examples:

```python
# Find users who are EITHER from "Paris" OR are younger than 20
query = {
    "$or": [
        {"city": "Paris"},
        {"age": {"$lt": 20}}
    ]
}
collection.find(query)

# Find products that are NEITHER "Electronics" NOR out of stock (stock = 0)
query = {
    "$nor": [
        {"category": "Electronics"},
        {"stock": 0}
    ]
}
```

---

## 4. Element Operators (Checking fields) 🔎

Because MongoDB is schema-less (NoSQL), some documents might have a field, and others might not.

*   `$exists`: Checks if a field exists in the document, regardless of its value.
*   `$type`: Checks if a field is a specific data type (e.g., string, integer).

### Examples:

```python
# Find all documents that ACTUALLY HAVE a "phone_number" field
collection.find({"phone_number": {"$exists": True}})

# Find documents where the "age" field accidentally got saved as a String
# (Type 2 represents a String in BSON)
collection.find({"age": {"$type": 2}}) 
```

---

## 5. Array Operators (Working with lists) 📦

If your document has a list (e.g., `"tags": ["python", "coding", "web"]`), querying gets interesting.

*   `$all`: Matches if the array contains **all** specified elements (order doesn't matter).
*   `$size`: Matches if the array is exactly a certain length.
*   `$elemMatch`: Matches if at least one item in the array matches *multiple* conditions.

### Examples:

```python
# Find posts that have BOTH "mongodb" and "python" in their tags
collection.find({"tags": {"$all": ["mongodb", "python"]}})

# Find users who have exactly 3 hobbies
collection.find({"hobbies": {"$size": 3}})

# Suppose you have a list of dictionaries: "scores": [{"subject": "Math", "grade": 90}, ...]
# Find documents where the user got > 85 in Math specifically:
collection.find({
    "scores": {
        "$elemMatch": {"subject": "Math", "grade": {"$gt": 85}}
    }
})
```

---

## 6. Text Search & Regular Expressions (Regex) 🔤

If you want to build a search bar, you don't want exact matches. You want to find if a string *contains* a word.

*   `$regex`: Allows you to use Regular Expressions to search text.
*   `$options`: Used with `$regex`, usually set to `"i"` for **Case-Insensitive** searching.

### Examples:

```python
# Find users whose name contains "john" (matches "John", "johnny", "Elton John")
collection.find({
    "name": {
        "$regex": "john", 
        "$options": "i" # "i" means ignore case (uppercase/lowercase)
    }
})

# Find emails that end with "@gmail.com"
collection.find({
    "email": {"$regex": "@gmail\.com$"}
})
```

---

## 7. Shaping the Results (Sort, Limit, Skip, Projection) 🎨

Once you filter your data, you usually want to format *how* it comes back to Python.

### A. Sorting
Sort the results alphabetically or numerically. Use `1` for Ascending (A-Z, 0-9) and `-1` for Descending (Z-A, 9-0).

```python
# Find all users, sort by age youngest to oldest (Ascending)
collection.find().sort("age", 1)

# Sort by newest created (Descending)
collection.find().sort("created_at", -1)
```

### B. Limiting
Only return a specific number of documents. Great for "Top 10" lists.

```python
# Get the top 5 most expensive products
collection.find().sort("price", -1).limit(5)
```

### C. Skipping (Pagination)
Skip a certain number of results. Used with `.limit()` to create pages (e.g., Page 1, Page 2).

```python
# "Page 2" of products (assuming 10 items per page)
# Skip the first 10, then take the next 10
collection.find().skip(10).limit(10)
```

### D. Projection (Hiding Fields)
Databases send the whole document by default. If a user document has a heavy `profile_image_data` field or a `password_hash`, you can block it from downloading to save bandwidth.
*   `1` means **Show** this field.
*   `0` means **Hide** this field.
*(You cannot mix 1s and 0s, except for the `_id` field).*

```python
# Give me all users, but ONLY return their name and email. 
# Also, hide the default _id field.
projection = {"_id": 0, "name": 1, "email": 1}

results = collection.find({}, projection) 
# Note: The first {} means "find all". The second argument is the projection.
```

---

## Putting it all together (A Master Query) 🏆

Let's combine everything into one massive, real-world query.

**Scenario:** *Find the 5 newest users who are active, older than 21, live in either NY or LA, whose bio contains the word "developer". Only return their name and age.*

```python
query = {
    "status": "Active",
    "age": {"$gt": 21},
    "city": {"$in": ["NY", "LA"]},
    "bio": {"$regex": "developer", "$options": "i"}
}

projection = {
    "_id": 0,
    "name": 1,
    "age": 1
}

results = collection.find(query, projection).sort("created_at", -1).limit(5)

for user in results:
    print(user)
```

You are now a PyMongo querying expert! Keep this document handy whenever you are building your database logic.