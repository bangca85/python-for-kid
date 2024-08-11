'''
Bài tập 7: Tạo danh bạ điện thoại

**Yêu cầu:** Viết chương trình tạo một danh bạ điện thoại và cho phép người dùng tra cứu số điện thoại.

**Input:**

```python
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}
name = "Alice"
```

**Output:**

```python
Số điện thoại của Alice: 123-456-7890
```
'''
def lookup_phone_number(phonebook, name):
    return phonebook.get(name, "Không tìm thấy số điện thoại")

phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}
name = "Alice"
phone_number = lookup_phone_number(phonebook, name)
print(f"Số điện thoại của {name}: {phone_number}")
