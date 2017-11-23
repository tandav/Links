# Protection Domains
* **domain** is a set of (object, rights) pairs 
	* objects - eg files, printers, devices
	* rights - e.g. Read, Write, eXecute 
	* often domains are users, but not always
	* **UID**: User ID **GID**: Group ID
		* domain in UNIX - pair (UID, GID)
		* Two processes with the same (UID, GID) combination will have access to exactly the same set of objects 

## Protection Matrix
* Rows - Domains, Columns - Objects
* Each matrix-box contains the rights of that domain for that object
* Переключение между доменами также может быть включено в ту же табличную модель, если в качестве объекта представить сам домен, в отношении которого может быть разрешена операция входа — enter 

![scheme](https://cloud.githubusercontent.com/assets/5549677/25082253/3dcf9f6c-2358-11e7-8386-62bca6781fba.png)

* На практике редко юзается, т.к эта матрица часто полупустая. Часто юзаются либо строки, либо столбцы этой матрицы

## Access Control Lists (ACL) (столбцы матрицы)
* Each object/file has ACL, содержащий все domains/users, которым разрешен доступ к данному объекту, а также тип доступа. 
* ACL Example: **File1:  A: R; B: RW; C:RX**
* ABC - users, R - Read, W - Write, X - eXecute 

## Capability list (C-List) (строки матрицы)
* ну типа **Domain1: File1:R, File2:W,     Domain2: File1:RX, File2:W**
