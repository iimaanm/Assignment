# from tabulate import tabulate
import datetime

def table():
    fields = ["Project ID", "Project Name", "Client", "Start Date", "End Date", "Consultant ID", "Country", "Project Status"]

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
            
    print_table(fields,data)

table()
