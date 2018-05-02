'''
Easy-Info: An easy way to grab python dictionary data.
Written in python 3.
Created by Dustin Halat(DHOcreator) May 1, 1018.
Desighned to create a dictionary "data base" that can 
easily be accesed. Great for grouping data about people
or object characteristics. (Grades, Courses, records, pros,
cons, ect.) This is just a temlate and a way to  access 
the dictionary. Download this and eddit the dictionary to your needs.
'''
#varibles that can be changed and put into the dictionary
#great for making dictionary code smaller
custom = '!#Need user info#! (coming soon)'
info = "Pretty easy to get around the different data groups! They're laid out easy for you project"
#The Main Dictionary itself
Dictionary = {'D1': ['This is Data group 1', 'pi equals 3.14', 3.14], 'SubDic':{'D2':['D2 is data group 2', 'Ti is held in a sperate dictionary'], 'userFile': custom }, 'D3':['D3 is data group 3', info] }
print(Dictionary)
#The program loop to access the data
while True:
    access = input('What data group do you wanna access?>')
    specific = input('What inside that data group do you wanna access?>')
    dataType = input('Is it a another sub-dictionary or a list? SubDic/list>')
    if(dataType == 'list'):
        print(Dictionary[access][int(specific)])
    elif(dataType == 'SubDic'):
        print(Dictionary[access][specific])
    else:
        print('!#ERROR#!')

