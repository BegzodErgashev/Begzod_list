# # list1
# def toq(n):
#     n = 8
#     a = []
#     for i in range(1, 2 * n, 2):
#         a.append(i)
#     return a
#
#
# print(toq(8))

# # list2
# n = 10
# a = []
# x = 1
# for i in range(n + 1):
#     x *= 2
#     a.append(x)
#     print(a)

# list3

# a = 3
# d = 5
# n = 10
# s = []
# for i in range(n + 1):
#     s.append(a)
#     a += d
#     print(s)

# # list 4
#
# b = 3
# q = 4
# s = []
# n = 6
# for i in range(n + 1):
#     s.append(b)
#     b *= q
#     print(s)

# # list 5
# a = 0
# b = 1
# n = 10
# s = []
# for i in range(n + 1):
#     c = a + b
#     a = b
#     b = c
#     s.append(c)
#     print(s)

#
# # list6
# n = 6
# a = 1
# b = 3
# s = [a, b]
#
# for i in range(1, n + 1):
#     x = a + b
#     s.append(x)
#     a = x
#     b = a
#
#     print(s)

# # list7
#
# n = int(input("n="))
# s = []
# for i in range(n):
#     x = float(input("x="))
#     s.append(x)
# print(s)
# print(s[::-1])

# list8

# n = 6
# s = [4, 5, 7, 3, 22, 11, 8, 6, 9]
# c = []
# k = 0
# for i in s:
#     if i % 2 != 0:
#         k += 1
#         c.append(i)
#         c.sort()
#         print(c)
#         print(k)

# # list9
#
# s = [4, 5, 7, 6, 8, 9, 2, 12, 10]
# c = []
# k = 0
# for i in s:
#     if i % 2 == 0:
#         k += 1
#         c.append(i)
#         c.sort()
#         print(c[::-1])
#         print(k)


# # list10
# s = [4, 10, 64, 78, 15, 23, 63, 5, 7, 8, 6, 9]
# c = []
# x = []
# for i in s:
#     if i % 2 == 0:
#         c.append(i)
#     else:
#         x.append(i)
#
# print("c", c)
# print("x", x[::-1])


# # list10
# a=[7,4,7,3,5,10]
# b = []
# c = []
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         b.append(i)
#         print("b", b)
#     else:
#         c.append(i)
#         print("c", c)
# print("natija", b)
# print("natija", c)


# list19
# a = [2, 1, 3, 4, 15, 5, 6, 77, 5, 1, 9]
# for i in range(1, len(a)):
#     if a[0] < a[len(a) - 1]:
#         if a[0] < a[i] and i != len(a) - 1:
#             c = i
# print(c)

# a = [1,5,4,2,6]
# for i in a:


# # list11
#
# n = [5, 62, 1, 2, 5, 2, 365, 5, 45, 78]
# k = 3
# for i in range(len(n)):
#     if i % 3 == 0:
#         print(i)


# # list18
# n = [6, 8, 5, 8, 6, 3, 2, 5]
# for i in n:
#     if i < n[-1]:
#         print(i)
#         break

# # list20
# n = [7, 9, 3, 1, 5, 8]
# k = 3
# l = 4
# s = 0
# for i in range(len(n)):
#     if i >= k and i <= l:
#         s += n[i]
# print(s)

# # list21
# n = [7, 9, 3, 1, 5, 8]
# k = 3
# l = 4
# m = 0
# s = 0
# for i in range(len(n)):
#     if i >= k and i <= l:
#         m+=1
#         s += n[i]
# print(s/m)

# # list22
# n = [7, 9, 3, 1, 5, 8]
# k = 3
# l = 4
# s = 0
# for i in range(len(n)):
#     if i < k or i > l:
#         print("i", i)
#         s += n[i]
# print(s)

# # list24
# n = [3, 8, 13, 18, 23, 28]
# for i in range(len(n) - 2):
#     if n[i + 1] - n[i] == n[i + 2] - n[i + 1]:
#         d = n[i + 1] - n[i]
# print("Arifmetik progressiya qiladi")
# print(d)

# # list25
# n = [16, 8, 4, 2]
# for i in range(len(n) - 2):
#     if n[i + 1] / n[i] == n[i + 2] / n[i + 1]:
#         q = n[i + 1] / n[i]
# print("Geometrik progressiya qiladi")
# print(q)

# # list26
# n = int(input("n="))
# a = []
# for i in range(n):
#     x = int(input("x="))
#     a.append(x)
# print(x)
# for j in range(len(a)):
#     if a[j] % 2 == 0 and a[j + 1] % 2 != 0 or a[j] % 2 != 0 and a[j + 1] % 2 == 0:
#         print(0)
#     else:
#         print(j + 1)

# # list28
# n = int(input("n="))
# a = []
# b = []
# for i in range(n):
#     x = int(input("x="))
#     a.append(x)
# print(a)
#
# for j in range(1, len(a)):
#     if j % 2 == 0:
#         b.append(a[j])
# b.sort()
# print(b[0])


# # list35
# n = int(input("n="))
# a = []
# b = []
# for i in range(n):
#     x = int(input("x="))
#     a.append(x)
# print(a)
# for j in range(n - 2):
#     if a[j] < a[j + 1] > a[j + 2]:
#         b.append(a[j + 1])
#
# if not b:
#     print(0)
# else:
#     b.sort()
#     print(b)
#     print(b[0])

# # list34
# n = int(input("n="))
# a = []
# b = []
# for i in range(n):
#     x = int(input("x="))
#     a.append(x)
# print(a)
# for j in range(n - 2):
#     if a[j] > a[j + 1] < a[j + 2]:
#         b.append(a[j + 1])
# if not b:
#     print(0)
# else:
#     print(b)
#     b.sort()
#     print(b[-1])

# # list36
# n = int(input("n="))
# a = []
# b = []
# c = []
# d = []
# for i in range(n):
#     x = int(input("x="))
#     a.append(x)
# print(a)
# for j in range(n - 2):
#     if a[j] < a[j + 1] > a[j + 2]:
#         b.append(a[j + 1])
#     elif a[j] > a[j + 1] < a[j + 2]:
#         c.append(a[j + 1])
#     else:
#         print(0)
# if not b and not c:
#     a.sort()
#     print(a[-1])
# else:
#     d.append(a[0])
#     d.append(a[-1])
#     d.sort()
#     print(d[-1])


# # list40
# from math import fabs
#
# r = float(input("r="))
# n = int(input("n="))
# a = []
# b = []
#
# for i in range(n):
#     x = int(input("x="))
#     a.append(x)
# print(a)
# for j in a:
#     z = fabs(r - j)
#     b.append(z)
# print(b)
# q = min(b)
# k = 0
# for w in range(len(a)):
#     if b[w] == q:
#         k = w
#         break
# print(a[k])
#
# n = int(input("n="))
# a = []
# b = []
# c = []
# d = []
# for i in range(n):
#     x = int(input("x="))
#     a.append(x)
# print(a)
# for j in range(n - 1):
#     b.append(a[j] + a[j + 1])
#     print(b)
# s = max(b)
# for r in range(n - 1):
#     if a[r] + a[r + 1] == s:
#         print(r, r + 1)

a = [1, 2, 3, 4, 5, 4, 4, 3, 4, 3, 2, 1, 5, 3, 5, 6, 4, 3, 2, 2, 1]
d = []
k = 0
b = set(a)
print(a)
c = list(b)
print(c)
for i in c:
    for j in range(len(a)):
        if i == a[j]:
            k += 1
    d.append(k)
    k = 0
print(d)
