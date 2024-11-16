class Book:
    def __init__(self,title,author,year) -> None:
        self.title=title
        self.author=author
        self.year=year
    def search_info(self,val,name):
        for nam in name:
            if val==nam.title:
                print(f'{nam.title}\n{nam.author}\n{nam.year}')
    def display_all(self):
            print(self.title)
    def search_range(self):
            if self.year>=2000:
                print(f'{self.title}\n{self.author}\n{self.year}')
class fiction(Book):
    def __init__(self,title,author,year,gener):
        super().__init__(title,author,year)
        self.gener=gener
    def display_all(self):
            print(f'{self.title}-{self.gener}')
class Nonfiction(Book):
    def __init__(self,title,author,year,topic):
        super().__init__(title,author,year)
        self.topic=topic
    def display_all(self):
            print(f'{self.title}-{self.topic}')               


print('please add the book')
num=int(input('how  many book do you want to add ?'))
Books=[]
for i in range(num):
    c=int(input('what type of book do you want to add fiction(F) or Nonfiction(Nf) ?'))
    if c==1:
        tit=input('enetr the title: ')
        aut=input('enter the auther: ')
        yr=int(input('enter the year: '))
        gn=input('enter the gener of the Book: ')
        Books.append(fiction(tit,aut,yr,gn))
    else:
        tit=input('enetr the title: ')
        aut=input('enter the auther: ')
        yr=int(input('enter the year: '))
        to=input('enter the topic of the Book: ')
        Books.append(Nonfiction(tit,aut,yr,to))


    
for bs in Books:

    if isinstance(bs,Nonfiction):
        bs.display_all()


# c=input('what type of book do you want fiction(F) or Nonfiction(Nf) ?')
# if c=='F':


