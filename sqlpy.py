'''
python program for running sqlite3 queries
'''
import sqlite3
def selectsearch(query):
    '''
    Docstring:
    This function returns 0 if SELECT statement else -1
    '''
    result=query.find("SELECT")*query.find("Select")*query.find("select")
    return result
def select_sql(selectquery,dbname):
    '''
    Docstring:
    This function is used to run queries to SELECT features
    and displays the result. 
    '''
    conn=sqlite3.connect(dbname)
    cursor=conn.execute(selectquery)
    for row in cursor:
        print(row)


def script(sql_string,dbname):
    '''
    Docstring:
    This function runs SQL queries on a database called somedatabase.db
    script(querystring).
    '''
    check=selectsearch(sql_string)
    if check==0:
        select_sql(sql_string,dbname)
    elif check==-1:
        conn=sqlite3.connect(dbname)
        conn.execute(sql_string)
        conn.commit()
    else:
        print("error lol")
#remember to check dbname when connecting to database

def runsqlquery():
    '''
    Docstring:
    Enter query mode in sqlite3
    '''
    sql_query="something"
    print("1.create database (use this if running for the first time)")
    print("2.use existing database")
    choice=int(input('>'))
    if choice==1:
        print("Please enter the name of the database that you wish to create followed by .db")
        database_name1=input('>')
        while sql_query!="quit":
            print("Please enter your query ('quit' to quit query mode)")
            query=input('>')
            if query=="QUIT" or query=="quit":
             break

            script(query,database_name1)
        print("Exited query mode.")

    elif choice==2:
        print("Please enter the name of the database that you created .db")
        database_name=input('>')
        while sql_query!="quit":
            print("Please enter your query ('quit' to quit query mode)")
            query=input('>')
            if query=="quit" or query=="QUIT":
                break
            script(query,database_name)
            

        #exited query loop
        print("Exited query mode")
    else:
        print("Wrong choice.")
        runsqlquery()

        
        
#<module> begins
runsqlquery()





