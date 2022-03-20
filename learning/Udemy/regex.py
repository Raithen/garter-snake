import re

message = 'Call me at 734-707-3952 today. Call my office at 734-647-5822'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
 #This returns a "Match Object"
 #Create groups in RegEx by using the () ex: (\d\d\d)
 #To search for () with RegEx, use the \ to escpae. Ex: \(\d\d\d\)
print(mo.group()) 
areaCode = mo.group(1)
phoneNumber = mo.group(2)

print(f'Area Code: {areaCode}\nPhone Number: {phoneNumber}')

#Use the pipe Character to match one of many terms.
#This will search for "batman, batmobile, batcycle"
batRegEx = re.compile(r'bat(man|mobile|cycle)')
batmo = batRegEx.search('I am batman and this is my famous batmobile')
print(batmo.group(1))