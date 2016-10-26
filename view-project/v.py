# view 1
from flask import Flask, render_template,json,request
import os

import csv




app= Flask(__name__)



@app.route('/')
def index():
 qs = request.query_string
 print (request.args)
 return render_template('index.html', query_string=qs)


#view 2
@app.route('/v2')
def showpage():
    test = [1, 2, 3, 4, 5, 6]
    print (test)
    return render_template("start.html", list=test)

#Dictionary

@app.route('/dict')
def my_dict():
    dictionary = {'Name': 'Asia', 'Age': 20, 'Class': 'First'}

    print ("dictionary['Name']: ", dictionary['Name'])
    print ("dictionary['Age']: ", dictionary['Age'])


    return render_template('view2.html',dictionary=dictionary)

#Tuple
@app.route('/tup')
def my_tuple():
    my_t1 = (1, 'H', 2, 'I', 3, 'E', 4, 'v', 5, 'e', 6, 'r')

    print (my_t1[1])
    print (my_t1[3])
    print (my_t1[6])
    print (my_t1[5])
    print (my_t1[7])
    print (my_t1[11])
    return render_template('view3.html', tuples=my_t1)
#CSV

@app.route('/cs')
def my_csv():
 with open('ctest.csv') as csvfile:
  fieldnames = ['first_name', 'last_name']
 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 return render_template('view4.html', my_csv= writer)

#json url


# Define routes for the examples to actually run

import urllib.request
@app.route('/jay')
def jay():

    geturl = ('http://search.mtv.com/solr/mtvpress/select/?q=pk_id:108&wt=json&indent=true')

    response=urllib.request.urlopen(geturl)
    content = response.read()
    data = json.loads(content)
    print(data)


    return render_template('jay5.html', data=data)

if __name__ == '__main__':
     app.run(debug= True)
