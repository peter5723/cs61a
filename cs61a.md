# cs61a,学Python啦

## 1.Ubuntu

Here is a summary of the commands we just went over for your reference:

- ls: **l**i**s**ts     all files in the current directory
- cd     <path to directory>: **c**hange     into the specified **d**irectory
- mkdir     <directory name>: **m**a**k**e a new **dir**ectory with the given name
- mv     <source path> <destination path>: **m**o**v**e the     file at the given source to the given destination

 

来自 <https://cs61a.org/lab/lab00/#backup-setups> 

Windows

On Windows, first change into your main home directory.

cd /mnt/c/Users/

Now try the ls command from earlier. You should see a few folders. One of those folders should match your username. For example, assuming your username is OskiBear, you should see a folder named OskiBear. Let's change into that folder:

cd /mnt/c/Users/Peter/Desktop/cs61a

 

来自 <https://cs61a.org/lab/lab00/#backup-setups> 

## 2. function



```python
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
>>> a_plus_abs_b(2, 3)
5
>>> a_plus_abs_b(2, -3)
5

if b < 0:
    f = sub
else:
    f = add  #注意这章学的，就是函数也可以看做是value
return f(a, b)
```

## 3. control

assignment赋值 parameter参数

if语句

```python
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()


def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())


def cond():
    "*** YOUR CODE HERE ***"
    return False
    

def true_func():
    "*** YOUR CODE HERE ***"
    print("Welcome to")
    

def false_func():
    "*** YOUR CODE HERE ***"
    return print("61A")


#此题的关键在于函数在读取形参时就已经返回值了，就已经执行了print函数，然后才得到true_func()=None，然后false_func=print("61A"),接下来才是执行函数判断
#而语句则直接执行判断，因为是false于是直接跳过了

```

![image-20220130215744386](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220130215744386.png)

同理：就是你要先计算所有的参数再执行函数，如果x=0就直接错误了。

但是，也有可以做的方法，实在想用函数的话：

```python
def if_func(then_expr,condition,else_expr):
    return then_expr() if condition else else_expr()

x=1
res = if_func(lambda:1/x,x>0,lambda:0)
#此函数if_func符合：括号里面的参数是函数，先计算得到的是一个函数，然后返回的是具体的值
```



## 4. high-order  function

```python
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print_sums(1)(3)(5)
```

高阶函数如何执行？`print_sums(1)(3)(5)`从左到右，一步步看即可，注意`print_sums(1)`是个函数，`print_sums(1)(3)`也是函数……以此类推`print_sums(1)(3)(5)(7)(9)……`可以一直写下去

![image-20220131224541580](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220131224541580.png)

