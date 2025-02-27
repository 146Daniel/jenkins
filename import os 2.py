import os 
import xlsxwriter
folder_path  = r"/Users/danielalimov/Documents"
#folder_name = input("Enter the name of the folder you want to create: ")
#os.mkdir(folder_path + "/" + folder_name)
#if os.path.exists(folder_path + "/" + folder_name):
#    print("Folder created successfully")
#else:
#    print("Error creating the folder : ")

excel_file  = xlsxwriter.Workbook(folder_path + "/" + "newxlsxfile" ".xlsx")
sheet = excel_file.add_worksheet()
sheet.write("A2", "Hello World")
excel_file.close()
print("Excel file created successfully")
