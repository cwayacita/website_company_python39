from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from colorama import Fore
from django.contrib import messages
import os
from datetime import datetime , timedelta
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from subprocess import Popen, PIPE
import time
import sqlite3
from django.contrib.auth.decorators import login_required
from mysite.decorators import user_is_webscraping

def check_for_done_web(p):
    if p.poll() is not None:
        return True
    return False, False


def runn_web(file):
    message = 'error'
    def exec_(list):
        proc = Popen(list, shell=True, stdin=None, stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc.communicate()
        print(stdout, stderr )


    with ThreadPoolExecutor(max_workers=1) as executor:
        # to demonstrate it will take a batch of 4 jobs at the same time
        cmds= [[ r"C:\Users\cjulemont\PycharmProjects\Channel_dynamic\venv\Scripts\python.exe",  r"C:\Users\cjulemont\PycharmProjects\Channel_dynamic\main.py", file], [ r"C:\Users\cjulemont\PycharmProjects\Channel_dynamic\venv\Scripts\python.exe",  r"C:\Users\cjulemont\PycharmProjects\Channel_dynamic\Main_model.py", file]]
        start = time.time()
        conn = sqlite3.connect(r'/home/cwayacita/Documents/Pycharmprojects/website_company_python39/mysite/db.sqlite3')

        file = 'test'
        sql_query = """INSERT INTO tasks (id, name, status_id, begin_date, end_date )
        VALUES ('1', '""" + str(file) + """','pending','""" + str(start) + """' , '""" + str(start) + """' );"""
        try:
            cur = conn.cursor()
            cur.execute(sql_query)
            conn.commit()
        except:
            message = 'error'
            return message
        futures = executor.map(exec_, cmds)
        for future in futures:
            # print(check_for_done(future))
            pass

        end = time.time()
        conn = sqlite3.connect(r'/home/cwayacita/Documents/Pycharmprojects/website_company_python39/mysite/db.sqlite3')
        cur = conn.cursor()
        cur.execute('delete from tasks;')
        conn.commit()
        message = 'success'
        print(f'Took {end - start} seconds')



    return message



@login_required
@user_is_webscraping
def simple_upload_web(request):
    status_url = ''

    if request.method == 'GET' and request.path == '/Webscraping/excel/':
        conn = sqlite3.connect(r'/home/cwayacita/Documents/Pycharmprojects/website_company_python39/mysite/db.sqlite3')
        df = pd.read_sql_query("SELECT * from tasks;", conn)
        print(df)
        if df.empty:
            # messages.warning(request, 'No file are actually in treatment')
            return render(request, 'Webscraping/simple_upload6.html', {'status_url': status_url})
        else:
            messages.warning(request, 'The file is being treated, please wait')
            return render(request, 'form/simple_upload3.html')




    elif request.method == 'POST' and request.FILES['myfile']:

        time_2 = datetime.now()
        print(Fore.YELLOW + f"{time_2} - ---> Setting up SqlLite connection")

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        if uploaded_file_url:
            input_folder = r'/Documents/Pycharmprojects/website_company_python39/mysite/media'
            files = [input_folder + "/" + x for x in os.listdir(input_folder)]
            newest = max(files, key=os.path.getctime)
            print(Fore.YELLOW + f"{uploaded_file_url} - ---> Loading the file for the process")

            message = ''
            try:
                df = pd.read_excel(newest, sheet_name='Hoja1')
            except:
                messages.warning(request,  'Please modify the name of the sheet : "Hoja1"')
                message = 'error'
            try:
                df = df[['Fecha' , 'CL' , 'Local Brand' , 'mensaje_literal_del_panelista' , '1_categoria' , '2_categoria' , '3_categoria']] #'1_categoria' , '2_categoria' , '3_categoria'
            except:
                messages.warning(request,  'Please modify the columns headers :' "'Fecha' , 'CL' , 'Local Brand' , 'mensaje_literal_del_panelista' , '1_categoria' , '2_categoria' , '3_categoria'" )
                message = 'error'

            if message in ('error', 'warning'):
                messages.warning(request,  'The format of your file is wrong, please retry')
            else :
                messages.success(request,  'The file is being treated, please wait')
                message = runn_web(newest)


            if message == 'success':
                messages.success(request,  'your file has been processed succesfully')

            return render(request, 'Webscraping/simple_upload6.html', )


