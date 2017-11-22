# Pro Tips
---

#### Example of clean Google search link
`https://www.google.com/search?q=Google+tutorial+create+link`

---

Am I set up on track?
`git branch -vv`
[how do I get git to show me which branches are tracking what? - Stack Overflow](http://stackoverflow.com/questions/4950725/how-do-i-get-git-to-show-me-which-branches-are-tracking-what)

---

#### Places to search besides google
* github and gist, also use `stars:>1000`
* stackoverflow and stackexchange most voted answers on some tag
* quora
* [hacker news](https://hn.algolia.com)
* reddit
* medium ([freeCodeCamp](https://medium.freecodecamp.org/search) and [Hacker Noon](https://hackernoon.com/search))
* If sb writes a good answer on stackowerflow/quora -> check their github/twitter/other answers
* Reddit / Quora / StackExchange - Top Q&A
    - Чуваков которые дают крутые ответы пробивать (их другие ответы, их гитхаб, твиттер)
* habrahabr / geektimes

---

Using 2FA on GitHub causes some troubles with pushing to gist via GitHub Desktop or via https-clone. So clone via SSH. Then you can add it to GitHub Desktop.

---

run shell scripts from string: `sudo sh -c “softwareupdate -ia && reboot”`

---

- [How to boot your Mac in Verbose Mode](http://www.idownloadblog.com/2015/08/17/how-to-boot-your-mac-in-verbose-mode/)

---

`touch test_{1..13}.txt`
`rm *.png *.txt`
---

- [Syntax highlighting in nano on Mac OS X](https://gist.github.com/BlakeGardner/5587269)

---

#### Encrypt and Decrypt any file from terminal
Encrypt:

`openssl enc -aes-256-cbc -e -in {file-in} -out {file-out}`

Dencrypt:

`openssl enc -aes-256-cbc -d -in {file-in} -out {file-out}`

You can drag and drop files to terminal for speed.

---

#### Get some information about host
curl $(host github.com | head -1 | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' |  awk '{print "ipinfo.io/" $1}')

---
