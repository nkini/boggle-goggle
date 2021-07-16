## Words source
TWL06 Scrabble Word List  
https://www.wordgamedictionary.com/twl06/  

## Dice source
http://www.bananagrammer.com/2013/10/the-boggle-cube-redesign-and-its-effect.html  

## How to play
### Autogenerate a board
```
$ python3 main.py
Autogenerate a board (a) or enter a board manually (m): a
Enter board size: 4
Creating 4 x 4 BOARD
D	O	U	T
A	E	G	H
E	L	I	R
Z	T	E	A
Prefix creation took 0.6452670097351074 seconds.
There are 279105 prefixes.
Possible words:
{'ado',
 'aerie',
 'aeried',
...
 'ugh',
 'uglier',
 'zeal',
 'zee'}
Num words in solution: 188
Num words checked: 3122
Total time elapsed: 13.786962985992432
D	O	U	T
A	E	G	H
E	L	I	R
Z	T	E	A
```

### Manually enter a board
```
$ python3 main.py
Autogenerate a board (a) or enter a board manually (m): m
Enter the board: gtna wexv dnsh ajtu
G	T	N	A
W	E	X	V
D	N	S	H
A	J	T	U
Prefix creation took 0.672652006149292 seconds.
There are 279105 prefixes.
Possible words:
{'adnexa',
 'and',
 'ane',
...
 'went',
 'west',
 'wet'}
Num words in solution: 85
Num words checked: 1133
Total time elapsed: 4.8889548778533936
G	T	N	A
W	E	X	V
D	N	S	H
A	J	T	U
```

## Programming notes
- Interestingly, `get_prefixes` takes longer if the twl06-prefixes.json already exists than when it gets created!
