# Memory
## Intro
* **memory hierarchy** - RAM + HDD. small-and-fast + big-and-slow
* **memory manager / dispatcher** - The part of the OS that manages the memory hierarchy 
	* Its job is to efficiently manage memory: keep track of which parts of memory are in use, allocate memory to processes when they need it, and deallocate it when they are done. 

## No Abstraction Memory
Предоставление процессам полного доступа к памяти (напрямую по физическим адресам). Процессы могут запускаться только по одному. Более точно - в оперативной памяти может находиться только один процесс, остальные ждут на HDD. 

## Address Spaces
* An **address space** is the set of addresses that a process can use to address memory. 
* Each process has its own address space, independent of those belonging to other processes (except in some special cases where processes want to share their address spaces).
* **base** and **limit** registers
	* весьма примитивная версия динамического перераспределения памяти. Адресное пространство каждого процесса просто проецируется на различные части физической памяти. **Оснащение каждого CPU двумя специальными аппаратными регистрами, которые обычно называются базовым и ограничительным регистрами.**
	* При использовании этих регистров программы загружаются в последовательно расположенные свободные области памяти без модификации адресов в процессе загрузки (см. рис. 3.2, в). При запуске процесса в **базовый** регистр загружается физический адрес, с которого начинается размещение программы в памяти, а в **ограничительный** регистр загружается длина программы.

## [Managing Free Memory](managing-free-memory.md)
## [Virtual Memory](virtual-memory.md)
## Raw Links
* [What and where are the stack and heap? - Stack Overflow](http://stackoverflow.com/questions/79923/what-and-where-are-the-stack-and-heap)
