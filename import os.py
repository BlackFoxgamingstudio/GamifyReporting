import os
import pickle
import sys
import csv
import time
import sys
import datetime

from custom_dict import iStr
from custom_dict import iList
from termcolor import colored
import xml.etree.ElementTree as ET




# create workflow docuement section by section with CRUD to each section of the XML template
# create a XML table template with pagenation
# push each printable CSV into its own CSV Template
# push CSV templates in to defreant pages on the XML Table Template
# add a navagation bar for each section of the document and each section of the table
# completed design should have above a xml report document. with supporting data in table below it and a side navagation bar

### FUNCTIONS ###

#def xml_find():
   
#def xml_findall():

#def xml_update():

#def xml_delate():
# report number of support workflows
# report numbeer of new cases
# inventory cases by firmware type
# list of keywords for doc search

#CRUD Docs Query

#CRUD Workflow docs Query

# create new workflow document using report and workflow XML file
#Create
#Update
#Delete
#Read

#def doc_search():
    #custyinput = input('what kind of docs would you like to look up? (please see best keyword matchs)')
    #if(custyinput = 'EDA'):
        #EDADoc = 
        #print EDADoc

#def doc_write():
#after printing report to concole after option to print to CSV, give option to coonect Documentation
# after you chouse yes  
def All_jira():            
    
    counter = 0
    arry2 = []
  
    with open('JIRA_7_2.csv') as master:
        master_indices = dict((r[1], i) for i, r in enumerate(csv.reader(master)))
        
    with open('wincsv4.csv') as hosts:
        with open('new.csv', 'wb') as results:
            reader = csv.reader(hosts)
            writer = csv.writer(results)

            writer.writerow(next(reader, []) + ['RESULTS'])
        
            for row in reader:
                index = master_indices.get(row[3])
                if index is not None:
                    message = 'FOUND in master list (row{})'.format(index)
                else:
                    message = 'NOT FOUND in Master list'
                writer.writerow(row + [message])

def noSubject():
    new_name = input("\n who is the case owner you would like to audit?")
        
    counter = 0
    arry = []
    with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if new_name in row['CaseOwner']:
                    if row['Subject'] =='ExtraHop':
                            output = row['Resolution'], row['Subject'], row['id'], row['JIRANumber']
                            ## by calling output we now can control the output into what is place in to arry and, down the line what is writen in to the csv
                            arry.append(str(output))
                            print(output)
                            counter = counter+1
        print colored("count of all cases with the keyword:",'red'), colored(new_name, 'green'), colored(counter,'red')
        ##I learned how to use zip()! it helps package the array to be unpackage later by the for loop##
        rows = zip(arry)
        question1 = raw_input("would you like to print results to CSV file? (yes/no)")
        if question1 == 'yes':
            with open("nosub.csv", 'wb') as f:
                writer = csv.writer(f)
                for row in rows:
                    writer.writerow(row)
                    print "please go to your home directory and find the CSV file Named - nosub.csv to view your new report!!!"
        else:
            print "glad to help you win, quickly...like a boss"
def QuestionsClean():
    new_name = input("\n who is the case owner you would like to audit?")
        
    counter = 0
    arry = []
    with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if new_name in row['CaseOwner']:
                    if row['Resolution'] =='':
                        if row['Closed'] =='1':
                            output = row['Resolution'], row['Subject'], row['id'], row['JIRANumber']
                            ## by calling output we now can control the output into what is place in to arry and, down the line what is writen in to the csv
                            arry.append(str(output))
                            print(output)
                            counter = counter+1
        print colored("count of all cases with the keyword:",'red'), colored(new_name, 'green'), colored(counter,'red')
        ##I learned how to use zip()! it helps package the array to be unpackage later by the for loop##
        rows = zip(arry)
        question1 = raw_input("would you like to print results to CSV file? (yes/no)")
        if question1 == 'yes':
            with open("emptyresolutions.csv", 'wb') as f:
                writer = csv.writer(f)
                for row in rows:
                    writer.writerow(row)
                    print "please go to your home directory and find the CSV file Named - csvwritest.csv to view your new report!!!"
        else:
            print "glad to help you win, quickly...like a boss"

def emptyresolutions():
    new_name = input("\n who is the case owner you would like to audit?")
        
    counter = 0
    arry = []
    with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if new_name in row['CaseOwner']:
                    if row['Resolution'] =='':
                        if row['Closed'] =='1':
                            output = row['Resolution'], row['Subject'], row['id'], row['JIRANumber']
                            ## by calling output we now can control the output into what is place in to arry and, down the line what is writen in to the csv
                            arry.append(str(output))
                            print(output)
                            counter = counter+1
        print colored("count of all cases with the keyword:",'red'), colored(new_name, 'green'), colored(counter,'red')
        ##I learned how to use zip()! it helps package the array to be unpackage later by the for loop##
        rows = zip(arry)
        question1 = raw_input("would you like to print results to CSV file? (yes/no)")
        if question1 == 'yes':
            with open("emptyresolutions.csv", 'wb') as f:
                writer = csv.writer(f)
                for row in rows:
                    writer.writerow(row)
                    print "please go to your home directory and find the CSV file Named - csvwritest.csv to view your new report!!!"
        else:
            print "glad to help you win, quickly...like a boss"
