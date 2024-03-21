import pytest
import table as table



def mock_input(prompt):
    responses = {"\nWhat is the Project ID of the record you would like to add:   ": 100,
                 "\nWhat is the Project name of the record you would like to add:   ": "Test",
                 "\nWho is the Client of the record you would like to add:   ": "Test",
                 "\nWhat is the Start Date of the record you would like to add:   ": 2011-11-11,
                 "\nWhat is the End Date of the record you would like to add:   ": 2012-12-12,
                 "\nWhat is the Consultant ID of the record you would like to add:   ": 100,
                 "\nWhat is the Country of the record you would like to add:   ": "Test",
                 "\nWhat is the Project Status of the record you would like to add (/3):   ": 0}
    return responses(prompt)

def test_add_record_success(monkeypatch):
    #ARRANGE
    new_record = []
    monkeypatch.setattr('builtins.input', mock_input)

    #ACT
    output = add_record(fields,data)

    #ASSERT
    assert output == "The new record has been added succesfully."



with pytest.raises(ValueError):
    int(input("\nWhat is the Country of the record you would like to add:   " ))