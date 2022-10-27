# @Name: Ravit Anuvongnukroh
# @id: 6420421008

import CI4003_expense_connect_database


class ExpenseTK:
    def __init__(self, name, amount=0.0, date="", type_ex=""):
        self.name = name
        self.amount = amount
        self.date = date
        self.type_ex = type_ex

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected Character")
        self._name = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Expected Number")
        self._amount = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected Character")
        self._date = value

    @property
    def type_ex(self):
        return self._type_ex

    @type_ex.setter
    def type_ex(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected Character")
        self._type_ex = value

    def __str__(self):
        return f"{self.name}, {self.amount}, {self.date}, {self.type_ex}"


class CalExpense:
    def __init__(self):
        self.expenseTK = []

    def add(self, qp):
        self.expenseTK.append(qp)

    # def items(self):
    #     for i in self.expenseTK:
    #         print(i)

    # def total(self):
    #     total = 0
    #     for i in self.expenseTK:
    #         total += i[1]
    #     return total

    # def update(self, na, da, am):
    #     for idx, item in enumerate(self.expenseTK):
    #         if na == item[0] and da == item[2]:
    #             self.expenseTK[idx][1] = am
    #             print("Updated")


# def display_expense(expenseTK, halo=0):
#     print("-" * 77)
#     print(f"{'No.':12}{'Goods Or Services':>16}{'Category':>16}{'Dates':>16}{'Amounts':>16}")
#     print("-" * 77)
#     for (i, item) in enumerate(expenseTK, start=1):
#         print(f"{i}{item[0]:>28}{item[3]:>16}{item[2]:>16}{item[1]:>16}")
#     if halo == 0:
#         print(f"{'There is no data in the dashboard.':>55}")
#         print("-" * 77)
#     elif halo > 0:
#         print("-" * 77)
#         print(f"{'TOTAL'}{halo:>72}")
#         print("-" * 77)


def main():
    import datetime
    db = "expense.sqlite3"
    sql_create_table_expense_tracker = """
            CREATE TABLE IF NOT EXISTS expense_tracker (
                id integer PRIMARY KEY,
                name text NOT NULL,
                amount real NOT NUll,
                date text NOT NULL,
                type_ex text NOT NULL
            );
        """
    cnx = CI4003_expense_connect_database.create_con(db)
    CI4003_expense_connect_database.create_table(cnx, sql_create_table_expense_tracker)
    print(f"Welcome to expense tracker program".title())
    global expense_type, x_1, x_2, halo
    option = -1
    calculate = CalExpense()
    while option != 0:
        print(f"1. Add Expense\n2. Show Expense\n3. Edit Expense\n4. Remove Expense\n0. Exit")
        option = int(input("Please input an options: "))
        if option == 1:
            print("Enter category name of expense")
            expense_type = input("").title()
            x_1 = input(f"Enter the name of {expense_type.lower()}: ").title()
            x_2 = float(input("Please input the price: "))
            x_3 = input("Please input a date in YYYY/MM/DD format: ")
            iformat = "%Y/%m/%d"
            # datetime = datetime.datetime.strptime(x_3, iformat)
            datetime.datetime.strptime(x_3, iformat)
            # print(x_3)
            # print(datetime)
            # print(type(datetime.date()))
            expense = ExpenseTK(x_1, x_2, x_3, expense_type)
            # print(expense)
            qp = [expense.name, expense.amount, expense.date, expense.type_ex]
            calculate.add(qp)
            print("Added Successfully")
            # calculate.items()
            CI4003_expense_connect_database.add_expense(cnx, x_1, x_2, x_3, expense_type)  # add data into database
            # halo = calculate.total()
            # print(halo)

        elif option == 2:
            # print(type(list_expense(cnx)))
            # halo = calculate.total()
            # display_expense(calculate.expenseTK, halo)
            CI4003_expense_connect_database.list_expense(cnx)
            print("To Continue Press 'Y' Or '0' To Quit: ")
            var = input("")
            # print(var)
            if var == "0":
                print("Exiting the program")
                break
            # elif var in ["1", "2", "3"]:
            #     break
            elif var in ["Y", "y"]:
                continue
            else:
                print("You did the wrong command!!\nBye!!!")
                break

        elif option == 3:
            # print("Please enter name to edit amount: ")
            na = str(input("Please enter name to edit amount: ").title())
            da = str(input("Please input date to edit amount: "))
            am = float(input("Input amount: "))
            # print(na, da, am)
            # calculate.update(na, da, am)
            CI4003_expense_connect_database.update_expense(cnx, na, da, am)
            # TODO - use try and exception when data not match in database
            print("Updated")
            print("To Continue Press 'Y' Or '0' To Quit: ")
            var = input("")
            # print(var)
            if var == "0":
                print("Exiting the program")
                break
            # elif var in ["1", "2", "3"]:
            #     break
            elif var in ["Y", "y"]:
                continue
            else:
                print("You did the wrong command!!\nBye!!!")
                break

        elif option == 4:
            na = str(input("Please enter name to remove: ").title())
            da = str(input("Please input date to remove: "))
            CI4003_expense_connect_database.delete_expense(cnx, na, da)
            # TODO - use try and exception when data not match in database
            print("Deleted")
            print("To Continue Press 'Y' Or '0' To Quit: ")
            var = input("")
            # print(var)
            if var == "0":
                print("Exiting the program")
                break
            # elif var in ["1", "2", "3"]:
            #     break
            elif var in ["Y", "y"]:
                continue
            else:
                print("You did the wrong command!!\nBye!!!")
                break

        elif option == 0:
            print("Exiting the program")
            break


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
