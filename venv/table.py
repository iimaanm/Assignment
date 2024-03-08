import datetime
from tabulate import tabulate
    # Hard coded data
data = [
    [100, "VACCINES", "NHS", datetime.date(2020,8,13), datetime.date(2022,10,7), 437, "UK", 3],
    [101, "FASTFOOD APP", "PFC", datetime.date(2023,12,1), datetime.date(2024,12,1), 931, "USA", 1],
    [102, "HYDROGEN X", "NESTLE", datetime.date(2019,3,30), datetime.date(2023,10,18), 125, "UK", 3],
    [103, "PEN PROGRAMME", "BIC", datetime.date(2024,4,6), datetime.date(2024,6,6), 740, "Sweden", 0],
    [104, "REUSABLE PAPER", "UNILEVER", datetime.date(2018,1,1), datetime.date(2024,1,1), 864, "UK", 3],
    [105, "APP RESEARCH", "LEXUS", datetime.date(2024,2,11), datetime.date(2024,10,30), 535, "USA", 1],
    [106, "REWARDS APP", "COSTA", datetime.date(2023,8,1), datetime.date(2024,12,7), 437, "UK", 1],
    [107, "FASTER LOGIN", "EVENTBRITE", datetime.date(2023,7,7), datetime.date(2024,7,7), 437, "UAE", 2],
    [108, "REDEVELOPMENT", "COUNCIL", datetime.date(2024,12,8), datetime.date(2025,12,8), 437, "UK", 0],
    [109, "TRANSPORT APP", "TFL", datetime.date(2022,2,27), datetime.date(2024,10,7), 437, "UK", 2],
]
fields = [" PROJECT ID", "PROJECT NAME", "CLIENT", "START DATE", "END DATE", "CONSULTANT ID", "COUNTRY", "STATUS (/3)"]

 # Function to print table
def print_table(fields, data):
    table = tabulate(data, fields, tablefmt = "pretty")
    print(table)

print_table(fields, data)
    

#Function to add record, data validation to check valid datatype is inputted by user.
def add_record(data):
    new_record = []

#Project ID is the Primary Key and therefore cannot be duplicated.
    while len(new_record)<=1:
        try:
            new_projectid = int(input("\nWhat is the Project ID of the record you would like to add:   "))
            duplicate = any(new_projectid == row[0] for row in data)

            if duplicate:
                print("\nProject ID already taken")
            else:
                new_record.append(new_projectid)
                print(new_record)
                break  # Breaks the loop if the project ID is not taken.

        except ValueError:
            print("\nError: Project ID must be a number")   

#Project name can be int or str.
    while len(new_record)<2:
        new_projectname= input("\nWhat is the Project name of the record you would like to add:   ")
        new_record.append(new_projectname)
        print(new_record)

#Client can be int or str.
    while len(new_record)<3:
        new_client= input("\nWho is the Client of the record you would like to add:   ")
        new_record.append(new_client)
        print(new_record)

#Checking start date is in datetime format.
    while len(new_record)<4:    
        try:
            new_startdate= input("\nWhat is the Start Date of the record you would like to add:   ")
            new_record.append(new_startdate)
            datetime.datetime.strptime(new_record[3],"%Y-%m-%d")
            print(new_record)
        except ValueError:
            print("\nError: Start Date should be in the format YYYY-MM-DD.")
            new_record.pop(-1)

#Checking enddate is in datetime format and is after start date.
    while len(new_record)<5:
        try:
            new_enddate= input("\nWhat is the End Date of the record you would like to add:   ")
            if new_enddate<new_startdate: 
                print(f"\nEnd date cannot be before {new_startdate}")
            else:
                new_record.append(new_enddate)
                datetime.datetime.strptime(new_record[4],"%Y-%m-%d")
                print(new_record)
        except ValueError:
            print("\nError: End Date should be in the format YYYY-MM-DD.")
            new_record.pop(-1)

#Checking consultant ID is a number.
    while len(new_record)<6:    
        try:
            new_consultantid= int(input("\nWhat is the Consultant's ID of the record you would like to add:   "))
            new_record.append(new_consultantid)
            print(new_record)
        except ValueError:
            print("\nError: Consultant ID must be a number")
             

# Checking country is a string.
    while len(new_record)<7:    
        new_country = input("\nWhat is the Country of the record you would like to add:   ")
        try:
            int(new_country)
            print ("\nError: Country must be a string")
        except ValueError:
            new_record.append(new_country)
            print(new_record)
 
