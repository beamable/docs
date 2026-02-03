# Plugin Source Modification Guidelines

This plugin is intentionally designed to be **modified directly at the source level**, rather than extended through Dependency Injection (DI).  
To keep custom changes maintainable and upgrade-friendly, **all modifications must follow the rules below**.

---

## Philosophy

- Source code is the extension point
- All changes must be **explicit, visible, and traceable**
- Updating the plugin should never require guessing what was customized

---

## 1. Mark All Custom Changes

Every modification to the plugin source **must be clearly marked**.

```cpp
// === CUSTOM MODIFICATION BEGIN ===
// Author: <Name or Team>
// Date: YYYY-MM-DD
// Reason: Why this change exists
// === CUSTOM MODIFICATION END ===
```

## 2. Group Changes Using Regions (C++)

All custom code could be grouped using #pragma region.

```cpp

#pragma region Custom_Plugin_Modifications
// custom code here
#pragma endregion

```

## 3. Extend, Don’t Erase

Prefer extending or overriding behavior instead of deleting original code.

 - Comment out original logic instead of removing it

 - Add replacements inside a custom region

 - Preserve context whenever possible

## 4. Keep Changes Small and Focused

 - One responsibility per modification block

 - Do not mix unrelated changes

 - Avoid large, unstructured edits

Small, isolated changes are easier to review, revert, and migrate.

## 5. Document Behavioral Impact

Any change affecting:

 - Public behavior or APIs

 - Networking or replication

 - Save / Load logic

 - Performance characteristics

Must include an explanatory comment, even if the code is self-explanatory.
