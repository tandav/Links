# Managing Free Memory
Динамическое распределение памяти - когда она выделяется по мере необходимости. 

2 common ways OS do it: Bitmaps and Linked Lists.

### Bitmaps
Memory is divided into allocation blocks. Each block corresponding to 0 (block is free) or 1(block is occupied).

![FULL DESCR. and SCHEME](https://cloud.githubusercontent.com/assets/5549677/25071287/b20e37a0-22bb-11e7-84f3-cd6be92b6b7e.png)

### Linked Lists
A linked list of allocated and free memory segments, where a segment either contains a process (P) or is an empty hole (H) between two processes 

Each entry in the list specifies a hole (H) or process (P), the address at which it starts, the length, and a pointer to the next item. 

--- Adnvanced Level Below ---

list is kept sorted by address 

algorithms can be used to allocate memory for a created process (or an existing process being swapped in from disk). 

* first fit
	* scans along the list of segments until it finds a hole that is big enough  
* next fit
* best fit
* worst fit
