# ProfileChecker
Checks Profile is Duplicate or Not with given fields


--- 
## Requirements
* Python 3 
### Third Party Libraries used
 * fuzzywuzzy 
```
  pip install fuzzywuzzy
  pip install python-Levenshtein
```
## Usage
import class
```
from ProfileChecker import ProfileChecker
```
### input
1. profiles [ list of 2 profiles with dictionary type ] 
2. fields [ list of fields for comparision ]
==> Model default fields : </br>
**string Type** : 'email', 'first_name', 'last_name', 'date_of_birth' (YYYY-MM-DD)</br>
**integer Type** : 'class_year'
 
#### format :
```
p1 = { id: 1, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': '1990-10-11' }
p2 = { id: 2, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai1', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': '1990-10-11'}
fields = ['first_name','last_name','email','class_year','date_of_birth']
profiles = [p1,p2]
```
### find_duplicates
**find_duplicates(profiles,fields)** takes 2 arguments 
```
p = ProfileChecker()
result = p.find_duplicates(profiles,fields)
```
### output
**result** : returns str: 'Duplicate' or 'Not Duplicate'<br />
**total_score** : returns int type of total score for each fields (greater than 1 => Duplicate else Non-Duplicate) <br />
**matching_attributes** : returns list of fields which matches with given constraints <br />
**non_matching_attributes** : returns list of fields which doesnot match with given constraints <br />
**ignored_attributes**: returns list of fields which are None or not taken into consideration with given constraints <br />
```
print(result)
>> {'result': 'Duplicate', 'total_score': 3, 'matching_attributes': ['class_year', 'date_of_birth', 'email', 'first_name', 'last_name'], 'non_matching_attributes': [None], 'ignored_attributes': [None]}
```

## Constrains
1. if first_name + last_name + email has match > 80%, then => score = +1
2. if same class year, then => score = +1 | elif either is None, then => score = score | else no match, then => score = -1
3. Rule 2 for date_of_birth

## Extras
* extra fields can be added  to fields of either string or Integer type
```
p1 = { id: 1,'college':'ITM Universe', 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai', 'last_name': 'Patel', 'class_year': 2012, 'date_of_birth': '1990-10-11'}
p2 = { id: 2,'college':'itm university', 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai1', 'last_name': 'Shah', 'class_year': 2012, 'date_of_birth': '1990-10-11'}

profiles = [p1,p2]
# ADD required fields
fields = ['first_name','last_name','email','class_year','date_of_birth','college']

p = ProfileChecker()
result = p.find_duplicates(profiles,fields)
print(result)
```
### Output
```
{'result': 'Duplicate', 'total_score': 4, 'matching_attributes': ['class_year', 'date_of_birth', 'college', 'email', 'first_name', 'last_name'], 'non_matching_attributes': [None], 'ignored_attributes': [None]}
```

