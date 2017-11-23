# Goals of Scheduling Algorithms
`not very important information`
## All Systems
- равнодоступность — предоставление каждому процессу справедливой доли времени центрального процессора
- принуждение к определенной политике — наблюдение за выполнением уста- новленной политики
- Balance - keeping all parts of the system busy 

## Batch
**About Batch Systems:** Просто типа идут пакеты 1за другим. нет нужды в быстром отклике, приемлемы неприоритетные алгоритмы или приоритетные алгоритмы с длительными периодами для каждого процесса`
- производительность - maximize jobs per hour
- оборотное время — минимизация времени между представлением задачи и ее завершением
- CPU utilization - keep the CPU busy all the time 

## Interactive
**About Interactive Systems:** важна приоритетность,(не дать одному процессу захватить весь CPU)`
- Response time - respond to requests quickly 
- Proportionality - meet users’ expectations // meet - соблюение

## Real-Time
**About Real-Time Systems:** запускаются лишь те программы, которые предназначены для содействия определенной прикладной задаче. процессы запускаются только на непродолжительные периоды времени, do their work quickly and block
- Meeting deadlines - avoid losing data
- Predictability - avoid quality degradation in multimedia systems 
