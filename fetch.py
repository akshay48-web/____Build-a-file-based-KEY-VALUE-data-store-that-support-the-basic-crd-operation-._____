 import program as pro

pro.create("maitri",56)

pro.create("src",10,9098) 

pro.read("oliver")

pro.read("team")

pro.create("maitri",40)
 
pro.delete("maitri")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.sleep()
