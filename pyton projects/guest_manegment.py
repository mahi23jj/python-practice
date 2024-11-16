class Guest:
    # class attribute - for all object created
    types='name'
    # instnace attribute - specfic for each object
    def __init__(self,fname,lname,rank,age) -> None:
        self.fname=fname
        self.lname=lname
        self.rank=int(rank)
        self.age=int(age)
    
    # to creat a class method - accesable for all object created
    @classmethod
    def zero(cls):
        return cls('ma','so',15,24)   
# class method provides a simple way to create a Guest object with default
# values, which can be useful in various scenarios, 
    def guest_info(self,alls):
        for all in alls:
            print(f'{all.lname},{all.fname},{all.age}')
    def loyality(self,alls) :
        Gold=[]
        for all in alls:
            if all.rank>=10:
                Gold.append(all.lname)     
        print('Gold memembers are:')
        for gold in Gold:
            print(gold)

guest=Guest('mahlet','sol',10,20)
gu=Guest('mahi','solomon',5,24)
a=guest.zero()
b=gu.zero()
print(f'{a.lname},{b.lname}') # so,so b/c class method is common for any obeject

# guest.t=10 # py is dynamic so we don't have to create every attribut in constructor 
# print(guest.t) # applicable 
# guest.types='you'# we can change the value of attribute as we want 

# val=[Guest('mahlet','sol',10,20),Guest('mahi','solomon',5,24)] 
# print(guest.guest_info(val))          
# print(guest.loyality(val))       


     


        