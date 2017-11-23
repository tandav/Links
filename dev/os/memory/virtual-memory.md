# Memory

Virtual memory is a method where each process is given its own address space (virtual memory), and the hardware translates every VM reference to a physical memory address. 

An **address space** is the set of addresses that a process can use to address memory. Each proc- ess has its own address space, independent of those belonging to other processes (except in some special circumstances where processes want to share their address spaces).

`Process → Virtual Memory / Address Space → MMU (Memory Management Unit) → Physical memory`

Both virtual and physical uses addresses.

Mapping from virtual to physical address is done by the memory management unit (MMU) which is a hardware device. 

* [What is virtual memory? - Super User](https://superuser.com/questions/42854/what-is-virtual-memory)
* [Why do we need virtual memory? - Stack Overflow](http://stackoverflow.com/questions/19349572/why-do-we-need-virtual-memory)
* [memory segments and physical RAM - Stack Overflow](http://stackoverflow.com/questions/28278319/memory-segments-and-physical-ram?rq=1)
* [more info on Memory layout of an executable program (process) - Stack Overflow](http://stackoverflow.com/questions/1966920/more-info-on-memory-layout-of-an-executable-program-process)
* [What's the difference between "virtual memory" and "swap space"? - Stack Overflow](http://stackoverflow.com/questions/4970421/whats-the-difference-between-virtual-memory-and-swap-space?rq=1)

## Paging
Nearly all implementations of virtual memory divide a virtual address space into pages, blocks of contiguous virtual memory addresses. Pages on contemporary systems are usually at least 4 kilobytes in size;

Page tables are used to translate the virtual addresses into physical addresses.

Similarly, main memory is divided into small fixed-sized blocks of (physical) memory called frames and the size of a frame is kept the same as that of a page to have optimum utilization of the main memory and to avoid external fragmentation.

![paging](https://www.tutorialspoint.com/operating_system/images/paging.jpg)

![screen shot 2017-04-05 at 13 40 41](https://cloud.githubusercontent.com/assets/5549677/24701999/82588010-1a05-11e7-92de-887cd76da9fc.png)

[Структура записи в таблице страниц · Morozov-5F/operational-system-docs Wiki](https://github.com/Morozov-5F/operational-system-docs/wiki/%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8-%D0%B2-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B5-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86)


## Swapping
To accommodate situations when more virtual memory is in use than actual physical memory, space on a storage device (the backing store, or swap space or page file) such as HDD, SSD or even thumb drive can be used to "swap out" data and later "swap (back) in" as needed. The swapped data is usually in data lengths called pages, but there are alternate schemes that use variable length segments or even paged segments.

Memory at a virtual address can be "paged out" to disk, and then "paged in" when it is accessed again.

* [Difference Swapping and Paging - Stack Overflow](http://stackoverflow.com/questions/4415254/difference-swapping-and-paging)
* [What's the difference between operating system "swap" and "page"? - Stack Overflow](http://stackoverflow.com/questions/1688962/whats-the-difference-between-operating-system-swap-and-page)
