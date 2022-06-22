###constraints
#1) if first_name + last_name + email has match > 80%, then => score = +1 (DONE)
#2) if same class year, then => score = +1 | elif either is None, then => score = score | else no match, then => score = -1(DONE)
#3) Rule 2 for birthday (DONE)

##Results
# if self.total_score > 1, then profiles are duplicate

##I/O
# input : Dict
# output : Dict [result,total_match_score,matching_attributes,self.ignored_attributes]

##Optimization
# fast processing [threads on constraints]
# support more fields [kwargs]

### algos used : fuzzywuzzy


from ProfileChecker import ProfileChecker

# UNCOMMENT required eg and run file
#
##Eg 1
# p1 = { id: 1, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': '1990-10-11' }
# p2 = { id: 2, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai1', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': '1990-10-11'}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Eg 2
# p1 = { id: 1, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai', 'last_name': 'Shah', 'class_year': None, 'date_of_birth': None}
# p2 = { id: 2, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai1', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': '1990-10-11'}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Eg 3
# p1 = { id: 1, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai', 'last_name': 'Shah', 'class_year': None, 'date_of_birth': None}
# p2 = { id: 2, 'email': 'knowkanhai+donotcompare@gmail.com', 'first_name': 'Kanhai1', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': '1990-10-11'}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Eg 4
# p1 = { id: 1, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai', 'last_name': 'Shah', 'class_year': None, 'date_of_birth': '1990-10-11' }
# p2 = { id: 2, 'email': None, 'first_name': 'Kanhai1', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': None}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Eg 5
p1 = { id: 1, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai', 'last_name': 'Patel', 'class_year': 2012, 'date_of_birth': '1990-10-11' ,'college':'ITM Universe'}
p2 = { id: 2, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai1', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': '1990-10-11','college':'itm university'}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#
# UNCOMMENT required eg and run file

profiles = [p1,p2]
# ADD required fields
fields = ['first_name','last_name','email','class_year','date_of_birth','college']

p = ProfileChecker()
print(p.find_duplicates(profiles,fields))


