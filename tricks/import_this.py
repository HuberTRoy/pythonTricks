import this

"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

"""
Wondering how this is implemented behind the scenes? Here's a good summary: 
https://stackoverflow.com/questions/5855758/what-is-the-source-code-of-the-this-module-doing?__s=x3s3zbg8b4xsmfzt6ct3
"""
"""
√
This is called rot13 encoding:
···
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
···

Builds the translation table, for both uppercase (this is what 65 is for) and lowercase (this is what 97 is for) chars.
···
print "".join([d.get(c, c) for c in s])
···
Prints the translated string.
"""