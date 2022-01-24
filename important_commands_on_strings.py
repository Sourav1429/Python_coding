Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string
>>> "abc DEF".capitalize()
'Abc def'
>>> "abc.DEF".capitalize()
'Abc.def'
>>> a="abcdef"
>>> a.center()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.center()
TypeError: center() takes at least 1 argument (0 given)
>>> a.center(0)
'abcdef'
>>> print('*','abcdef'.center(7),'*')
*  abcdef *
>>> print('*','abcdef'.center(7),'*',sep='')
* abcdef*
>>> print("abcdef".center(7,1))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("abcdef".center(7,1))
TypeError: The fill character must be a unicode character, not int
>>> print("abcdef".center(7,'1'))
1abcdef
>>> print("abcdef".center(10,'12'))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("abcdef".center(10,'12'))
TypeError: The fill character must be exactly one character long
>>> print('*',"abcde".center(6),'*',sep='')
*abcde *
>>> 
