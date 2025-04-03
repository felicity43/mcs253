"""Assignment 1 - MCS253
Creating Python Objects ~ Lists, Tuples, Dictionaries"""

#Due Date - Submit no later than 4:10 pm on Thursday (3rd April 2025)

#Please type in your name in the next line by way of commenting

#Name: _Margreth.Kuri__________

#-ID-202412245--------------------------------------------------------------

#Quesiton 1

"""Create a python object to store all the courses you are taking this semester.
You may be required to change a course next week."""

Semester_One_Courses=["Discrete Mathematics One","Calculus One","Set Theory and Logic","Data Sturcture and Logic","Computer Programming One"]

#Question 2

"""Store all MCS 253 students ID in a python object. These IDs will be
used for 4 years thus do not change IDs."""

MCS_253_Std_Ids=(202412245,202412236,202412232,2023314260,2023314233,202412253)

#Question 3
"""Since students IDs are a unique identifying number for each student, 

use it as a reference to point to students records. The students records
should consist of full names, gender, DOB,Province of origin & email addresses."""

MCS_253_Std_Records={"202412245":"Fullname:""Margreth Kuri,""Gender:""Female,""DOB:""18-12-98,""Province:""Jiwaka,""Email:""kurimargreth@gmail.com",
"202412236":"Fullname:""Natasha Ricky,""Gender:""Female,""DOB:""05-07-98,""Province:""Eastern Highlands,""Email:""natashajricky@mail.com",
"202412232":"Fullname:""Dahan Timinai,""Gender:""Male,""DOB:""11-11-01,""Province:""Western,""Email:""timinaidahan@gmail.com",
"2023314260":"Fullname:""Jonah Albert,""Gender:""Male,""DOB:""19-05-04,""Province:""Central,""Email:""albertjonah84@gmail.com",
"2023314233":"Fullname:""Rophie Nomoru,""Gender:""Male,""DOB:""19-10-02,""Province:""Morobe,""Email:""rophiejosephnomoru191002@gmail.com",
"202412253":"Fullname:""Junior Robert,""Gender:""Male,""DOB:""12-10-2000,""Province:""Jiwaka,""Email:""juniorwalrob127@gmail.com"}

#Question 4
"""Using indexing, print out your favorite course for the sem (refer to Q1)"""

print(Semester_One_Courses[4])

#Question 5
"""Print out only your student ID from Q2"""

print(MCS_253_Std_Ids[0])


#Question 6
"""Print out all students records (exclude the IDs)"""

print(*MCS_253_Std_Records.values())

#Question 7
"""Print out only your student record"""

print(MCS_253_Std_Records["202412245"])


#Question 8
"""Update the student ID in Q2.
What is the error here?
WHy do you think this happened"""

#print(MCS_253_Std_Ids[202412245])
#It says index error
#This happened because the student ID was in tuple so it can not change because tuple are immutable.

#Question 9
"""Print out the data types for all the objects you have created so far"""

print(type(Semester_One_Courses))
print(type(MCS_253_Std_Ids))
print(type(MCS_253_Std_Records))


#------end of Assignment
#UPLOAD your completed A1 to your GitHub account. Only share the link with me. 