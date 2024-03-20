import pytest
from main import menu
from table import print_table, add_record, amend_record, delete_record

data = []
fields = []


def test_add_record():
    #ARRANGE
    new_record = []
    responses = {
        "\nWhat is the Project ID of the record you would like to add:   " : 110,
        "\nWhat is the Project ID of the record you would like to add:   " : 100,
        "\nWhat is the Project name of the record you would like to add:   ": "test_name1",
        "\nWho is the Client of the record you would like to add:   " : "test_client1"
        "\nWhat is the Start Date of the record you would like to add:   "

    }

    #ACT


    #ASSERT



