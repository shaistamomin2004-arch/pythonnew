#arithmetic operator : + - * / % ** //
a = 3
b = 5
sum = a+b
sub = a-b
div = a / b
mul = a * b
exp = a ** b #exponential
flr = a // b #floor division
mod = a % b # modulus
print(sum)
print(sub)
print(f"{a} / {b} = {div}")
print(f"{a} * {b} = {mul}")
print(f"{a} ** {b} = {exp}")
print(f"{a} // {b} = {flr}")
print(f"{a} % {b} = {mod}")

#assignment operator
# =  +=  -=  %=  **=  //=
x = 10
y = 15

x += y ##x = x + y this means
print(x)
x -= y #x = x - y this means
print(x)
x *= y #x = x * y this means
print(x)
x /= y #x = x / y this means
print(x)
x %= y #x = x % y this means
print(x)
x **= y #x = x ** y this means
print(x)
x //= y #x = x // y this means
print(x)


#comparison operator----------
#  >  >=  <  <=  ==  !=

v = 4
w = 6
ss = v <= w
print(ss)

c = 5
d = 6
print(f"{c}>{d} => {c > d}")
 
g = 5 
f = 7
print(g > f)
print(g < f)
print(g <= f)
print(g >= f)
print(g == f)

g1 = 4
h1 = 4
print(g1 == h1)
print(g1 <= h1)
print(g1 != h1)


#----------------comparison operator
q = 7 
t = 6
print(f"{q}>{t}> {q > t}")
print(q > t)
print(f"{q}<{t} < {q < t}")

print(f"{q}<={t} <= {q <= t}")
print(f"{q}>={t} >= {q >= t}")
print(f"{q}=={t} == {q == t}")
q1 = 5
q2 = 5
print(f"{q1}!={q2} != {q1 != q2}")
print(f"{q1}=={q2} is {q1 == q2}")


#logical opetrator    (and ,or , not)
no = 50
no2 = no > 10 and no < 70
print(f"This is :{no2}")

no2 = no > 30 or no < 20
print(f"This is :{no2}")

print(not(no2))
print(not(no < 30 or no > 60))
print(not(no > 30 and no < 100))

print("-------------- combining different operator---------")

print((5+2) - (5+2)) # use paranthesis () to give priority and for perfect result

print(50 + 100 * 3)

print(3 + 4 - 8 + 2)
print((3 + 4) - (8 + 2))











