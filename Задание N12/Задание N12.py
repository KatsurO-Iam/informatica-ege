# for n in range(3, 10000):
#     s = '5' + '2'*n
#     while '52' in s or '2222' in s or '1122' in s:
#         s = s.replace('52', '11', 1)
#         s = s.replace('2222', '5', 1)
#         s = s.replace('1122', '25', 1)
#         a = sum([int(x) for x in s])
#     if a == 64:
#         print(n)
#         break

# s = '123' * 30
# while '21' in s or '23' in s:
#     if '21' in s:
#         s = s.replace('21', '11')
#     else:
#         s = s.replace('23', '21')
#
# print(s.count('1'))

# s = '1' + '0' * 90
# while '1' in s:
#     if '10' in s:
#         s = s.replace('10', '0001',1)
#     else:
#         s =s.replace('1','000', 1)
#
# print(s.count('0'))

# s = "543"*30
# while '43' in s or '53' in s:
#     if '43' in s:
#         s = s.replace('43', '33', 1)
#     else:
#         s = s.replace('53', '433', 1)
#
# print(s.count('3'))
# k = 0
# for i in range(234567900, 789012346):
#     s = '1' * i
#     while '111' in s:
#         s = s.replace('111', '2')
#         s = s.replace('222', '11')
#         s = s.replace('1', '2')
#     if len(s) == 3:
#         k+=1
# print(k)

# def f(l):
#     summ = 0
#     for i in range(0, len(l)):
#         summ+= int(l[i])
#     return summ
#
# for n in range(4, 10000):
#     s = '1' * n + '7'
#     while '117' in s or '17' in s:
#         if '117' in s:
#             s = s.replace('117', '73')
#         else:
#             s = s.replace('17', '1117')
#     a = f(s)
#     if a==22:
#         print(n)
#         break
#
# def process_string(s):
#     while '117' in s or '17' in s:
#         if '117' in s:
#             s = s.replace('117', '73', 1)
#         else:
#             s = s.replace('17', '1117', 1)
#     return s
#
# def sum_digits(s):
#     return sum(int(d) for d in s)
#
# for n in range(5, 10000):
#     input_str = '1' * n + '7'
#     result_str = process_string(input_str)
#     if sum_digits(result_str) == 22:
#         print(n)
#         break

# for a in range(80):
#     for b in range(80):
#         for c in range(80):
#             s = '>' + '1'* a + '2' * b + '3' * c
#             while '>1' in s or '>2' in s or '>3' in s:
#                 s = s.replace('>1', '21>3', 1)
#                 s = s.replace('>2', '32>', 1)
#                 s = s.replace('>3', '11>2', 1)
#             if s.count('1') == 71 and s.count('2') == 54 and s.count('3') == 31:
#                 print(b)
#                 break
# maxx = []
# for i in range(3, 10000):
#     s = '8' + '5'*i
#     while '8858' in s or '555' in s:
#         if '8858' in s:
#             s = s.replace('8858', '4')
#         else:
#             s = s.replace('555', '58')
#         if '5858' in s:
#             s = s.replace('5858', '85')
#
#     summ = sum([int(x) for x in s])
#     if summ == 66:
#         maxx.append(i)
#
# print(max(maxx))

# s = '9.txt' * 134
#
# while '22222' in s or '9999' in s:
#     if '22222' in s:
#         s = s.replace('22222', '99',1)
#     else:
#         s = s.replace('9999', '2',1)
#
# print(s)

