#import argparse
import filecmp
import subprocess
import winapps
import difflib as df


#запись списка установленных программ 
def w_f(name): 
    f = open(name,'w')
    try:
        for apps in winapps.list_installed():
            f.write(apps.name)
            f.write('\n')
    except:
        print()
    f.close()
#чтение файла, вывод текста
def r_f(name):
    file = open(name)
    text = file.readlines()
    print(name)
    file.close()
    return text
#меню    
def gui():
    print('- MENU -')
    print('1 - list of installed programs') #список установленных программ
    print('2 - to compare the list of installed programs') #сравнить списки установленных программ
    print()
    print('0 - Exit')
    print()
    print('Enter the command number:')
    return int(input())
#оформление записи списка программ
def command_1():
    print('Enter file name:')
    name = input()
    w_f(name)
    print('--- DONE!\n')
#оформление сравнения файлов со списками программ
def command_2():
    print('Enter the name of the first file:')
    f1 = input()
    print('Enter the name of the second file:')
    f2 = input()
    a = filecmp.cmp(f1, f2, shallow=False)

    if a == False:
        dif(f1,f2)
    else:
        print('--- No changes!')
    print('--- DONE!\n')
#сравнивание и вывод различий в списках
def dif(f1,f2):
    txt1_list = r_f(f1)
    txt2_list = r_f(f2)


    d = df.Differ()
    diff = df.unified_diff(txt1_list, txt2_list, lineterm='')
    print('\n'.join(diff))

   
a = gui()
while a != 0:
    if a == 1:
        command_1()
        print('\n---')
        a = gui()
    else: 
        if a == 2:
            try:
                command_2()
            except:
                   print('\n--- error :(') 
            print('---')
            a = gui()
        else: 
            print('\n--- Wrong answer. Repeat, please')
            print('---')
            a = gui()
