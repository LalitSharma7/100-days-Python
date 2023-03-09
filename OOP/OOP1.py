# Init is constructor and it runs everytime object call this class
# self is the current object on which we are working

L = [1,2,3]

L.upper()

s = 'hello'
s.append('x')

L = [1,2,3]
print(type(L))

s = [1,2,3]

# syntax to create an object

#objectname = classname()

# object literal
L = [1,2,3]

L = list()
L

s = str()
s

# Pascal Case

HelloWorld

class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.balance = 0
    #self.menu()

  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.balance = user_balance

    print('pin created successfully')
    self.menu()

  def change_pin():
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
      self.menu()
    else:
      print('nai karne de sakta re baba')
      self.menu()

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.balance)
    else:
      print('chal nikal yahan se')

  def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print('withdrawl successful.balance is',self.balance)
      else:
        print('abe garib')
    else:
      print('sale chor')
    self.menu()

obj1 = Atm()

id(obj1)

obj2 = Atm()

id(obj2)

L = [1,2,3]
len(L) # function ->bcos it is outside the list class
L.append()# method -> bcos it is inside the list class

class Temp:

  def __init__(self):
    print('hello')

obj = Temp()

3/4*1/2

class Fraction:

  # parameterized constructor
  def __init__(self,x,y):
    self.num = x
    self.den = y

  def __str__(self):
    return '{}/{}'.format(self.num,self.den)

  def __add__(self,other):
    new_num = self.num*other.den + other.num*self.den
    new_den = self.den*other.den

    return '{}/{}'.format(new_num,new_den)

  def __sub__(self,other):
    new_num = self.num*other.den - other.num*self.den
    new_den = self.den*other.den

    return '{}/{}'.format(new_num,new_den)

  def __mul__(self,other):
    new_num = self.num*other.num
    new_den = self.den*other.den

    return '{}/{}'.format(new_num,new_den)

  def __truediv__(self,other):
    new_num = self.num*other.den
    new_den = self.den*other.num

    return '{}/{}'.format(new_num,new_den)

  def convert_to_decimal(self):
    return self.num/self.den

fr1 = Fraction(3,4)
fr2 = Fraction(1,2)

fr1.convert_to_decimal()
# 3/4

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)

s1={1,2,3}
s2={3,4,5}

s1 + s2

print(fr1 - fr2)
