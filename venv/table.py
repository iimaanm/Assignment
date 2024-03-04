from tabulate import tabulate
import datetime

def table():


    fields = ["Project ID", "Project Name", "Client", "Start Date", "End Date", "Consultant ID", "Country", "Project Status"]

# Hard coded data
    data = [
        [1, "Vaccine Programme", "NHS", datetime.date(2020,8,13), datetime.date(2022,10,7), 437, "UK", "Complete"],
        [2, "Fastfood Digitalisation", "PFC", datetime.date(2023,12,1), datetime.date(2024,12,1), 931, "USA", "In Progress"],
        [3, "Hydrogen Packaging", "Nestle", datetime.date(2019,3,30), datetime.date(2023,10,18), 125, "UK", "In Progress"],
        [4, "Pen Programme", "Bic", datetime.date(2024,4,6), datetime.date(2024,6,6), 740, "Sweden", "Not Started"],
        [5, "Reusable Paper", "Unilever", datetime.date(2018,1,1), datetime.date(2024,1,1), 864, "UK", "Complete"],
        [6, "Consumer Research", "Lexus", datetime.date(2024,2,11), datetime.date(2024,10,30), 535, "USA", "In Progress"],
        [7, "Rewards App", "Krispy Kreme", datetime.date(2023,8,1), datetime.date(2024,12,7), 437, "UK", "In Progress"],
        [8, "Faster Login", "British Airways", datetime.date(2023,7,7), datetime.date(2024,7,7), 437, "UK", "In Progress"],
        [9, "Redevelopment Programme", "Hackney Council", datetime.date(2024,12,8), datetime.date(2025,12,8), 437, "UK", "Not Started"],
        [10, "Transport Research", "TFL", datetime.date(2022,2,27), datetime.date(2024,10,7), 437, "UK", "In Progress"],
        
        # Add more rows as needed
    ]

    # Function to print a formatted table
    def print_table(field_names, data):
        # Calculate the maximum width for each column
        max_widths = [max(len(str(field)), max(len(str(row[i])) for row in data)) for i, field in enumerate(field_names)]

        # Print the header
        header = " | ".join(f"{field:<{max_widths[i]}}" for i, field in enumerate(field_names))
        print(header)
        print("-" * len(header))

        # Print the data rows
        for row in data:
            row_str = " | ".join(f"{str(row[i]):<{max_widths[i]}}" for i in range(len(row)))
            print(row_str)

    # Print the table
    print_table(field_names, data)