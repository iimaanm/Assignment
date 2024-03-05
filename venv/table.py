# def table():
    import datetime

    # Hard coded data
    data = [
        [100, "Vaccines", "NHS", datetime.date(2020,8,13), datetime.date(2022,10,7), 437, "UK", "Complete"],
        [101, "Fastfood App", "PFC", datetime.date(2023,12,1), datetime.date(2024,12,1), 931, "USA", "In-Progress"],
        [102, "Hydrogen 1", "Nestle", datetime.date(2019,3,30), datetime.date(2023,10,18), 125, "UK", "In-Progress"],
        [103, "Pen Programme", "Bic", datetime.date(2024,4,6), datetime.date(2024,6,6), 740, "Sweden", "Not-Started"],
        [104, "Reusable Paper", "Unilever", datetime.date(2018,1,1), datetime.date(2024,1,1), 864, "UK", "Complete"],
        [105, "App Research", "Lexus", datetime.date(2024,2,11), datetime.date(2024,10,30), 535, "USA", "In-Progress"],
        [106, "Rewards App", "Costa", datetime.date(2023,8,1), datetime.date(2024,12,7), 437, "UK", "In-Progress"],
        [107, "Faster Login", "Emirates", datetime.date(2023,7,7), datetime.date(2024,7,7), 437, "UAE", "In-Progress"],
        [108, "Redevelopment", "Council", datetime.date(2024,12,8), datetime.date(2025,12,8), 437, "UK", "Not-Started"],
        [109, "Transport App", "TFL", datetime.date(2022,2,27), datetime.date(2024,10,7), 437, "UK", "In-Progress"],
    ]
    fields = ["Project ID", "Project Name", "Client", "Start Date", "End Date", "Consultant ID", "Country", "Project Status"]

    # Function to print table
    def print_table(fields, data):
        print ("|", fields[0],"|", fields[1],"   |", fields[2],"     |",fields[3],"|", fields[4],"  |", fields[5],"|", fields[6],"|", fields[7],"|")
        print("-------------------------------------------------------------------------------------------------------------------")
        for item in data:
            print ("|", item[0],(" ")*6,"|",
                    item[1],(" ")*(14-len(item[1])),"|",
                    item[2],(" ")*(10-len(item[2])),"|",
                    item[3],"|",
                    item[4],"|",
                    item[5],(" ")*9,"|",
                    item[6],(" ")*(6-len(item[6])),"|",
                    item[7],(" ")*(13-len(item[7])),"|")
    return (data)
    print_table(fields,data)

#function to add record, data validation to check valid datatype is inputted by user
def add_record():
    import data
    new_record = []
    while len(new_record)<9:
        try:
            new_projectid= int(input("What is the Project ID of the record you would like to add   "))
            new_record.append(new_projectid)
        except TypeError:
            return "Project ID must be a number"
        for id in data[0]:
            if id == new_projectid:
                return "Project ID alread taken"
            

            #add data validation for strings????

            new_projectname= input("What is the Project name of the record you would like to add   ")
            new_record.append(new_projectname)
    
            new_client= input("Who is the Client of the record you would like to add   ")
            new_record.append(new_client)


        try:
            new_startdate= input("What is the Start Date of the record you would like to add   ")
            datetime.datetime.strptime(new_record[3],"%Y-%m-%d")
            new_record.append(new_startdate)
        except TypeError:
            ("Error: Start Date should be in the format YYYY-MM-DD.")
        try:
            new_enddate= input("What is the End Date of the record you would like to add   ")
            datetime.datetime.strptime(new_record[3],"%Y-%m-%d")
            new_record.append(new_enddate)
        except TypeError:
            ("Error: End Date should be in the format YYYY-MM-DD.")

        
        try:
            new_consultantid= int(input("What is the Consultant's ID of the record you would like to add   "))
        except TypeError:
            return "Error: Consultant ID must be a number"
        new_country= input("What is the Country of the record you would like to add   ")
        new_projectstatus= input("What is the Project Status of the record you would like to add   ")

        print(new_record)


        # while len(new_record)<9:
        #     new_item= input("What is the record you would like to add   ")
        #     new_record.append(new_item)

        #     if len(new_record) == 1 and not new_record[0].isdigit():
        #         print("Error: Project ID should be an integer.")
        #         new_record.pop(0)
        #     elif len(new_record) == 2 and not isinstance(new_record[1],str):
        #         print("Error: Project Name should be an string.")
        #         new_record.pop(1)
        #     elif len(new_record) == 3 and not isinstance(new_record[2],str):
        #         print("Error: Client should be an string.")
        #         new_record.pop(2)
        #     elif len(new_record) == 4:
        #         try:
        #             datetime.datetime.strptime(new_record[3],"%Y-%m-%d")
        #         except ValueError:
        #             ("Error: Start Date should be in the format YYYY-MM-DD.")
        #             new_record.pop(3)
        #     elif len(new_record) == 5:
        #         try:
        #             datetime.datetime.strptime(new_record[4],"%Y-%m-%d")
        #         except ValueError:
        #             ("Error: End Date should be in the format YYYY-MM-DD.")
        #             new_record.pop(3)
                
        #         # and not isinstance(new_record[3], datetime.date):
        #     #     print("Error: Start Date should be in the format YYYY-MM-DD.")
            
        #     # elif len(new_record) == 5 and not isinstance(new_record[4], datetime.date):
        #     #     print("Error: End Date should be in the format YYYY-MM-DD.")
        #         new_record.pop(4)
        #     elif len(new_record) == 6 and not isinstance(new_record[5],str):
        #         print("Error: Consultant ID should be an integer.")
        #         new_record.pop(5)
        #     elif len(new_record) == 7 and not isinstance(new_record[6],str):
        #         print("Error: Country should be a string.")
        #         new_record.pop(6)
        #     elif len(new_record) == 8 and not isinstance(new_record[7],str):
        #         print("Error: Project Status should be an integer.")
        #         new_record.pop(7)

        #     else:
        #         pass




    # data.append(new_record)

# add_record()


#function to amend record
def amend_record():
    id_to_amend = int(input("Enter the Project ID of the project you want to amend.    "))

# Using project id to find index of project to amend
    record_index = -1
    for i, record in enumerate(data):
        if record[0] == id_to_amend:
            record_index = i
            break
#Making sure project id exixts
    if record_index == 0:
        print("Record not found.")
        return

    print(f"Amending Project {id_to_amend}...")

    field_to_amend = input("Which field would you like to amend?    ").upper()
    
    if field_to_amend not in fields:
        print(f"Field '{field_to_amend} does not exist")
        return
    
    amended_record = input(f"Enter the new record for {field_to_amend}  ")

    #Amending record
    field_index = fields.index(field_to_amend)
    amended_record = data[record_index][field_index]
    print("\nRecord amended successfuly...")
    
    print_table(fields,data)


add_record()

    