"""
Question 078 - Level 03
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
Hints: Use zlib.compress() and zlib.decompress() to compress and decompress a string.
"""
import zlib

s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s.encode("utf-8"))
print(t)
print(zlib.decompress(t))
