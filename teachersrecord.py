import pandas as pd
import matplotlib.pyplot as plt

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('                   Welcome to Teacher Module         ')
print('-------------Select the correct choice to work on Teacher Module-------')
option = 1
dfTeacher=pd.read_csv('lol.csv',header=None,names=['TNO','Name','Subject','Experience'])

while (option != 6):
    print()
    print('1. Add a new Teacher')
    print('2. Update Teacher')
    print('3. Delete Teacher')
    print('4. View Teachers')
    print('5. View Chart')
    print('6. Exit Teacher Module')
    option = int(input('Enter Choice : '))

    #Code for addition
    if (option == 1):
        # Take details of the Teachers
        TeacherNo = int(input('Enter Teacher Number : '))
        name = input('Enter Name : ')
        Subject = input('Enter Subject : ')
        Experience = input('Enter Experience : ')
        
        # Code to add data to dataframe
        # and write the Updated dataframe to csv file
        totalTeacher = dfTeacher['TNO'].count()
        dfTeacher.loc[totalTeacher] = [TeacherNo,name,Subject,Experience]
        print('--------------OUTPUT-----------------')
        print('Teacher Added....')
        dfTeacher.to_csv('lol.csv',header=False,index=False)
        print(dfTeacher)
        print('-------------------------------------')
    # Code for updation    
    elif (option == 2):
        # Search Record with Teacher number
        TeacherNo = int(input('Enter Teacher Number : '))
        indexno = dfTeacher.loc[dfTeacher['TNO'] == TeacherNo].index
        print(dfTeacher.loc[dfTeacher['TNO'] == TeacherNo])
        print('What would you like to change?')
        print('1. To Change Teacher Number')
        print('2. To Change Name')
        print('3. To Change Subject')
        print('4. To Change Experience')
        print('5. Back to main menu')
        changeoption = int(input('What would you like to change? : '))

        # Code to change the Data as per input choice
        if (changeoption == 1):
            TeacherNoNew = int(input('Enter New Teacher Number : '))
            dfTeacher.loc[indexno,'TNO'] = TeacherNoNew
            dfTeacher.to_csv('lol.csv',header=False,index=False)
        elif (changeoption == 2):
            nameNew = input('Enter New Name : ')
            dfTeacher.loc[indexno,'Name'] = nameNew
            dfTeacher.to_csv('lol.csv',header=False,index=False)
        elif (changeoption == 3):
            SubjectNew = input('Enter New Subject : ')
            dfTeacher.loc[indexno,'Subject'] = SubjectNew
            dfTeacher.to_csv('lol.csv',header=False,index=False)
        elif (changeoption == 4):
            ExperienceNew = input('Enter New Experience : ')
            dfTeacher.loc[indexno,'Experience'] = ExperienceNew
            dfTeacher.to_csv('lol.csv',header=False,index=False)
        print('Record Updated....')
        print(dfTeacher.loc[dfTeacher['TNO'] == TeacherNo])
        print('-----------------------------------')
        
    #Code for deletion        
    elif (option ==3):
        # Search Record with Teacher number
        TeacherNo = int(input('Enter Teacher Number : '))
        indexno = dfTeacher.loc[dfTeacher['TNO'] == TeacherNo].index
        print('--------------OUTPUT-----------------')
        print(dfTeacher.loc[dfTeacher['TNO'] == TeacherNo])
        deleteconfirm = input('Are You Sure You Want To Delete Record? (Y/N) : ')

        # Code to delete Teacher after confirmation
        if (deleteconfirm == 'Y' or deleteconfirm == 'y'):
            dfTeacher = dfTeacher.drop(indexno)
            print('Record Deleted....')
            dfTeacher.to_csv('teachers.csv',header=False,index=False)
        print('--------------------------------------')
         
    #Code for vieweing records    
    elif (option ==4):
         print('1. Display on the basis of Teacher number')
         print('2. Display on the basis of name')
         print('3. Display on the basis of Subject')
         print('4. Display all records')
         print('5. Display top ___ records')
         print('6. Display bottom ___ records')
         print('7. Back to main menu')
         displaychoice = int(input('Enter your choice : '))
         print('--------------OUTPUT-----------------')
         if (displaychoice == 1):
             TeacherNoDisplay = int(input('Enter Teacher Number : '))
             print(dfTeacher.loc[dfTeacher['TNO'] == TeacherNoDisplay])
         elif (displaychoice == 2):
             nameDisplay = input('Enter Name to Search : ')
             print(dfTeacher.loc[dfTeacher['Name'] == nameDisplay])
         elif (displaychoice == 3):
             SubjectDisplay = input('Enter Subject to Search : ')
             print(dfTeacher.loc[dfTeacher['Subject'] == SubjectDisplay])
         elif (displaychoice == 4):
             print(dfTeacher)
         elif (displaychoice == 5):
             toprecords = int(input('Enter The Top Number of Records to Display : '))
             print(dfTeacher.head(toprecords))
         elif (displaychoice == 6):
             bottomrecords = int(input('Enter The Bottom Number of Records to Display : '))
             print(dfTeacher.tail(bottomrecords))
         print('--------------------------------------')

    #Code to display line chart
    elif (option ==5):
        print('1. Display Teacher wise Experience Bar chart')
        print('2. Back to main menu')
        chartoption = int(input('Enter your choice : '))
        
        #Display Class wise number of Teachers
        if (chartoption == 1):
            names = dfTeacher['Name'].to_list()
            exp = dfTeacher['Experience'].to_list()
            plt.plot(names,exp)
            plt.xlabel('Teachers')
            plt.ylabel('Experience (In Years)')
            plt.title('Teachers Experience')
            plt.show()

            

print('------------Thanks for using Teacher Module----------')
