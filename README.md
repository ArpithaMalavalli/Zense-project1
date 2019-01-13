WHAT TO DO

#### 1.In order to run the program using my lms and google accounts,run quickstart.py

 1) This makes changes in my google calendar based on the upcoming events in my LMS
 2) The dialy timetable added into calendar is the first year timetable which is hardcoded
 3) It does not require any modifications to any other file in the cloned directory
  


#### 2.inorder to run program for anyboby else ,use managingEvents_general.py

1)Delete token.json which comes with cloned directory

in managingEvents_general.py:

2)add lms username and password at line 201 and 203
3)change timetable from line 49 to 55 as required
4)when the program is run for the first time it asks for login to google accounts
5)give permission to access calendar



`The events already added are in the events directory.They wont be added again`
