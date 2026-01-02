# file_Path = open('C:/Clinogensis/August/30-Days-Of-Python-master/files/example.txt')
# text = file_Path.readlines()
# print(text)
# file_Path.close()
# import csv
# with open('C:/Clinogensis/August/30-Days-Of-Python-master/files/csv_example.csv') as f:
#     csv_reader = csv.reader(f, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are :{", ".join(row)}')
#             line_count += 1
#         else:
#             print(
#                 f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
#             line_count += 1
#         print(f'Number of lines:  {line_count}')

import xlrd
excel_book = xlrd.open_workbook('C:/Clinogensis/August/30-Days-Of-Python-master/files/excel_example.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)

