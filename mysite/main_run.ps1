

$path = 'C:\Users\cjulemont\PycharmProjects\Django_apache_channel\mysite'
$file = 'TestFile.py'
$path2 = & "C:\Program Files\Python39\python.exe"

$python_file = $path+"\\"+$file

$cmd = $path2+" "+$python_file  # This line of code will create the concatenate the path and file
Start-Process $cmd  # This line will execute the cmd
cmd.exe "import os"
cmd.exe "print('hello')"
cmd.exe name = input("Enter your name: ")



