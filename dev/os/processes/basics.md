# Processes Basics
The ‘‘brain’’ of the computer is the CPU. It fetches instructions from memory and executes them. The basic cycle of every CPU is to fetch the first instruction from memory, decode it to determine its type and operands, execute it, and then fetch, decode, and execute subsequent instructions. The cycle is repeated until the program finishes. In this way, programs are carried out.

A process is basically a program in execution.

## Process Table
Для реализации модели процесса операционная система содержит таблицу (массив структур), называемую таблицей процессов, с одним элементом для каждого процесса. (Эти элементы иногда называют блоками управления процессом.)

### Table Entries
* id
* owner
* priority
* parent process
* pointers to the executable machine code of a process
* state - ready, running, blocked, sleeping etc
* when was the process RUNNING the last time (for scheduler)

**ioppps+t** (last time) (йопс!) - для запоминания
