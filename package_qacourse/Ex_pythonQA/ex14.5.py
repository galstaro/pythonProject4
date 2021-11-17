from openpyxl import Workbook
import json

workbook = Workbook()
sheet = workbook.active

sheet["A2"] = "Category"
sheet["A3"] = "Product ID"
sheet["A4"] = "Quantity"
sheet["A5"] = "Color"
sheet["B1"] = "Test 1"
sheet["B2"] = "speakers"
sheet["B3"] = 19
sheet["B4"] = 2
sheet["B5"] = "RED"
sheet["C1"] = "Test 2"
sheet["C2"] = "headphones"
sheet["C3"] = 12
sheet["C4"] = 2
sheet["C5"] = "Purple"
sheet["D1"] = "Test 3"
sheet["D2"] = "mice"
sheet["D3"] = 28
sheet["D5"] = "GREEN"
sheet["E1"] = "Test 4"
sheet["E2"] = "mice"
sheet["E3"] = 30
sheet["E4"] = 1
sheet["F1"] = "Test 5"
sheet["F2"] = "laptops"
sheet["F3"] = 9
sheet["F4"] = 2
sheet["F5"] = "BLUE"
sheet["G1"] = "Test 6"
sheet["G2"] = "laptops"
sheet["G3"] = 7
sheet["G4"] = 3
sheet["H1"] = "Test 7"
sheet["H2"] = "tablets"
sheet["H3"] = 18
sheet["H5"] = "yellow"

tests={}
for column in sheet.iter_cols(1,8,1,5,True):
    print(column)
    if column[0] is None:
        continue
    else:
        test_number=column[0]
        test={
            "Category":column[1],
            "Product ID": column[2],
            "Quantity": column[3],
            "Color": column[4]
        }
        tests[test_number]=test

print(json.dumps(tests,indent=4))

workbook.save(filename="TestData_EX.xlsx")