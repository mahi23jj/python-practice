
# with open('name.txt','w') as t:


class todo:
    def __init__(self) -> None:
        self.lists=[]
        self.f=open('storage.txt', 'w')
    def add(self,data):
        self.lists.append(data)
        self.f.write(data)   
    def remove(self,inx):
        for i in range(len(self.lists)):
            if i==inx:
                self.lists.remove(self.lists[i])
    def complete(self,inx):
        for i in range(len(self.lists)):
            if i==inx:
                if self.lists[i].comp==True:
                    self.lists[i].comp=False
                else:
                    self.lists[i].comp=True
    def out(self):
        for lists in self.lists:
            print(f'title: {lists.title}')
            print(f'discription: {lists.disc}')
            print(f'completed: {lists.comp}')


class lists:
    def __init__(self,title,disc) -> None:
        self.title=title
        self.disc=disc
        self.comp=False
def add():
    try:    
        with open('file_name.txt','a')as f:
            f.write('you')
    except OSError as e:
        print(f"An error occurred while trying to write to the file: {e}")

#f'title: {data.title} ,discription: {data.disc}\n'
# x=1
# while x==1:
#     ti=input('enter the title')
#     dis=input('enter the discription')
#     add(lists(title=ti,disc=dis))
#     x=int(input('if you want continue enter 1 to terminet enter 2:'))

# val.complete(1)
# val.out()
add()



                            



                    
        





