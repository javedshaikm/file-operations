import xlrd
#Location of the text file 
loc = ('C:\\Users\\shaikjav\\Desktop\\Pending banner.xlsx')
#location of the excel file to be compared
txt = open('C:\\Users\\shaikjav\\Desktop\\Pending-banner.txt').read().splitlines()
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
ddc = sheet.cell_value(0,0)
for i in range(sheet.nrows): 
   for lines in txt:
    	if sheet.cell_value(i, 5) == lines:
    		print (f"{sheet.cell_value(i, 5)} is present")
    	else:
    		pass
    		#print (f"{sheet.cell_value(i, 1)} is not equal to {lines}")
