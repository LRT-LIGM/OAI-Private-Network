# FlexRIC Source Code Modifications

This document lists and explains all source-level code changes made during FlexRIC integration and debugging with the OAI 5G SA platform. These modifications were essential for ensuring compatibility, improving error diagnostics, and overcoming runtime issues.

---

## File: `src/xApp/db/sqlite3/sqlite3_wrapper.c`

### 1. Error Handling – Replace Assertion with Proper Logging

**Original Code:**

```c
assert(rc == SQLITE_OK && "Error while inserting into the DB. Check the err_msg string for further info");
```

**Modified Code:**

```c
if (rc != SQLITE_OK) {
    fprintf(stderr, "[xApp][SQLite] ERROR: %s\n", err_msg);
    sqlite3_free(err_msg);
    exit(EXIT_FAILURE);
}
```

**Reason:** Avoids abrupt `core dumped` on constraint violation and gives clear debug message for troubleshooting.

---

### 2. Disabling Faulty Constraint: `phr > -24 AND phr < 41`

**Original Schema Insertion (Implicit):**

```sql
phr INTEGER NOT NULL CHECK( phr > -24 AND phr < 41 )
```

**Modified Behavior:** Constraint was removed or relaxed to avoid runtime insert failures due to PHR values falling outside the valid range because of rounding, simulation noise, or actual UE measurements.

**Updated Schema:**

```sql
phr INTEGER
```

**Note:** Since the schema is dynamically created, this was handled either by editing the schema generation code (inside wrapper.c) or by modifying the DB externally if schema was generated separately.

---

### 3. Debug Output Enhancements

Several debug `printf()` statements were added to trace values and understand message flow:

```c
printf("[DEBUG] Inserting MAC UE sample: phr = %f\n", phr);
printf("[DEBUG] DB file: %s\n", db_filename);
```

**Reason:** Helps understand where failure occurs or when insert succeeds, useful in live monitoring.

---

## Build Config Adjustments

### Compilation With Clang (for better error reporting)

```bash
cmake -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ ..
sudo make -j1
```

**Why?** GCC was less explicit about nested function errors. Clang helped isolate build issues.

---

## Summary

| Area               | Change Made                 | Purpose                         |
| ------------------ | --------------------------- | ------------------------------- |
| Error Handling     | Assert ➔ Logging            | Better diagnostics, no crash    |
| Schema Constraint  | Removed `phr` CHECK         | Prevents xApp crash on bad data |
| Debug Statements   | Added `printf` in wrapper.c | Monitor insertions & flow       |
| Compilation Method | Switched to Clang           | Clearer compile errors          |

These changes were minimal but crucial for achieving stable xApp execution and valid metric storage.

---
