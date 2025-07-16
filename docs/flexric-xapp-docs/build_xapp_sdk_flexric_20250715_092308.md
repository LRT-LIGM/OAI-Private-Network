# Building and Installing xapp_sdk for FlexRIC with SWIG 4.1 and Clang

This guide explains how to build the Python xApp SDK bindings (`xapp_sdk`) for FlexRIC using **Clang** and **SWIG ≥ 4.1**, ensuring compatibility with Python xApps.

---

## Prerequisites

- Ubuntu 22.04
- Clang and Clang++
- SWIG 4.1.1+ (must be built from source)
- FlexRIC source code already cloned

---

## 1. Install Required Packages

```bash
sudo apt update
sudo apt install clang clang++ build-essential cmake python3-dev \
    bison libpcre2-dev automake libtool
```

---

## 2. Install SWIG 4.1.1 from Source

```bash
cd ~
wget https://github.com/swig/swig/archive/refs/tags/v4.1.1.tar.gz
tar -xzf v4.1.1.tar.gz
cd swig-4.1.1

./autogen.sh
./configure
make -j2
sudo make install
```

### Confirm version

```bash
swig -version
# Should show 4.1.1
```

---

## 3. Clean Previous FlexRIC Build

```bash
cd ~/flexric
rm -rf build
mkdir build && cd build
```

---

## 4. Configure with Clang and Explicit SWIG Path

```bash
cmake .. \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
  -DSWIG_EXECUTABLE=/usr/local/bin/swig \
  -DENABLE_XAPP_PYTHON=ON
```

---

## 5. Compile with Single Thread

```bash
sudo make -j1
```

---

## 6. Locate the Generated xapp_sdk

```bash
find . -name "_xapp_sdk.so"
# Expected: ./src/xApp/swig/_xapp_sdk.so and/or ./examples/xApp/python3/_xapp_sdk.so
```

---

## 7. Install the Python Module

Copy both `.py` and `.so` files to Python’s site-packages:

```bash
sudo cp ./examples/xApp/python3/xapp_sdk.py /usr/local/lib/python3.10/dist-packages/
sudo cp ./examples/xApp/python3/_xapp_sdk.so /usr/local/lib/python3.10/dist-packages/
```

---

## 8. Test the Module

```bash
python3 -c "import xapp_sdk"
```

> If no error, you’re done!

---

## Notes

- This enables you to run any Python xApp under `flexric/examples/xApp/python3/`
- You can also use `PYTHONPATH=...` instead of copying if you prefer

