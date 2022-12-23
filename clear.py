import xlwings as xw
from xlrd import open_workbook
from xlutils.copy import copy

#clear existing xls file

def clearSheet():    #close workbook if already open
    try:
        openBook = xw.Book("C:/Users/Kylew/CS/sports betting/windSpeedDirection.xls")
        openBook.close()
    except Exception as e:
        print(e)

    #open work bork
    rb = open_workbook("windSpeedDirection.xls")
    wb = copy(rb)
    sheet1 = wb.get_sheet('Sheet 1')

    deleteRows = 12
    deleteColumns = 28

    row = 1
    column = 0

    rowIndex = deleteRows

    for col in range(deleteColumns):
        sheet1.write(0, column, '')
        for i in range(rowIndex):
            if rowIndex == 0: break
            sheet1.write(row, column, '')
            sheet1.write(row, column + 1, '')
            sheet1.write(row, column + 2, '')
            row = row+1
            rowIndex = rowIndex - 1
        row = 1
        column = column + 4
        rowIndex = deleteRows

    wb.save('windSpeedDirection.xls')