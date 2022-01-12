print(hex(345))#hexadecimal
pow(2,4,3)    #(2**4) % 3
abs(-45)    #45
round(3.1)    #3.0
print(round(3.476879, 4))    #3.4769

s='hello world'
s.capitalize()
s.upper()
s.lower()
s.count('o')
s.find('o')
'hello\thi'.expandtabs() #'hello	hi'
s.isalnum()    #is alphanumeric
s.isalpha()    #is alphabetic
s.islower()
s.isspace()       #all char are whitespace
s.istitle()       
s.isupper()
s.endswith('o')
s.split('e')      #['h', 'llo']
s.partition('e')  # ['h', 'e', 'llo']        will give firt split head, seperator and rest

s = set()
s.add(1)
s.add(2)
s.add(2)
sc = s.copy()
sc.add(3)
sc.difference(s)     #{1, 2}
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.difference_update(s2)       #A = A-B
s1.discard(3)
s2.discard(12)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.intersection(s2)    #{3}
s1.intersection_update()       #A = A intersection B
s.clear()   #makes it empty
s1 = {1,2}
s2 = {1,2,4}
s3={5}
s1.isdisjoint(s2)        #false        they have common
s1.disjoint(s3)            #true
s1.issubset(s2)          #true
s2.issuperset(s1)
s1.symmetric_difference(s2)   #{4} elements that are only in one   can be _update
s1.union(s2)           
s1.update(s2)            #union update


d = {'k1':1, 'k2':2, 'k3':3}
z
