'''BOOK RETURN FUNCTION'''
def book_return():
    f=open('books2.csv','r+')
    list_of_books=[]
    book_search=input('''Search For Book by:
                      1. Name
                      2. Author
                      Select operation(1 or 2): ''')
    if book_search=='1':
        x=input('Enter the Name of the Book to be Returned: ')
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
            print('Sorry Your Book Does not belong to this library! :(')
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
            print('Sorry Your Author\'s Book Does not belong to this library! :(')
        if (flag==1):
            for val in list_of_books:
                print(val)
    else:
        print('You gave a wrong entry!')
        book_return()
    f1=open('Final.csv','w')
    book_id_select=input('Enter the book ID of the book needed from the above books.')
    for book in f:
        field=book.split(',')
        #print(book[0])
        if field[0]==book_id_select and field[10]=='Available\n':
            print('''This book is currently Available!
                  Your Book Does not belong to this library! :(''')
            f1.close()
            f.close()
            return

        if field[0]==book_id_select:
            print(book)
            field[10]='Available\n'
            #print(field[10])
        x=','.join(field)
        f1.write(f'{x}')
    f1.close()
    print('Your Book Return is Accepted! Thank you!')
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
    return 'NA'
#print(book_return())