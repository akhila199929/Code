#import module
import data_store as operations

#key-value
x.create("todo",12)

#key-value with time-tto-live property
x.create("list",13,3600) 

#to return key name
x.read("todo")

#to return value
x.read("list")

#to return error as name already exists
x.create("todo",14)

#modify value
x.modify("todo",15)

#delete key value 
x.delete("todo")

#multi threading
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
