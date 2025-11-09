# f=open('a3.txt','a')
# # print(f.name)
# # print(f.mode)
# # print(f.encoding)
# # print(f.writable())
# # print(f.readable())
# # print(f.closed)
# # data='''This" 
# #             "        " 
# #       "        is " 
# #       "      python " 
# #       "clas'''
# # data=['python\n','java\n']
# # f.writelines(data)
# # f.close()
# cl='python\n'
# cl1="This is python\n"
# cl2='''this is 
#              python
#                 class\n'''
# f.writelines([cl,cl1,cl2])
# f.close()
f=open('a1.txt','r')
# all_data=f.read(5)
# # for x in all_data(5):
#     # print(x)
# print(all_data)
# data=f.read()
# print(data)
# data=f.readline()
# print(data)
data=f.readlines()
print(data)