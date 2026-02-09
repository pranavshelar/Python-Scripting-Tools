import sys
import threading
import queue
from hashlib import md5, sha1, sha256
from datetime import datetime


SUPPORTED_HASHES = {
    "md5": md5,
    "sha1": sha1,
    "sha256": sha256
}
print(type(SUPPORTED_HASHES["md5"]))

def load_wordlist(path, q):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                q.put(line.strip())
    except FileNotFoundError:
        print(" Wordlist file not found")
        sys.exit()

def worker(hash_func, target_hash, q, stop_event, result):
    while not stop_event.is_set():
        try:
            password = q.get_nowait()
        except queue.Empty:
            return

        hashed = hash_func(password.encode()).hexdigest()

        if hashed == target_hash:
            result["password"] = password
            stop_event.set()
            return

        q.task_done()

def main():
    print("Hash Cracker (MD5 / SHA1 / SHA256)")
    print("-" * 50)

    target_hash = input("Enter hash: ").strip()
    hash_type = input("Enter hash type (md5, sha1, sha256): ").strip().lower()

    if hash_type not in SUPPORTED_HASHES:
        print("[-] Unsupported hash type")
        sys.exit(1)

    wordlist_path = input("Enter wordlist path: ").strip()
    thread_count = int(input("Enter number of threads: ").strip())

    q = queue.Queue()
    load_wordlist(wordlist_path, q)

    stop_event = threading.Event()
    result = {}

    threads = []
    hash_func = SUPPORTED_HASHES[hash_type]

    start_time = datetime.now()

    for _ in range(thread_count):
        t = threading.Thread(
            target=worker,
            args=(hash_func, target_hash, q, stop_event, result),
            daemon=True
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = datetime.now()

    print("=" * 50)
    if "password" in result:
        print(f"[+] Hash cracked: {result['password']}")
    else:
        print("[-] Password not found")

    print(f"Time taken: {end_time - start_time}")

if __name__ == "__main__":
    main()
