Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={0:'A',1:'B',2:'C'}
>>> for i,j in a.items():
	print(i,j," ")

	
0 A  
1 B  
2 C  
>>> print(a.get(1,4))
B
>>> print(a.get(5,4))
4
>>> print(a.setdefault(3))
None
>>> print(a.setdefault(2))
C
>>> a.setdefault(4,"D")
'D'
>>> print(a)
{0: 'A', 1: 'B', 2: 'C', 3: None, 4: 'D'}
>>> b={3:'f',9:'g'}
>>> a.update(b)
>>> print(a)
{0: 'A', 1: 'B', 2: 'C', 3: 'f', 4: 'D', 9: 'g'}
>>> b=a.copy()
>>> b
{0: 'A', 1: 'B', 2: 'C', 3: 'f', 4: 'D', 9: 'g'}
>>> b[2]='D'
>>> b
{0: 'A', 1: 'B', 2: 'D', 3: 'f', 4: 'D', 9: 'g'}
>>> a.clear()
>>> a
{}
>>> a={2:'d',2:'f'}
>>> a
{2: 'f'}
>>> a.pop(2)
'f'
>>> print(a)
{}
>>> a={1:5,2:3,3:4}
>>> print(a.pop(4,9))
9
>>> a.items()
dict_items([(1, 5), (2, 3), (3, 4)])
>>> 
