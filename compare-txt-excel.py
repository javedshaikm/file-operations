import xlrd
loc = ('C:\\Users\\shaikjav\\Desktop\\Pending banner.xlsx')
txt = open('C:\\Users\\shaikjav\\Desktop\\Pending-banner.txt').read().splitlines()
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
#ddc = sheet.cell(0,0)
for i in range(sheet.nrows): 
	for lines in txt:
		if  lines in sheet.cell_value(i, 5):
			print (f"{sheet.cell_value(i, 1)} is equal to {lines}")
		else:
			pass
    		#print (f"{sheet.cell_value(i, 1)} is not equal to {lines}")
