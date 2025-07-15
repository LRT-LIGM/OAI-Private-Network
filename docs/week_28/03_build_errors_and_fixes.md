# Build Errors & Fixes – FlexRIC + xApps

This document tracks all the issues we encountered during the build phase and how we resolved them.

---

## 1. Error: `function definition is not allowed here` in `sqlite3_wrapper.c`

### Symptom

```
sqlite3_wrapper.c:331:1: error: function definition is not allowed here
```

### Cause

Multiple functions in the source file were defined **inside** another function by mistake.

### Solution

We moved all the function definitions out to the correct global scope in `sqlite3_wrapper.c`.

---

## 2. Error: `assert(rc == SQLITE_OK)` crash during runtime

### Symptom

```
insert_db: Assertion `rc == SQLITE_OK && "Error while inserting into the DB"` failed.
```

### Cause

The xApp attempted to insert data into the SQLite DB that violated a schema constraint (e.g., `phr > -24 AND phr < 41`), but this constraint was not visible in the code directly.

### Debug

Used:

```bash
sqlite3 /tmp/xapp_db_xxx
sqlite> .tables
sqlite> PRAGMA table_info(MAC_UE);
```

This confirmed the presence of hidden `CHECK` constraints.

### Solution

We fixed the RIC/xApp to ensure that values inserted into the DB are within valid ranges. In our case, values like `phr` were reviewed.

---

## 3. Error: Missing Binary `nearRT-RIC`

### Symptom

```
./build/examples/ric/nearRT-RIC: No such file or directory
```

### Cause

- Either compilation was incomplete
- Or `cmake` was not configured correctly.

### Solution

Recompiled from clean with:

```bash
cd ~/flexric/build
cmake -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ ..
sudo make -j1
```

This resolved all missing binaries.

---
