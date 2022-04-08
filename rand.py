import random
print ("random number from range(100) : ", random.choice(range(100)) )  
list = [1,2,3,5,9]
print ("random element from list : " , random.choice(list))
str = "Hello world"
print ("random character from string : " , random.choice(str))
print ("randrange(1,100,2): ", random.randrange(1,100,2))
print ("randrange(100): ", random.randrange(100))
print ("random(): " , random.random())
random.seed()

print ("random with default seed",random.random())
random.seed(10)
print ("random with int seed", random.random())
random.seed("hello",2)
print ("random number with string seed", random.random())
list =  [20,16,10,5]
random.shuffle(list)
print ("reshufled list",list)
print ("random float unfiform(5,10)",random.uniform(5,10))
