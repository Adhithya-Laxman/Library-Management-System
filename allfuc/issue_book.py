'''BOOK ISSSUE FUNCTION'''
def book_issue():
    f=open('books2.csv','r+')
    list_of_books=[]
    book_search=input('''Search For Book by:
                      1. Name
                      2. Author
                      Select operation(1 or 2): ''')
    if book_search=='1':
        x=input('Enter the Name of the Book Needed: ')
        x=x.lower()
        flag=0
        for record in f:
            field=record.split(',')
            y=field[1]
            y=y.lower()
            if(x in y):
                flag=1
                list_of_books.append(record)
        f.seek(0)
        if(flag==0):
            print('Sorry Your Book is Not available! :(')
        if (flag==1):
            for val in list_of_books:
                print(val)
    elif book_search=='2':
        x=input('Enter the Name of the Author Needed: ')
        x=x.lower()
        flag=0
        for record in f:
            field=record.split(',')
            y=field[2]
            y=y.lower()
            if(x in y):
                flag=1
                list_of_books.append(record)
        f.seek(0)
        if(flag==0):
            print('Sorry Your Author\'s Book is Not available! :(')
        if (flag==1):
            for val in list_of_books:
                print(val)
    else:
        print('You gave a wrong entry!')
        book_issue()
    f1=open('Final.csv','w')
    global book_id_select
    book_id_select=input('Enter the book ID of the book needed from the above books.')
    for book in f:
        field=book.split(',')
        #print(book[0])
        if field[0]==book_id_select and field[10]=='Unavailable\n':
            print('Sorry, This book is currently Unavailable!')
            f1.close()
            f.close()
            return

        if field[0]==book_id_select:
            print(book)
            field[10]='Unavailable\n'
            #print(field[10])
        x=','.join(field)
        f1.write(f'{x}')
    f1.close()
    print('''Your Book is Available!Congrats You are Issued with the book.
          
          
          Note: You are requested to return the book within 30 days with this being day 0.
          The fine for delay is Rs. 1/- for each day.''')
    f1=open('Final.csv','r')
    over_writing_original=f1.readlines()
    #print(over_writing_original)
    f1.close()
    f.close()
    f=open('books2.csv','w')
    x=''.join(over_writing_original)
    f.write(f'{x}')
    #f.write(x)       
    f.close()
    #f.write()     
    return book_id_select
#print(book_issue())