模拟网址：[Online Python Tutor - Composing Programs - Python 3](https://pythontutor.com/composingprograms.html#mode=edit)

## 5、lambda函数

```python
d= lambda f: f(4)
def square(x):
    return x*x
print(d(square))
#此题是想说函数也可以作为lambda的参数，冒号后面是该被表示的函数返回的值
```

![image-20220206203955330](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220206203955330.png)

![image-20220206205908904](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220206205908904.png)

We can similarly use the same two functions to compute powers of other numbers. Currying allows us to do so without writing a specific function for each number whose powers we wish to compute.

In the above examples, we manually performed the currying transformation on the `pow` function to obtain `curried_pow`. Instead, we can define functions to automate currying, as well as the inverse *uncurrying* transformation:

```python
>>> def curry2(f):
        """Return a curried version of the given two-argument function."""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g
>>> def uncurry2(g):
        """Return a two-argument version of the given curried function."""
        def f(x, y):
            return g(x)(y)
        return f
>>> pow_curried = curry2(pow)
>>> pow_curried(2)(5)
32
>>> map_to_range(0, 10, pow_curried(2))
1
2
4
8
16
32
64
128
256
512
```

## 6、recursion

例题一

```python
def get_next_coin(coin):
    """Return the next coin. 
    >>> get_next_coin(1)
    5
    >>> get_next_coin(5)
    10
    >>> get_next_coin(10)
    25
    >>> get_next_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(change,smallest_coin):
        if smallest_coin==None:
            return 0
        if change<smallest_coin:#这道换零钱的题目写了两个小时，其实递归表达式早就写对了，但是这个递归出口一直没对，找了很久，要重视啊
            return 0
        elif change==smallest_coin:
            return 1
        return helper(change-smallest_coin,smallest_coin) + helper(change,get_next_coin(smallest_coin))#从小到大，从大到小都没问题，根据题意来
       
    return helper(change,1)
#这道题，利用辅助函数helper来增加所需要的变量
```

例题二：

```python
def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> pawssible_patches("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> pawssible_patches("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> pawssible_patches("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit<0:
        return 0
    if len(start)==0 or len(goal)==0:
        return max(len(start),len(goal))
    elif start[0]==goal[0]:
        return pawssible_patches(start[1:],goal[1:],limit)
    else:
        add=pawssible_patches(start,goal[1:],limit-1)
        jian=pawssible_patches(start[1:],goal,limit-1)
        ti=pawssible_patches(start[1:],goal[1:],limit-1)
        return min(add,min(jian,ti))+1
    """"这个递归好好看看。类似于走迷宫""""
```

## 7、decorator （没看懂）

![image-20220209210750001](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220209210750001.png)

![image-20220209210806981](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220209210806981.png)

## 8、object

### 1、基本概念

![image-20220217135425199](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220217135425199.png)

### 2、class（类）

![image-20220217135548466](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220217135548466.png)

```python
# Define a new type of data
class Product:

    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self._name = name
        self._price = price
        self._nutrition_info = nutrition_info
        self._inventory = 0

    # Define methods
    def increase_inventory(self, amount):
        self._inventory += amount

    def reduce_inventory(self, amount):
        self._inventory -= amount

    def get_label(self):
        return "Foxolate Shop: " + self._name

    def get_inventory_report(self):
        if self._inventory == 0:
            return "There are no bars!"
        return f"There are {self._inventory} bars."
    
```

具体操作：

```python
pina_bar = Product("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])
#创建一个实例，Product类名称作constructor，其调用__init__函数，创建了实例
pina_bar.increase_inventory(2)
#调用一个方法，使用dot(.)来调用属性或方法
```



### 3、Instance variables 实例变量

**Instance variables** are data attributes that describe the state of an object.

The object's methods can then change the values of those variables or assign new variables.

```python

class Product:
    def __init__(self, name, price, nutrition_info):
        self._name = name
        self._price = price
        self._nutrition_info = nutrition_info
        self._inventory = 0  
#This __init__ initializes 4 instance variables
```

### 4、Method invocation调用方法



```python
class Product:
    def increase_inventory(self, amount):
        self._inventory += amount
     
```

`pina_bar.increase_inventory(2)`

`pina_bar`是`increase_inventory`的第一个参数`self`（即实例本身）

也可以写成：`Product.increase_inventory(pina_bar, 2)`

### 5、object  attributes

1、An object can create a new instance variable whenever it'd like.（Python）

例如：

```python
class Product:

    def reduce_inventory(self, amount):
        if (self._inventory - amount) <= 0:
            self._needs_restocking = True
        self._inventory -= amount

pina_bar = Product("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])
pina_bar.reduce_inventory(1)
#_inventory _needs_restocking这两个是新的instance variables
```

2、若希望构建对所有实例都相同的variables，那就是class varibales类变量了

```python
class Product:
    _sales_tax = 0.07

    def get_total_price(self, quantity):
        return (self._price * (1 + self._sales_tax)) * quantity
    #_sales_tax即为类变量
```

3、Attributes are all public（Python）

所有属性均可以直接修改

### 6、inheritance继承

![](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220217163756674.png)

```python
class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += self.interact_increment
        print(f"Yay happy fun time with {animal2.name}")
#class Animal is the base class
class Rabbit(Animal):
    species_name = "European rabbit"
    scientific_name = "Oryctolagus cuniculus"
    calories_needed = 200
    play_multiplier = 8
    interact_increment = 4
    num_in_litter = 12

class Elephant(Animal):
    species_name = "African Savanna Elephant"
    scientific_name = "Loxodonta africana"
    calories_needed = 8000
    play_multiplier = 4
    interact_increment = 2
    num_tusks = 2
    def __init__(self, name, age=0):
        super().__init__(name, age)
        if age < 1:
            self.calories_needed = 1000
        elif age < 5:
            self.calories_needed = 3000
           #overridding __init__
 #Rabbit and Elephant are the superclasses of Animal   
class Panda(Animal):
    species_name = "Giant Panda"
    scientific_name = "Ailuropoda melanoleuca"
    calories_needed = 6000

    def interact_with(self, other):
        print(f"I'm a Panda, I'm solitary, go away {other.name}!")
    #If a subclass overrides a method, Python will use that definition instead of the superclass definition. the function interact_with is the case.(Overriding methods重载)
class Lion(Animal):
    species_name = "Lion"
    scientific_name = "Panthera"
    calories_needed = 3000

    def eat(self, food):
        if food.type == "meat":
            super().eat(food) #Animal.eat(self, food)
   #To refer to a superclass method, we can use super()
    
```

### 7、composition组合

An object can contain references to objects of other classes.

不同类的对象进行联动，称作组合composition

例子一，上面动物开party

```python
def partytime(animals):
    """Assuming ANIMALS is a list of Animals, cause each
    to interact with all the others exactly once."""
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            animals[i].interact_with(animals[j])
```

```python
jane_doe = Rabbit("Jane Doe", 2)
scar = Lion("Scar", 12)
elly = Elephant("Elly", 5)
pandy = Panda("PandeyBear", 4)
partytime([jane_doe, scar, elly, pandy])
```

例子二，下面的人养宠物：

```python
class Lamb:
    species_name = "Lamb"
    scientific_name = "Ovis aries"

    def __init__(self, name):
        self.name = name

class Human:
    species_name = "Human"
    scientific_name = "Homo sapiens"

    def __init__(self, name):
        self.name = name
        self.pets = []

    def adopt(self, pet):
        self.pets.append(pet)
        print(f"I have a pet named {pet.name}")

lamb = Lamb("little")
mary = Human("Mary")
mary.adopt(lamb)
```

project ants里面，place.bees,或者containerant中包含了ant，也是composition

## 补充1 

for循环中边修改边遍历的情况

```python
'''Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:'''
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

不搞清楚题目意思，再怎么做也是白做。别做了。

现在是做出来了

## 9、对象方法   Special Object Methods

### 1、dir

ask `dir()`, a built-in function that returns a list of all the attributes（methods and variables） on an object.

### ![image-20220220132911418](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220220132911418.png)

object中的典型方法：

1、__str__

![image-20220220132938174](C:\Users\Peter\AppData\Roaming\Typora\typora-user-images\image-20220220132938174.png)

实际上，`__str__`被应用在很多地方，我们看不见

```python
from fractions import Fraction

one_third = 1/3
one_half = Fraction(1, 2)

print(one_third)             # '0.3333333333333333'
print(one_half)              # '1/2'

str(one_third)               # '0.3333333333333333'
str(one_half)                # '1/2'

f"{one_half} > {one_third}"  # '1/2 > 0.3333333333333333'
```

我们甚至可以重载`__str__`,得到不一样的返回：

```python
class Lamb:
    species_name = "Lamb"
    scientific_name = "Ovis aries"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "🐑 : " + self.name#看看有没有这句话的区别
    
    def __repr__(self):
        return f"Lamb({repr(self.name)})"#看看有没有这句话的区别
    
lil = Lamb("Lil lamb")
lil
str(lil)
repr(lil) #返回内容为其值本身的字符串
print(lil) 
```

2、__repr__

The `__repr__` method returns a string that would evaluate to an object with the same values.

```python
from fractions import Fraction

one_half = Fraction(1, 2)
Fraction.__repr__(one_half)           # 'Fraction(1, 2)' 
#repr(one_half)
```





## 10、Recursive objects

### 1、join用法

```python
>>>print('\n'.join(['Hi','How','are','you']))
Hi
How
are
you
>>>print(','.join(['Hi','How','are','you']))
Hi,How,are,you
>>>','.join(['Hi','How','are','you'])
'Hi,How,are,you'
```

### 2、format表达式用法

在字符串前面加一个f即可

```python
>>>a = 100
sum0 = 0
for i in range(1,a+1):
    sum0 += i
print(f"sum = {sum0}")
#输出 sum = 5050
```

格式化：用`{content:format}`的形式输入输出即可

`f"sum = {sum0:o}"`就输出二进制格式

`f"sum = {sum0:.2f}"`保留两位小数

## 11、复杂度问题

np问题
