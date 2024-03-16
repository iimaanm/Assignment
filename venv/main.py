# from table import data,fields, add_record, amend_record
# import datetime




def menu():

    print("\n------------- Main Menu -------------")
    print("1. Add Record")
    print("2. Amend Record")
    print("3. Delete Record")
    print("4. Display Full Details")
    print("5. Exit")

while True:
    menu()
    selected = int(input("Choose a menu option (1-5):   "))

    if selected == 1:
        add_record()

    elif selected == '2':
        amend_record()
    # elif selected == '3':
    #         # .delete_record()
    # elif selected == '4':
    #         # .display_full_details()
    # elif selected == '5':
    #     print("Exiting... ")
    #     break
    # #Range check
    # else:
    #      print("Error. Please enter a valid menu option (1-5).")
    