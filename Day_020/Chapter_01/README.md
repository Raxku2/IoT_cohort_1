## 1. Under the Hood: Memory Space Allocation

Before you can declare a variable, you need to understand where it lives. The JavaScript engine allocates memory in two distinct realms:

* **The Stack (Static Memory):** Fast, rigid, and organized. It stores **Primitive Values** (Numbers, Strings, Booleans) and pointers (references) to complex data.
* **The Heap (Dynamic Memory):** Expansive and unstructured. It stores **Reference Types** (Objects, Arrays, Functions).

> **🧠 The Mental Model:** The Stack is a tightly packed filing cabinet for small, predictable items. The Heap is a massive warehouse for large, complex items. The Stack just holds a "map" (pointer) to the warehouse location.

---

## 2. Variable Declaration, Re-assignment & Keywords

In modern JavaScript, declaring a variable means asking the engine to reserve a space in memory. We have three ways to do this: `var`, `let`, and `const`.

### The Core Keywords

| Keyword | Re-assignment? | Recommended Use |
| --- | --- | --- |
| **`const`** | ❌ No | **Default choice.** Use for variables that should never change their reference. |
| **`let`** | ✅ Yes | Use when you know a value will change (e.g., loops, counters, state). |
| **`var`** | ✅ Yes | **Legacy.** Avoid in modern code. Prone to scope bugs. |

### Practical Approach

```javascript
// 1. Variable Declaration & Initialization
let currentScore = 0; 
const maxPlayers = 4; // Constant: Cannot be changed

// 2. Variable Re-assignment
currentScore = 10; // ✅ Valid (let allows re-assignment)
// maxPlayers = 5; // ❌ TypeError: Assignment to constant variable.

// 3. The Object Mutation Exception
const user = { name: "Alice" };
user.name = "Bob"; // ✅ Valid! 
// Why? 'const' locks the POINTER in the Stack, not the data in the Heap.

```

---

## 3. Demystifying Scope

**Scope** determines where your variables are visible and accessible. Think of it as the security clearance levels of your code.

### The 3 Levels of Scope

1. **Global Scope:** Declared outside of any function or block. Visible to the *entire* script. (High risk of collisions).
2. **Functional Scope:** Variables declared inside a function. Only visible *within* that function.
3. **Block Scope:** Variables declared inside a `{ }` block (like `if` statements or `for` loops).

### `let` vs `var` Scope Differences

This is where `var` often breaks applications. **`var` does not respect block scope**, whereas `let` and `const` do.

```javascript
if (true) {
  var oldSchool = "I leak out!";
  let modernJS = "I am locked in here.";
}

console.log(oldSchool); // "I leak out!" (var ignores the block)
console.log(modernJS);  // ReferenceError: modernJS is not defined

```

### Lexical Scope (The Scope Chain)

JavaScript determines scope lexically—meaning it relies on *where the code is physically written*. If an inner function needs a variable it doesn't have, it looks "outward" to its parent function, climbing the chain until it hits the Global Scope. It never looks "inward".

---

## 4. The Execution Context & Hoisting

To understand **Hoisting**, we have to understand how JavaScript runs your code. It doesn't just read top-to-bottom. It executes in an environment called the **Execution Context**, which has two distinct phases.

### The Two Phases of Execution Context

1. **Phase 1: Memory Allocation (Creation Phase)**
The engine scans your code and allocates memory for variables and functions *before* executing a single line.
2. **Phase 2: Code Execution (Thread of Execution)**
The engine reads the code line-by-line, assigning actual values and running functions.

### How this impacts Hoisting

**Hoisting** is the phenomenon where variables and functions seem to move to the "top" of your code. In reality, they aren't moving; they are just being stored in memory during Phase 1.

* **`var` Hoisting:** Stored in memory as `undefined`. If you log it before declaring it, it doesn't crash; it just returns `undefined`.
* **Function Hoisting:** Entire functions are stored in memory. You can call them before they are physically written in the code.
* **`let` & `const` Hoisting (The TDZ):** They *are* hoisted, but the engine does not initialize them with `undefined`. They are placed in a **Temporal Dead Zone (TDZ)**. Accessing them before initialization throws a fatal error.

```javascript
console.log(player); // undefined (var is hoisted with 'undefined')
console.log(score);  // ReferenceError (let is in the TDZ)

var player = "John";
let score = 100;

```

---
