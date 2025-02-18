# create the hashmap.
# use modulo function to get the index where the value must be stored.
# if conflicts then create the array and append the value there.

# hash = {
#     0:"varsha",5:"vamshi",8:"varun" ,9:"vinu",14:"gaja"
# }


# list_length=len(hash)

# list1=[[] for _ in range(list_length)]



# hash_keys=hash.keys()
# list_hash_keys = list(hash_keys)
# print(list_hash_keys)

# store_index=[]
# new_list=[]
# match=False
# new_list_value=[]



# for key in list_hash_keys:
#    index =  key%list_length
#    if store_index!=[]:
#       for i in store_index:
#          if index==i:
#             match=True
#       if match:
#          list1[index].append(hash[key])        
#       else:
#          list1[index]=[hash[key]]         
#    else:
#       list1[index] = [hash[key]]
      
#    store_index.append(index)
# print(list1)     


class HashMap:
   def __init__(self,size):
      print("constructor")
      self.size=size
      self.list1=[[] for _ in range(self.size)]
      self.store_index=[]

   def get(self,key):
      index =  key%self.size 
      if index in self.store_index:
        for pair in self.list1[index]:
          if pair[0]==key:
            return pair[1]
            
      print("key not found")
      return None
      
   def set(self,key,value):
    index =  key%self.size
    if index in self.store_index:
      self.list1[index].append([key,value])
    else:
      self.list1[index] = [[key,value]]
    self.store_index.append(index)
    
    # match=False
    # if self.store_index!=[]:
    #     for i in self.store_index:
    #         if index==i:
    #            match=True
    #     if match:
    #         self.list1[index].append(value)        
    #     else:
    #         self.list1[index]=[value]         
    # else:
    #         self.list1[index] = [value]
      
    # self.store_index.append(index)

    
    #   for item in self.list1[index]:
    #        if item[0]==key:
    #          return item[1]
    #   else:
    #     print("key not found")
    

          
      

map=HashMap(10)

map.set(0,"varsha")
map.set(10,"vamshi")
map.set(20,"varun")
map.set(9,"vinu")
map.set(35,"gaja")
print(map.list1)
print(map.get(36))