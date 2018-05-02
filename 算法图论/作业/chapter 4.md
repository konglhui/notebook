# chapter 4

## 4.1

请编写前述sum函数的代码。    

```python
def sum(arr):
	if arr == []:
		return 0
	else :
		return arr[0] + sum(arr[1:])

print(sum([1,2,3,4]))
```
## 4.2

编写一个递归函数来计算列表包含的元素数。    

```python
def sum(arr):
	if arr == []:
		return 0
	else :
		return 1 + sum(arr[1:])

print(sum([1,2,3,4]))
```

## 4.3
找出列表中最大的数字。

```python
def sum(arr):
	if arr == []:
		return 0
	else :
		return 1 + sum(arr[1:])

print(sum([1,2,3,4]))
```
