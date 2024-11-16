# f=open('file_name.txt', 'r')
# # r - read only
# #rt
# #rb - binary file open 
# c=f.read() # jus to read
# print(c)
# print(f.closed) # to cheak wather it is closed or not 
# f.close() # to close
# print(f.closed)

# read in form of list
# with open('file_name.txt','a') as f:
#         f.write('hey you\n just')

    # con=f.read().splitlines()
    # print(con) # ['hey my name is mahlet', 'hey my name', 'mahlet']
#     cos=f.readline()
#     print(cos)# hey my name is mahlet -> it only one line 
#     col=f.readlines()
#     print(col) #_>['hey my name is mahlet\n', 'hey my name\n', 'mahlet\n']
#     cob=list(f) # ['hey my name is mahlet\n', 'hey my name\n', 'mahlet\n']
#     # ######################
#     # for line in f:
#     #     print(line)

# write to text files
# a - append text on the existing file 
# w- writen mode 
#r+ -append text on the existing file on the beggining of file 
# with open('name.txt','w') as t:
#     t.write('hey you\n just')
    #cos=t.read()
    #print(cos)
# try:
#     with open('name.txt', 'w') as f:
#         f.write('hey you\n just')
# except OSError as e:
#     print(f"An error occurred: {e}")
# z=[]
# with open('d.txt') as f:
#     con=f.read().splitlines()
#     for line in con:
#         line=line.strip()
#         ts=line.split(':')
#         z.append(ts)
# #print(z)

# for i in range(len(z)):
#     print(f"{z[i][0]}    |  {z[i][1]}  |  {z[i][2]}  |  {z[i][3]}  |  {z[i][4]}  ")

    
# def add_task_to_file(task, filename='todo_list.txt'):
#     try:
#         with open(filename, 'a') as file:
#             file.write(task + '\n')
#         print(f'Task "{task}" added to {filename}')
#     except Exception as e:
#         print(f'Error: {e}')

# # Example usage
# add_task_to_file('Buy groceries')
# add_task_to_file('Complete Flutter project')


try:
       print("Attempting to open file...")
       file = open('s.txt', 'w')
       print("File opened successfully.")
       file.write('Hello, World!')
       file.flush()  # Ensure all data is written
       print("Write operation successful.")
except OSError as e:
       print(f"An error occurred: {e}")
finally:
       if 's.txt' in locals():
           file.close()  # Ensure the file is closed
   




