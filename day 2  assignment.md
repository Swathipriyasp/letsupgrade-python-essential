```python
#A list is a container which can hold diffrent data types in it.
lst=["Swathi",15,8790,[9,8,5],"Priya"]
```


```python
lst
```




    ['Swathi', 15, 8790, [9, 8, 5], 'Priya']




```python
lst[0]
```




    'Swathi'




```python
lst[3][1]
```




    8




```python
lst.append("sumiya")
```


```python
lst
```




    ['Swathi', 15, 8790, [9, 8, 5], 'Priya', 'sumiya']




```python
lst.index(15)
```




    1




```python
lst[-1]
```




    'sumiya'




```python
lst[-4]
```




    8790




```python
lst[4]
```




    'Priya'




```python
lst[3][2]
```




    5




```python
#It is complex,this is a key value pair data structure
```


```python
dit={"name ":"Swathipriya","age":"20","phone number":"123456789"}
```


```python
dit
```




    {'name ': 'Swathipriya', 'age': '20', 'phone number': '123456789'}




```python
dit.items()
```




    dict_items([('name ', 'Swathipriya'), ('age', '20'), ('phone number', '123456789')])




```python
dit.keys()
```




    dict_keys(['name ', 'age', 'phone number'])




```python
dit
```




    {'name ': 'Swathipriya', 'age': '20', 'phone number': '123456789'}




```python
dit["School"]="GEMS"
```


```python
dit
```




    {'name ': 'Swathipriya',
     'age': '20',
     'phone number': '123456789',
     'School': 'GEMS'}




```python
type(dit)
```




    dict




```python
#sets are used for string unique values in the python
```


```python
st={"kumari","Google",1,1,2,4,8,5,2,9}
```


```python
st
```




    {1, 2, 4, 5, 8, 9, 'Google', 'kumari'}




```python
st2={"Google",2}
```




```python
st2.issubset(st)
```




    True




```python
#tuples are ordered immutable collection of objects
```


```python
tup=("Swathi","%","swathi@com")
```


```python
tup
```




    ('Swathi', '%', 'swathi@com')




```python
tup.count("%")
```




    1




```python
tup.index("swathi@com")
```




    2




```python
#String is  ordered sequence of characters
```


```python
name="Swathi"
name1="Soumya"
```


```python
name1
```




    'Soumya'




```python
name+" "+name1
```




    'Swathi Soumya'




```python
type(name)
```




    str




```python

```
