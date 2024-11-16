# from abc import ABC,abstractmethod
# class Elements(ABC):
#     def __init__(self,title,author,year):
#         self.title=title
#         self.author=author
#         self.year=year
#     @abstractmethod
#     def display(self,name):
#         if name==self.title:
#             print(f'title of Book: {self.title}\nauthor of Book: {self.author}\n publied in: {self.year}')
#         else:
#             print('sorry,don\'t exist')    
# class book(Elements):
#     def __init__(self, publisher, num_page,title,author,year):
#         super().__init__(title, author, year)
#         self.publisher=publisher
#         self.num_page=int(num_page)
#     def display(self,name):
#         super().display(name)
#         if name==self.title:
#            print(f'published by: {self.publisher}\nnumber of page: {self.num_page}\n')
# class Magazin(Elements):
#     def __init__(self, issue_number, month,title,author,year):
#         super().__init__(title, author, year)
#         self.issue_number=issue_number
#         self.month=int(month)
#     def display(self,name):
#         super().display(name)
#         if name==self.title:
#             print(f'published by: {self.issue_number}\nnumber of page: {self.month}\n')

# # this is polymorphithm property , it maynot nesessaty related to abstract class
# def display(element):
#     for elem in element:
#         elem.display('Ethiopia')

# bk=book('dk company',300,'Ethiopia','Dr.Anderson Mattew','2007')
# mg=Magazin('34',3,'Ethiopia','libneh hulu','2024')

# display([bk,mg])
#  # class type(str): ->this means type inherite property of string 