def nolic():
    new_name = input("\n who is the case owner you would like to audit?")
    
    counter = 0
    arry = []
    with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if new_name in row['CaseOwner']:
                    if row['License'] =='':
                        output = row['License'], row['Subject'], row['id']
                        ## by calling output we now can control the output into what is place in to arry and, down the line what is writen in to the csv
                        arry.append(str(output))
                        print(output)
                        counter = counter+1
        print colored("count of all cases with the keyword:",'red'), colored(new_name, 'green'), colored(counter,'red')
        ##I learned how to use zip()! it helps package the array to be unpackage later by the for loop##
        rows = zip(arry)
        question1 = raw_input("would you like to print results to CSV file? (yes/no)")
        if question1 == 'yes':
            with open("nolic.csv", 'wb') as f:
                writer = csv.writer(f)
                for row in rows:
                    writer.writerow(row)
                    print "please go to your home directory and find the CSV file Named - csvwritest.csv to view your new report!!!"
        else:
            print "glad to help you win, quickly...like a boss"
def createxml():
    #add a record-but we would need to check for duplicates first
    #ask the user for the student email address to search for
    n =input("Enter the workflow ID of the student you want to search for: ")    
    exists=recordExists(n)
    if exists==False:
        
        #gt a new id
        nid=newid()

        #get the field values from the user
        print("Create a record")
        SUBJECT=input("SUBJECT:")
        ACTOR=input("ACTOR:")
        TOPIC=input("TOPIC:")
        DEVICE=input("DEVICE:")
        VERSION=input("VERSION:")
        PRECONDITION=input("PRECONDITION:")
        TRIGGER=input("TRIGGER:")
        POSTCONDITION=input("POSTCONDITION:")
        NORMALFLOW=input("NORMALFLOW:")
        ALTERNATIEFLOW=input("ALTERNATIEFLOW:")
        ISSUE=input("ISSUE")
        SOLUTION=input("SOLUTION")
        CASE=input("CASE")
        JIRA=input("JIRA")
        DOCS=input("DOCS")

        #create a contact element at root level
        newrecord = ET.SubElement(root, "USECASE1",ID=str(nid))

        #add the fields into out new record
        ET.SubElement(newrecord, "ID", name="ID").text = str(nid)
        ET.SubElement(newrecord, "SUBJECT", name="SUBJECT").text = SUBJECT
        ET.SubElement(newrecord, "ACTOR", name="ACTOR").text = ACTOR
        ET.SubElement(newrecord, "TOPIC", name="TOPIC").text = TOPIC
        ET.SubElement(newrecord, "DEVICE", name="DEVICE").text = DEVICE
        ET.SubElement(newrecord, "VERSION", name="VERSION").text = VERSION
        ET.SubElement(newrecord, "PRECONDITION", name="VERSION").text = VERSION
        ET.SubElement(newrecord, "NORMALFLOW", name="VERSION").text = VERSION
        ET.SubElement(newrecord, "ALTERNATIEFLOW", name="VERSION").text = VERSION
        ET.SubElement(newrecord, "ISSUE", name="VERSION").text = VERSION
        ET.SubElement(newrecord, "SOLUTION", name="VERSION").text = SOLUTION
        ET.SubElement(newrecord, "CASE", name="CASE").text = CASE
        ET.SubElement(newrecord, "JIRA", name="JIRA").text = JIRA
        ET.SubElement(newrecord, "DOCS", name="DOCS").text = DOCS
        #finally save the update
        ntree.write("template1.xml")    

    else:
        print("--------------------------------------------")
        print("Record already exists")
        print("--------------------------------------------")
def print_xmltest():
    tree = ET.parse('template1.xml')
    root = fromstring(xml_text)
    for Workflow1 in root.findall(''):
        Subject = Workflow1.find('')
        print(Subject.text)
# print all solutions
def print_usecase():
   tree = ET.parse('template1.xml')
   root = tree.getroot()
   for USECASE1 in root.iter('USECASE1'):
    Subject = USECASE1.find('SUBJECT').text
    Actor = USECASE1.find('ACTOR').text
    Case = USECASE1.find('CASE').text
    Jira = USECASE1.find('JIRA').text
    docs = USECASE1.find('DOCS').text
    solution = USECASE1.find('SOLUTION').text
    print(Subject,Actor,Case,Jira,docs,solution)

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print(colored("\t****************************************************************************", 'green'))
    print(colored("\t*******************  Greeter - Hello old and new friends!  ****************", 'blue'))
    print(colored("\t***  Morphaus here, your knowledge Base for support is ready. are you?  ***", 'red'))
    print(colored("\t****************************************************************************", 'green'))

    
def all_cases():
    # Shows the names of everyone who is already in the list.
    print("\nHere are all the issues since russell start working at extrahop.\n")
    time.sleep(5)
    with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        counter = 0
        for row in reader:
            print(row['Subject'],row['DateTimeOpened'], row['CaseOwner'],row['id'],row['JIRANumber'])
            counter = counter+1
        time.sleep(5)
        print colored("count of all cases: ",'red'), colored(counter,'red')
