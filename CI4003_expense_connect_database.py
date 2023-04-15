# @Name: Ravit Anuvongnukroh
# @id: 6420421008

import sqlite3 # import sqlite 
from sqlite3 import Error


def create_con(db):
    cnx = None
    try:
        cnx = sqlite3.connect(db)
    except Error as e:
        print(e)
    return cnx


def create_table(cnx, sql):
    try:
        c = cnx.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def add_expense(cnx, name, amount, date, type_ex):
    sql = """
        INSERT INTO expense_tracker(name, amount, date, type_ex)
        VALUES (?, ?, ?, ?)
    """
    params = (name, amount, date, type_ex)
    try:
        c = cnx.cursor()
        c.execute(sql, params)
        cnx.commit()
    except Error as e:
        print(e)

    return c.lastrowid


def update_expense(cnx, name, date, amount):
    sql = """
        UPDATE expense_tracker
        SET amount = (?)
        WHERE name = (?)
        AND  date  = (?)
    """
    params = (amount, name, date)
    try:
        c = cnx.cursor()
        c.execute(sql, params)
        cnx.commit()
    except Error as e:
        print(e)


def delete_expense(cnx, name, date):
    sql = """
        DELETE FROM expense_tracker
        WHERE name = ?
        AND  date = ?
    """
    params = (name, date)
    try:
        c = cnx.cursor()
        c.execute(sql, params)
        cnx.commit()
    except Error as e:
        print(e)


def list_expense(cnx):
    sql = """
        SELECT * from expense_tracker
    """
    try:
        c = cnx.cursor()
        c.execute(sql)
        expense = c.fetchall()
        print("-" * 77)
        print(f"{'No.':12}{'Goods Or Services':>16}{'Category':>16}{'Dates':>16}{'Amounts':>16}")
        print("-" * 77)
        total = 0
        for item in expense:
            print(f"{item[0]}{item[1]:>28}{item[4]:>16}{item[3]:>16}{item[2]:>16}")
            total += item[2]
            # print(total)
        print("-" * 77)
        print(f"{'TOTAL'}{total:>72}")
        print("-" * 77)
    except Error as e:
        print(e)


def main():
    pass


if __name__ == "__main__":
    main()
