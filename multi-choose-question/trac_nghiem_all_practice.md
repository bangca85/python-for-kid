
1. **Kết quả của đoạn mã sau là gì?**

   ```python
   x = 10
   y = 5
   z = x + y
   print(z)
   ```

   - a) 10
   - b) 15
   - c) 5
   - d) Lỗi
2. **Đoạn mã sau có lỗi không?**

   ```python
   a = 10
   b = "5"
   c = a + b
   ```

   - a) Có, vì không thể cộng số nguyên với chuỗi
   - b) Không, c sẽ là 105
   - c) Không, c sẽ là "10 + 5"
   - d) Không, c sẽ là "15"
3. **Kết quả của đoạn mã sau là gì?**

   ```python
   a = 2
   a = a * 3
   a = a - 5
   print(a)
   ```

   - a) 1
   - b) 6
   - c) 5
   - d) 0
4. **Kết quả của đoạn mã sau là gì?**

   ```python
   x = 10
   x += 5
   print(x)
   ```

   - a) 5
   - b) 10
   - c) 15
   - d) Lỗi
5. **Kết quả của đoạn mã sau là gì?**

   ```python
   x = 5
   y = x
   x = 10
   print(y)
   ```

   - a) 5
   - b) 10
   - c) 15
   - d) Lỗi
6. **Kết quả của đoạn mã sau là gì?**

   ```python
   for i in range(3):
       print(i)
   ```

   - a) 0 1 2
   - b) 1 2 3
   - c) 0 1 2 3
   - d) 1 2 3 4
7. **Kết quả của đoạn mã sau là gì?**

   ```python
   i = 0
   while i < 3:
       print(i)
       i += 1
   ```

   - a) 0 1 2
   - b) 1 2 3
   - c) 0 1 2 3
   - d) 1 2
8. **Kết quả của đoạn mã sau là gì?**

   ```python
   for i in range(5, 10):
       print(i)
   ```

   - a) 5 6 7 8 9 10
   - b) 5 6 7 8 9
   - c) 6 7 8 9 10
   - d) 4 5 6 7 8 9
9. **Kết quả của đoạn mã sau là gì?**

   ```python
   for i in range(3):
       for j in range(2):
           print(i, j)
   ```

   - a) 0 1 2 3 4 5
   - b) 0 0 0 1 1 0 1 1
   - c) 0 0 0 1 1 0 1 1 2 0 2 1
   - d) 0 1 0 1 0 1
10. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 0
    while x < 5:
        x += 1
    print(x)
    ```

    - a) 0
    - b) 4
    - c) 5
    - d) Lỗi
11. **Kết quả của đoạn mã sau là gì?**

    ```python
    for i in range(2):
        for j in range(2):
            if j == 1:
                break
            print(i, j)
    ```

    - a) 0 0 0 1 1 0 1 1
    - b) 0 0 1 0 1 1
    - c) 0 0 1 0
    - d) 0 0 1 0 1
12. **Kết quả của đoạn mã sau là gì?**

    ```python
    for i in range(3):
        if i == 2:
            continue
        print(i)
    ```

    - a) 0 1 2
    - b) 0 1
    - c) 1 2
    - d) 2 3
13. **Kết quả của đoạn mã sau là gì?**

    ```python
    count = 0
    while count < 3:
        print("Hello")
        count += 1
    ```

    - a) "Hello"
    - b) "Hello" in ra 2 lần
    - c) "Hello" in ra 3 lần
    - d) "Hello" in ra 4 lần
14. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 10
    while x > 0:
        print(x)
        x -= 3
    ```

    - a) 10 7 4 1
    - b) 10 8 6 4 2
    - c) 10 7 4
    - d) 9 6 3 0
15. **Kết quả của đoạn mã sau là gì?**

    ```python
    for i in range(1, 4):
        print(i * "*")
    ```

    - a) *
      **---
    - b) ***
      **
      *
    - c) *
      *
      *
    - d) ***


16. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 5
    if x > 3:
        print("Lớn hơn 3")
    else:
        print("Nhỏ hơn hoặc bằng 3")
    ```

    - a) Lớn hơn 3
    - b) Nhỏ hơn hoặc bằng 3
    - c) Không có gì được in ra
    - d) Lỗi
17. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 10
    if x > 15:
        print("Lớn hơn 15")
    elif x > 5:
        print("Lớn hơn 5")
    else:
        print("Nhỏ hơn hoặc bằng 5")
    ```

    - a) Lớn hơn 15
    - b) Lớn hơn 5
    - c) Nhỏ hơn hoặc bằng 5
    - d) Không có gì được in ra
18. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 10
    y = 20
    if x > y:
        print("x lớn hơn y")
    else:
        print("x không lớn hơn y")
    ```

    - a) x lớn hơn y
    - b) x không lớn hơn y
    - c) Không có gì được in ra
    - d) Lỗi
19. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 5
    if x > 10:
        print("Lớn hơn 10")
    elif x > 3:
        print("Lớn hơn 3")
    else:
        print("Nhỏ hơn hoặc bằng 3")
    ```

    - a) Lớn hơn 10
    - b) Lớn hơn 3
    - c) Nhỏ hơn hoặc bằng 3
    - d) Không có gì được in ra
20. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 3
    y = 5
    if x < y:
        print("x nhỏ hơn y")
    else:
        print("x không nhỏ hơn y")
    ```

- a) x nhỏ hơn y
  - b) x không nhỏ hơn y
  - c) Không có gì được in ra
  - d) Lỗi

21. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 5
    if x % 2 == 0:
        print("Chẵn")
    else:
        print("Lẻ")
    ```

    - a) Chẵn
    - b) Lẻ
    - c) Không có gì được in ra
    - d) Lỗi
22. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 10
    if x == 10:
        print("Bằng 10")
    else:
        print("Không bằng 10")
    ```

    - a) Bằng 10
    - b) Không bằng 10
    - c) Không có gì được in ra
    - d) Lỗi
23. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 15
    if x > 10:
        if x < 20:
            print("Lớn hơn 10 và nhỏ hơn 20")
        else:
            print("Lớn hơn hoặc bằng 20")
    else:
        print("Nhỏ hơn hoặc bằng 10")
    ```

    - a) Lớn hơn 10 và nhỏ hơn 20
    - b) Lớn hơn hoặc bằng 20
    - c) Nhỏ hơn hoặc bằng 10
    - d) Không có gì được in ra
24. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 30
    if x > 10 and x < 40:
        print("x nằm trong khoảng 10 đến 40")
    else:
        print("x không nằm trong khoảng 10 đến 40")
    ```

    - a) x nằm trong khoảng 10 đến 40
    - b) x không nằm trong khoảng 10 đến 40
    - c) Không có gì được in ra
    - d) Lỗi
25. **Kết quả của đoạn mã sau là gì?**

    ```python
    x = 25
    if x > 20 or x < 10:
        print("x lớn hơn 20 hoặc nhỏ hơn 10")
    else:
        print("x nằm trong khoảng 10 đến 20")
    ```

    - a) x lớn hơn 20 hoặc nhỏ hơn 10
    - b) x nằm trong khoảng 10 đến 20
    - c) Không có gì được in ra
    - d) Lỗi
26. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [1, 2, 3, 4]
    print(my_list[2])
    ```

    - a) 1
    - b) 2
    - c) 3
    - d) 4
27. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [5, 6, 7, 8]
    print(my_list[-1])
    ```

    - a) 5
    - b) 6
    - c) 7
    - d) 8
28. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)
    ```

    - a) `[1, 2, 3, 4]`
    - b) `[4, 1, 2, 3]`
    - c) `[1, 2, 3]`
    - d) `[1, 2, 3, [4]]`
29. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [1, 2, 3, 4, 5]
    print(len(my_list))
    ```

    - a) 4
    - b) 5
    - c) 6
    - d) 3
30. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [1, 2, 3]
    my_list.insert(1, 4)
    print(my_list)
    ```

    - a) `[1, 4, 2, 3]`
    - b) `[4, 1, 2, 3]`
    - c) `[1, 2, 3, 4]`
    - d) `[1, 2, 4, 3]`
31. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [1, 2, 3, 4]
    my_list.remove(3)
    print(my_list)
    ```

    - a) `[1, 2, 4]`
    - b) `[1, 2, 3, 4]`
    - c) `[1, 3, 4]`
    - d) `[2, 3, 4]`
32. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [1, 2, 3]
    my_list[1] = 10
    print(my_list)
    ```

    - a) `[1, 10, 3]`
    - b) `[10, 2, 3]`
    - c) `[1, 2, 10]`
    - d) `[10, 1, 3]`
33. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [1, 2, 3, 4]
    print(my_list[1:3])
    ```

    - a) `[1, 2]`
    - b) `[2, 3]`
    - c) `[3, 4]`
    - d) `[2, 3, 4]`
34. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [10, 20, 30]
    my_list.reverse()
    print(my_list)
    ```

    - a) `[30, 20, 10]`
    - b) `[10, 20, 30]`
    - c) `[20, 30, 10]`
    - d) `[10, 30, 20]`
35. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_list = [3, 1, 2]
    my_list.sort()
    print(my_list)
    ```

    - a) `[1, 2, 3]`
    - b) `[3, 2, 1]`
    - c) `[2, 3, 1]`
    - d) `[1, 3, 2]`
36. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (1, 2, 3)
    print(my_tuple[1])
    ```

    - a) 1
    - b) 2
    - c) 3
    - d) Lỗi
37. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (4, 5, 6)
    print(len(my_tuple))
    ```

    - a) 2
    - b) 3
    - c) 4
    - d) Lỗi
38. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (7, 8, 9)
    print(my_tuple[-1])
    ```

    - a) 7
    - b) 8
    - c) 9
    - d) Lỗi
39. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (1, 2, 3)
    my_tuple[1] = 10
    print(my_tuple)
    ```

    - a) `[1, 10, 3]`
    - b) `(1, 10, 3)`
    - c) `[1, 2, 3]`
    - d) Lỗi
40. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple =

    ```

 (1, 2, 3)
    print(my_tuple[1:3])
    ```
    - a) `(1, 2)`
    - b) `(2, 3)`
    - c) `[2, 3]`
    - d) `[1, 2, 3]`

41. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (1, 2, 3)
    print(4 in my_tuple)
    ```
    - a) True
    - b) False
    - c) Lỗi
    - d) Không có gì được in ra
42. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (5,)
    print(type(my_tuple))
    ```
    - a) `<class 'tuple'>`
    - b) `<class 'int'>`
    - c) `<class 'list'>`
    - d) `<class 'dict'>`
43. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (1, 2, 3, 4)
    print(my_tuple[::2])
    ```
    - a) `(1, 2)`
    - b) `(2, 4)`
    - c) `(1, 3)`
    - d) `[1, 3]`
44. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (1, 2, 3)
    print(my_tuple + (4, 5))
    ```
    - a) `(1, 2, 3, 4, 5)`
    - b) `(4, 5, 1, 2, 3)`
    - c) `[1, 2, 3, 4, 5]`
    - d) `[4, 5, 1, 2, 3]`
45. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_tuple = (1, 2, 3)
    a, b, c = my_tuple
    print(a, b, c)
    ```
    - a) 1 2 3
    - b) 3 2 1
    - c) 2 3 1
    - d) Lỗi
46. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(my_dict["b"])
    ```
    - a) 1
    - b) 2
    - c) 3
    - d) Lỗi
47. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(len(my_dict))
    ```
    - a) 2
    - b) 3
    - c) 4
    - d) Lỗi
48. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2}
    my_dict["c"] = 3
    print(my_dict)
    ```
    - a) `{"a": 1, "b": 2}`
    - b) `{"a": 1, "b": 2, "c": 3}`
    - c) `{"c": 3, "a": 1, "b": 2}`
    - d) Lỗi
49. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2, "c": 3}
    del my_dict["b"]
    print(my_dict)
    ```
    - a) `{"a": 1, "b": 2}`
    - b) `{"a": 1, "c": 3}`
    - c) `{"b": 2, "c": 3}`
    - d) Lỗi
50. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2, "c": 3}
    print("d" in my_dict)
    ```
    - a) True
    - b) False
    - c) Lỗi
    - d) Không có gì được in ra
51. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(my_dict.get("d", 4))
    ```
    - a) 1
    - b) 2
    - c) 4
    - d) Lỗi
52. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2}
    my_dict.update({"b": 3})
    print(my_dict)
    ```
    - a) `{"a": 1, "b": 2}`
    - b) `{"a": 1, "b": 3}`
    - c) `{"b": 3, "c": 4}`
    - d) Lỗi
53. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2}
    print(my_dict.keys())
    ```
    - a) `["a", "b"]`
    - b) `("a", "b")`
    - c) `dict_keys(["a", "b"])`
    - d) Lỗi
54. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2}
    print(my_dict.values())
    ```
    - a) `[1, 2]`
    - b) `(1, 2)`
    - c) `dict_values([1, 2])`
    - d) Lỗi
55. **Kết quả của đoạn mã sau là gì?**

    ```python
    my_dict = {"a": 1, "b": 2}
    print(my_dict.items())
    ```
    - a) `[("a", 1), ("b", 2)]`
    - b) `{("a", 1), ("b", 2)}`
    - c) `dict_items([("a", 1), ("b", 2)])`
    - d) Lỗi