def Largest():
   with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        my_list = []

        for row in reader:
            my_list.append(row['DateTimeOpened'])
        return my_list[0]

def Smallest():
   with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        my_list = []

        for row in reader:
            my_list.append(row['DateTimeOpened'])
        return my_list[-1]
def get_user_choice():
       
     
    # Let users know what they can do.
        print '[1] See all cases from',Largest(),'to',Smallest()
        print "[2] search for a case by case name"
        print "[3] Search by case name for a case with a JIRANumber"
        print '[4] Print example xml file'
        print "[5] Clean up Lic's"
        print "[6] Clean up empty resolutions"
        print "[7] print all Jira esculations"
        print "[8] Clen up Case Types"
        return input("What would you like to do?")

## ad case insensitive to search funcationality: https://micropyramid.com/blog/how-to-implement-case-insensitive-csv-Insensitivecsv.DictReader-in-python/

def cases_by_keyword():
    # Asks the user for a new name, and stores the name if we don't already
    #  know about this person.
    new_name = input("\n What kind of issue(VMWare, EDA, ECA, EXA, ERSPAN, Triggers, LDAP, netflow, Datastore, Addy)? : ")
    
    counter = 0
    arry = []
    with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if new_name in row['Subject']:
                output = row['CaseOwner'], row['Subject'], row['id']
                ## by calling output we now can control the output into what is place in to arry and, down the line what is writen in to the csv
                arry.append(str(output))
                print(output)
                counter = counter+1
        time.sleep(5)
        print colored("count of all cases with the keyword:",'red'), colored(new_name, 'green'), colored(counter,'red')
        ##I learned how to use zip()! it helps package the array to be unpackage later by the for loop##
        rows = zip(arry)
        question1 = raw_input("would you like to print results to CSV file? (yes/no)")
        if question1 == 'yes':
            with open("csvwritest.csv", 'wb') as f:
                writer = csv.writer(f)
                for row in rows:
                    writer.writerow(row)
                    print "please go to your home directory and find the CSV file Named - csvwritest.csv to view your new report!!!"
        else:
            print "glad to help you win, quickly...like a boss"

            
## ad case insensitive to search funcationality: https://micropyramid.com/blog/how-to-implement-case-insensitive-csv-Insensitivecsv.DictReader-in-python/

def cases_by_keyword_has_jira():            
    
    new_name = input("\n What kind of issue(VMWare, EDA, ECA, EXA, ERSPAN, Triggers, LDAP, netflow, Datastore, Addy)? : ")
    counter = 0
    arry2 = []
  
    with open('wincsv4.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row['JIRANumber'] != '':

                if new_name in row['Subject']:
                    output2 = row['CaseOwner'],row['Subject'],row['id'],row['JIRANumber'],row['Resolution']
                    arry2.append(str(output2))
                    print(output2)
                    counter = counter+1
        time.sleep(5)
        print colored("Count of Jira tickets with the keyword:", 'red'), colored(new_name, 'green'), colored(counter,'red') 
        rows = zip(arry2)
        question2 = raw_input("would you like to print results to CSV file? (yes/no)")
        if question2 == 'yes':
            with open("csvwritestjira.csv", 'wb') as f2:
                writer = csv.writer(f2)
                writer.writeheader()
                for row in rows:
                    writer.writerow(row)
                    print "please go to your home directory and find the CSV file Named - csvwritestjira.csv to view your new report!!!"
        else:
            print "glad to help you win, quickly...like a boss"
def get_new_name():
    # Asks the user for a new name, and stores the name if we don't already
    #  know about this person.
    new_name = input("\nPlease tell me this person's name: ")
    if new_name in names:
        print("\n%s is an old friend! Thank you, though." % new_name.title())
    else:
        names.append(new_name)
        print("\nI'm so happy to know %s!\n" % new_name.title())
        
def load_names():
    # This function loads names from a file, and puts them in the list 'names'.
    #  If the file doesn't exist, it creates an empty list.
    try:
        file_object = open('names.pydata', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names
    except Exception as e:
        print(e)
        return []
        
def quit():
    # This function dumps the names into a file, and prints a quit message.
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(names, file_object)
        file_object.close()
        print("\nThanks for playing. I will remember these good friends.")
    except Exception as e:
        print("\nThanks for playing. I won't be able to remember these names.")
        print(e)

### LVL TWO ####
def get_user_choice2():
       
     
    # Let users know what they can do.
        print '[1] PRINT REPORT'
        return input("What would you like to do?")



### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
names = load_names()

choice = ''


display_title_bar()
while choice != 'q':    
    
    choice = get_user_choice()
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == 1:
        all_cases()
    elif choice == 2:
        cases_by_keyword()
    elif choice == 3:
        cases_by_keyword_has_jira()
    elif choice == 4:
        print_usecase()
    elif choice == 5:
        nolic()
    elif choice == 6:
        emptyresolutions()
    elif choice == 7:
        All_jira()
    elif choice == 'q':
        quit()
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")
###Part2###choice2 = ''
   
    
    
    # Respond to the user's choice.
 
