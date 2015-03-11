# Name: learn_python.py
# Date: 03/11/2015
# Author: Muralidhar Ramarao
# email: muralidharhsn@gmail.com
# Description: This script would download the pages from the Learn to Python the Hard Way
#              and create offline pages for access. It would basically download the contents
#              and create and offline version. the start_here.py is the first page with all
#              index and the index would work locally as well.
# Note: This is a very basic script. I'm on my path to master the programming language.
# creating these tiny scripts that will keep me going. Please feel free to send me feedback
# on my email address.

import requests, re, os

def main(path):
    print path
    url='http://learnpythonthehardway.org/book/'
    pages=[]
    read_pages(url,'start_here.html',path)
    for links in re.findall(r'href="(\w+[\d]*[.]\w+)"',get_response(url).text):
        if not os.path.isfile(path+'/'+links):
            read_pages(url+links,links,path)
            print 'checking if it is appendix:',links=='appendixa.html'
            if links=='appendixa.html':
                for link in re.findall(r'href="(\w+[-]\w+[-]\w+[/]\w+[.]\w+)',get_response(url+links).text):
                    path_list=link.split('/')[:-1]
                    check_directoy(path,path_list)
                    read_pages(url+link,link,path)
        else:
            print 'Skipping %s as the file already exists.'% links


def get_response(url):
    response=requests.get(url)
    return response

def check_directoy(path,path_list):
    for paths in path_list:
        if not os.path.exists(path+'/'+paths):
            os.mkdir(path+'/'+paths)

def read_pages(url,filename,path):
    response=requests.get(url)
    flag=False
    output=path+'/' +filename
    print "Created: ",output
    with open(output,'a') as fp:
        for line in response.text.split('\n'):
            if 'RST ENDS' in line:
                    flag=False
            if flag:
                    fp.write(line)
            if 'RST STARTS' in line:
                    flag=True

if __name__=='__main__':
    try:
        print '''Please enter the path where this script will download the book into.
The script would download each page from the website learnpythonthehardway.org
and store it as an html file. The links would work locally for most of the
contents.
If you are not sure yet, then please create a new folder and pass the complete
path in the below prompt'''
        input_path=raw_input("Enter the output path:")
        if os.path.exists(input_path.strip()):
            main(input_path)
        else:
            print "ERROR!!! Please enter a valid path."
            pass
    except KeyboardInterrupt:
            pass
