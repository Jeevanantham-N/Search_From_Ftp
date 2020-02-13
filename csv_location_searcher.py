import os, sys
from ftplib import FTP, error_perm
import ftplib
import csv
csv_list = []
def walk_dir(f, dirpath):
    original_dir = f.pwd()
    try:
        f.cwd(dirpath)
    except error_perm:
        return

    names = f.nlst()
    x= 0
    for i in names:
        if ".csv" in i:
            csv_list.append(["ftp://192.168.4.100"+str(dirpath)+"/"+i])
            x = 1
    if x==0:
        for name in names:
            walk_dir(f, dirpath + '/' + name)
        print(original_dir)
        f.cwd(original_dir)

def main(csv_list):
    f = ftplib.FTP("192.168.4.100")
    f.login('grluser','grlindia123$')
    walk_dir(f, '/Public/C2 QA Data/Sprint1batch1/B - 1.4.7.45')
    #csv_location(csv_list)
    f.quit()

def csv_location(csv_list):
    filepath = '/home/jeevanantham/PycharmProjects/GRL_11_2_2020/csv_location.csv'
    with open(filepath, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
    for each in csv_list:
        with open(filepath, 'a', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows([[each[0]]])

    with open(filepath,'r',newline='',errors='replace') as print_:
        reader = csv.reader(print_)
        reader = list(reader)
        for i in reader:
            print(i)


if __name__ == '__main__':
    main(csv_list)
