'''----LIBRARY MANAGEMENT SYSTEM----'''
from allfunc import issue_book
from allfunc import return_book
#while(True):
def user():
    print('Login Page:')
    operation=input('''Enter the operation:
                     1. Login
                     2. Sign up
                     Your Operation: ''')
    profile=[]
    if operation=='1':
        username=input('Enter User Name: ')
        password=input('Enter password! ')
        member_file=open('member.csv','r+')
        data=member_file.readlines()
        member_file.seek(0)
        #print(data)
        for record in data:
            fields=record.split(',')
            #print(fields)
            if(fields[0]==username and fields[1]==password):
                global flag
                flag=f'Welcome {username}!'
                print(flag)
                #print('Your Profile is: \n',record)
                #global profile
                profile=record.split(',')
                print('Your Profile is: \n',profile)
                return profile
            
            else:
               # global flag
                flag='You are not a member! Try Signing up!'
        print(flag)
        
        #print(flag)
        if profile==[]:
            user()
        #data=member_file.readlines()
    
    elif operation=='2':
          flag='You are new to the Application! Welcome!'
          username=input('Create User Name: ')
          password=input('Create password! ')
          member_file=open('member.csv','a+')
          #member_file.write(f'\n{username},{password}')
          print(flag) 
          new_profile={'Username':username,'Password':password,'No_of_Books_accessed':'0','Book1':'NA','Book2':'NA','Fine':'0'}     #Username,Password,No_of_Books_accessed,Book1,Book2,Fine
          #print(new_profile)
          val=list(new_profile.values())
          #print(val)
          str1=','.join(val)
          member_file.write(f'{str1}\n')
          #global profile
          profile=val
          print('Your Profile is: \n',profile)
          return profile
    else:
        user()
    
    #return profile
profile=user()
print(profile)
print('Username: ',profile[0])
print('Number Of Books accessed: ',profile[2])
print('Book1: ',profile[3])
print('Book2: ',profile[4])
print('Pending Fine Amounnt: ',profile[5],'Rupees')
books_accessed=int(profile[2])
written_string=''

while(True):
    function=input('''Enter the operation to be performed!
                   1. Book Issue
                   2. Book Return
                   3. Pay Fine
                   Select Operation(1/2/3): ''')
    if function=='1':
        if books_accessed<2:
            #Book_id=issue_book.book_issue()
            #profile[3]+=1
            if profile[2]=='0':
                profile[3]=issue_book.book_issue()
            elif profile[2]=='1':
                profile[4]=issue_book.book_issue()
            val=int(profile[2])
            profile[2]=str(val+1)
            
        else:
            print('You are allowed to access only 2 books at the same time.\nReturn a book to take another.')
            
    elif function=='2':
        if books_accessed>0:
            #Book_id=return_book.book_return()
            #profile[3]+=1
            if profile[2]=='1':
                profile[3]=return_book.book_return()
            elif profile[2]=='2':
                Book_id=return_book.book_return()
                if(profile[3]==str(Book_id)):
                    profile[3]=''
                elif(profile[4]==str(Book_id)):
                    profile[4]=''
                    
                    
            val=int(profile[2])
            profile[2]=str(val-1)
            
        else:
            print('You have not borrowed any book.')
            break
        #return_book.book_return()
        day_of_return=int(input('Enter the day you are returning the book after issue.'))
        if day_of_return>30:
            print(f'You have submitted the book {day_of_return-30} days after the due date.')
            print(f'Hence Your Fine amount will be increased by {day_of_return-30} Rupees.')
            profile[5]=str(day_of_return-30)
    elif function=='3':
        print('Your Fine Amount is:', profile[5])
        fine=int(input('Enter money you are going to pay:'))
        if(fine<=int(profile[5])):
            profile[5]=str(int(profile[5])-fine)
            print('Your Remaining fine amount is: ',profile[5],'Rupees')
        else:
            print('Your amount is greater than the pending fine amount of ',profile[5],'Rupees')
    f=open('member.csv','r')
    f.seek(0)
    x=f.readlines()
    final=[]
    f.close()
    #f=open('temp_member.csv','w')
    for record in x:
        fields=record.split(',')
        if(fields[0]==profile[0] and fields[1]==profile[1]):
            fields=profile
            
            #break
        final.append(fields)
    #print(final)
    f=open('member.csv','w')
    for record in final:
        #print(record)
        #written_string=''
        written_string=','.join(record)
        #print(f'{written_string}\n')
        f.write(f'{written_string}\n')
    f.close()
    print(profile)
    choice=input('Do you Want to continue operation? (Y,N)')
    if(choice not in ['y','Y','Yes','YES','yes']):
        break    
