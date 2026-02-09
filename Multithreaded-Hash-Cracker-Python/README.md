

# 🔐 Multithreaded Hash Cracker (Python)

## Overview

This project is a **multithreaded dictionary-based hash cracker** written in Python.
It attempts to crack password hashes by comparing them against hashes generated from a supplied wordlist.

Supported hash algorithms:

* MD5
* SHA-1
* SHA-256

The tool is designed to demonstrate **offensive security fundamentals**, **thread synchronization**, and **cryptographic hash analysis**, rather than to replace professional tools like Hashcat or John the Ripper.

---

## Features

* Multithreaded cracking using Python `threading`
* Queue-based task distribution (`queue.Queue`)
* Graceful thread termination using `threading.Event`
* Supports user-supplied wordlists
* Measures total cracking time
* Clean exit once the hash is cracked

---

## How It Works

1. Loads a wordlist into a thread-safe queue
2. Spawns multiple worker threads
3. Each thread:

   * Pulls a password candidate from the queue
   * Hashes it using the selected algorithm
   * Compares it with the target hash
4. When a match is found:

   * The result is stored
   * A shared stop signal (`Event`) is set
   * All other threads stop execution

This approach avoids race conditions and unnecessary CPU usage.

---

## Usage

```bash
python hash_cracker.py
```

You will be prompted for:

* Target hash
* Hash type (`md5`, `sha1`, `sha256`)
* Wordlist path
* Number of threads

---

## Example

```text
Enter hash: 5f4dcc3b5aa765d61d8327deb882cf99
Enter hash type (md5, sha1, sha256): md5
Enter wordlist path: rockyou.txt
Enter number of threads: 8
```

---

## Limitations 

This tool **does not defeat modern password storage mechanisms**. Specifically:

* No support for salted hashes
* No adaptive hashing (bcrypt, scrypt, Argon2)
* Dictionary attack only (no rules, masks, or GPU acceleration)

These limitations are intentional and acknowledged.

For real-world cracking, specialized tools should be used.

---

## Why This Project Exists

This project was built to:

* Understand how password hashing works
* Learn multithreading and thread coordination in Python
* Demonstrate how dictionary attacks operate at a low level
* Gain hands-on experience with offensive security tooling

---

