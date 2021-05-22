import xlrd
from utils.data import LoginData, SearchData


class ExcelReader:

    @staticmethod
    def get_data_log_in_passed():
        wb = xlrd.open_workbook('../utils/log_in_data.xlsx')
        sheet = wb.sheet_by_index(0)

        data = []
        for i in range(1, sheet.nrows):
            login_data = LoginData(sheet.cell(i, 0).value, sheet.cell(i, 1).value)
            data.append(login_data)
        return data

    @staticmethod
    def get_data_log_in_fail():
        wb = xlrd.open_workbook('../utils/log_in_data.xlsx')
        sheet = wb.sheet_by_index(1)

        data = []
        for i in range(1, sheet.nrows):
            login_data = LoginData(sheet.cell(i, 0).value, sheet.cell(i, 1).value)
            data.append(login_data)
        return data

    @staticmethod
    def search_data():
        wb = xlrd.open_workbook('../utils/add_to_cart_data.xlsx')
        sheet = wb.sheet_by_index(0)

        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchData(sheet.cell(i, 0).value)
            data.append(search_data)
        return data