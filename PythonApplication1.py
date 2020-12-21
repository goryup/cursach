#import argparse
import filecmp
import subprocess
import winapps
import difflib as df

def w_f(name):
    f = open(name,'w')
    try:
        for apps in winapps.list_installed():
            f.write(apps.name)
    except:
        print()
    f.close()

def r_f(name):
    file = open(name)
    text = file.readlines()
    print(name)
    file.close()
    return text
    
def gui():
    print('MENU')
    print('1 - list of installed programs') #список установленных программ
    print('2 - to compare the list of installed programs') #сравнить списки установленных программ
    print()
    print('0 - Exit')
    print()
    print('Enter the command number:')
    return int(input())

def command_1():
    print('Enter file name:')
    name = input()
    w_f(name)

def command_2():
    print('Enter the name of the first file:')
    f1 = input()
    print('Enter the name of the second file:')
    f2 = input()
    a = filecmp.cmp(f1, f2, shallow=False)

    if a == False:
        dif(f1,f2)
    else:
        print('No changes!')

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
        print('---')
        a = gui()
    else: 
        if a == 2:
            command_2()
            print('---')
            a = gui()
        else: 
            print('Wrong answer. Repeat, please')
            print('---')
            a = gui()

