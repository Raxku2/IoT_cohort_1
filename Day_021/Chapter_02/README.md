# Chapter 02: The DNA of Data

Welcome to the foundation of programming logic. If a program is a recipe, **Data Types** are the ingredients. To build highly optimized and bug-free applications, you must understand not just *what* your data is, but *how* the computer stores and interacts with it behind the scenes.

This guide is designed with **zero cognitive overload**. We will break down complex memory architectures and data structures into intuitive, memorable concepts.

---

## 1. The Great Divide: Data Type Categories

Every piece of data in JavaScript falls into one of two fundamental categories. The difference between them comes down to **simplicity vs. complexity**, and **where they live in the computer's memory**.

| Feature | Primitive Data Types | Non-Primitive (Reference) Data Types |
| --- | --- | --- |
| **Nature** | Simple, single values | Complex collections of values |
| **Mutability** | **Immutable** (Cannot be changed directly) | **Mutable** (Properties can be modified) |
| **Memory** | Stored in the **Stack** | Stored in the **Heap** |
| **Access** | Accessed by **Value** | Accessed by **Reference** |

---

## 2. The 7 Primitives (The Building Blocks)

Primitives are the lowest level of data. They are singular, hardcoded facts. Think of them as individual atoms.

### Number

JavaScript doesn't distinguish between integers and decimals. They are all just `Number` (stored as 64-bit floating-point values).

```javascript
let age = 28;         // Integer
let price = 99.99;    // Floating point

```

### BigInt

Standard numbers hit a limit at `2^53 - 1`. If you are dealing with cryptographic keys, high-precision timing, or massive scientific calculations, you need `BigInt`. You create one by appending an `n` to the end of an integer.

```javascript
let massiveNumber = 9007199254740991n; 

```

### String

A sequence of characters used for text. Wrap them in single quotes, double quotes, or backticks.

```javascript
let greeting = "Hello, World!";
let name = 'Alice';

```

### Boolean

The ultimate binary choice. It can only be one of two values: `true` or `false`.

```javascript
let isLoggedIn = true;
let hasError = false;

```

### null (Stand-alone empty value)

`null` is an **intentional absence of value**. It means "I purposefully emptied this box."

```javascript
let activeUser = null; // We explicitly know no user is active right now

```

### undefined

`undefined` is an **unintentional absence of value**. It means "A box exists, but no one has put anything inside it yet."

```javascript
let futureData; 
console.log(futureData); // Output: undefined

```

### Symbol (Uniqueness)

Introduced in ES6, a `Symbol` generates a completely unique identifier. Even if two Symbols have the same description, they are never equal. Think of it as a digital fingerprint.

```javascript
let sym1 = Symbol("id");
let sym2 = Symbol("id");
console.log(sym1 === sym2); // Output: false

```

---

## 3. Non-Primitive Data Types

### Object (As a Data Type)

If primitives are atoms, Objects are molecules. An object allows you to store collections of data and more complex entities using **key-value pairs**. (Note: Arrays and Functions are technically just specialized Objects in JavaScript).

```javascript
let user = {
    name: "John Doe",   // String
    age: 30,            // Number
    isActive: true      // Boolean
};

```

---

## 4. The Detective: `typeof` Operator

When dealing with dynamic data (like an API response), you need a way to check what kind of data you are holding. The `typeof` operator tells you the type of a value.

```javascript
typeof "Hello"      // Returns "string"
typeof 42           // Returns "number"
typeof true         // Returns "boolean"
typeof undefined    // Returns "undefined"

```

> **The `typeof null` Bug:**
> If you run `typeof null`, JavaScript returns `"object"`. **This is a famous historical bug in JavaScript.** `null` is absolutely a primitive, but changing this behavior now would break thousands of legacy websites, so the bug was permanently left in the language.

---

## 5. Memory Architecture: Stack vs. Heap

To master data types, you must visualize how they are stored in your computer's RAM. JavaScript uses two distinct memory spaces: The **Stack** and the **Heap**.

### The Stack Memory (For Primitives)

* **Analogy:** A neat, orderly stack of small, identical boxes.
* **How it works:** It is incredibly fast, but has limited space. Because Primitive types have a fixed, predictable size, they are placed directly into the Stack.
* **Memory Allocation:** When you declare a primitive (`let name = "Alex"`), the actual value `"Alex"` is stored right there in the Stack.

### The Heap Memory (For Reference Types)

* **Analogy:** A massive, unstructured warehouse.
* **How it works:** It is slightly slower to access but can hold massive amounts of data of unpredictable sizes (like Objects and Arrays).
* **Memory Allocation:** When you create an Object, the actual data goes into the Heap. The computer then writes down the **memory address** (the reference) of where that data lives, and stores *that address* in the Stack.

---

## 6. Interaction: Call by Value vs. Call by Reference

Understanding how data behaves when you copy it or pass it to a function separates juniors from seniors.

### Call by Value (Copies)

When you assign a **Primitive** to a new variable, JavaScript creates a strict **copy** of the value.

```javascript
let a = 10;
let b = a;  // 'b' gets a strict copy of '10'

b = 20;     // Changing 'b' does not affect 'a'

console.log(a); // 10
console.log(b); // 20

```

*Mental Model:* You took a photocopy of a document and gave it to a friend. If they draw on their copy, your original document is untouched.

### Call by Reference (Sharing the Remote)

When you assign a **Non-Primitive** (Object) to a new variable, you are NOT copying the data. You are copying the **memory address** (the pointer) from the Stack. Both variables now point to the exact same object in the Heap.

```javascript
let userOne = { name: "Alice", email: "alice@google.com" };
let userTwo = userOne;  // userTwo gets the memory address, NOT a copy of the object!

userTwo.email = "hacked@evil.com"; // We change data via userTwo

console.log(userOne.email); // Output: "hacked@evil.com"

```

*Mental Model:* You have one TV (the Object in the Heap). `userOne` and `userTwo` are two remote controls. If `userTwo` changes the channel, `userOne` also sees the new channel, because they are controlling the exact same TV.
---

<div align="center">

[![Previous](https://img.shields.io/badge/-%5B%E2%86%90%5D_Previous_Chapter-black?style=for-the-badge)](../../Day_020/Chapter_01/) [![Next](https://img.shields.io/badge/Next_Chapter_%5B%E2%86%92%5D-black?style=for-the-badge)](../../Day_021/Chapter_03/)

</div>