#Checking project status is between 0-3.
    while len(new_record)<8:    
        try:
            new_projectstatus= int(input("\nWhat is the Project Status of the record you would like to add (/3):   "))
            if 0<=new_projectstatus<4:
                new_record.append(new_projectstatus)
                print(new_record)
            else:
                print ("\nError: Project Status must be a number 0-3")
        except ValueError:
            print ("\nError: Project Status must be a number 0-3")
    
    data.append(new_record)
    print_table(fields,data)
        
# add_record(data)


#function to amend record
def amend_record(fields,data):
    id_to_amend = int(input("Enter the Project ID of the project you want to amend.    "))
    record_doesnt_exist= True
# Using project id to find index of project to amend



    record_index = -1
    for i, record in enumerate(data):
        if record[0] == id_to_amend:
            record_index = i
            break

        # Making sure project id exists
    if record_index == -1:
        print("Record not found.")
    else:
        print(f"Amending Project {id_to_amend}...")

#     # for i, record in enumerate(data):
#     #     if record[0] == id_to_amend:
#     #         record_index = i
#     #         break
# #Making sure project id exixts
#     while record_doesnt_exist == True:
#         if record_index == -1:
#             print("Record not found.")
#             record_doesnt_exist == True
#         else:
#             record_doesnt_exist = False
            


    field_to_amend = input("Which field would you like to amend?    ").upper()
    if field_to_amend not in fields:
        print(f"Field {field_to_amend} does not exist")
    else:
        #Checking Project ID is an integer and is not duplicated.
        if field_to_amend == "PROJECT ID":
            try:
                new_projectid = int(input(f"Enter the new record for {field_to_amend}:   "))
                duplicate = any(new_projectid == row[0] for row in data)

                if duplicate:
                    print("\nProject ID already taken")
                else:
                    field_index = fields.index(field_to_amend)
                    data[record_index][field_index] = new_projectid
                    print("\nRecord amended successfuly...")
                    # break 
            except ValueError:
                print("\nError: Project ID must be a number") 
        #Checking start date is in datetime format.
        if field_to_amend == "START DATE":
            try:
                new_startdate=  input(f"Enter the new record for {field_to_amend}:   ")
                datetime.datetime.strptime(new_startdate,"%Y-%m-%d")
                field_index = fields.index(field_to_amend)
                data[record_index][field_index] = new_startdate
                print("\nRecord amended successfuly...")
            except ValueError:
                print("\nError: Start Date should be in the format YYYY-MM-DD.")
            
        new_startdate = data[record_index][fields.index("START DATE")]

        
        #Checking enddate is in datetime format and is after start date.
        if field_to_amend == "END DATE":
            try:
                new_enddate=  input(f"Enter the new record for {field_to_amend}:   ")
                if new_enddate<new_startdate: 
                    print(f"\nEnd date cannot be before {new_startdate}")
                else:
                    datetime.datetime.strptime(new_enddate,"%Y-%m-%d")
                    field_index = fields.index(field_to_amend)
                    data[record_index][field_index] = new_enddate
                    print("\nRecord amended successfuly...")
            except ValueError:
                print("\nError: End Date should be in the format YYYY-MM-DD.")
            

        
        #Checking input is in string format
        if field_to_amend == "PROJECT NAME" or field_to_amend == "COUNTRY" or field_to_amend == "CLIENT":
            try:
                new_string= str(input(f"Enter the new record for {field_to_amend}:   ")).upper()
                field_index = fields.index(field_to_amend)
                data[record_index][field_index] = new_string
                print("\nRecord amended successfuly...")
            except TypeError:
                print(f"\nError: {field_to_amend} must be a string") 
  
        #Checking input is in integer format
        if field_to_amend == "CONSULTANT ID" or field_to_amend == "STATUS":
            try:
                new_integer= int(input(f"Enter the new record for {field_to_amend}:   "))
                field_index = fields.index(field_to_amend)
                data[record_index][field_index] = new_integer
                print("\nRecord amended successfuly...")
            except TypeError:
                print(f"\nError: {field_to_amend} must be an integer") 

        

        # #Amending record
        # field_index = fields.index(field_to_amend)
        # data[record_index][field_index] = amended_record_value
        # print("\nRecord amended successfuly...")
        
        print_table(fields,data)



amend_record(fields,data)