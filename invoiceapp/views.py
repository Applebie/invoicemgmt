from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection, transaction

#cursor = connection.cursor()
# Create your views here.

def show_client_details(request):
    #x=calculate()
    #return HttpResponse('Client Details')
        # Data retrieval operation - no commit required
        
    #return render(request,'client.html',{'name':'John'})
    
    #cursor.execute("SELECT foo FROM invoice WHERE id = %s", 1)
    #row = cursor.fetchall()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM invoice")
        query = cursor.fetchall()
        return render(request, 'client.html',{'query': query})
    finally:
        cursor.close()
    
    #return row

# def my_custom_sql():

#     # Data modifying operation - commit required
#     cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
#     transaction.commit_unless_managed()

