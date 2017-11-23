# Interprocess Communication
There is whole chapter about it in Tanenbaum.

## Lock, Mutex, Semaphore
* **Lock** allows only one thread to enter the part that's locked and the lock is not shared with any other processes.
* **Mutex** is the same as a lock but it can be system wide (shared by multiple processes).
* **Semaphore** does the same as a mutex but allows x number of threads to enter.

---

* [concurrency - Lock, mutex, semaphore... what's the difference? - Stack Overflow](http://stackoverflow.com/questions/2332765/lock-mutex-semaphore-whats-the-difference)
* [What is the difference between a mutex and a semaphore? - Quora](https://www.quora.com/What-is-the-difference-between-a-mutex-and-a-semaphore)
