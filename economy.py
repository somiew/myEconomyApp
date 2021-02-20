# python 3.8.7
import sqlite3

person = 'SamuelLindsköld'
incomeCat = 'Lön'
income = 18000
expenseCat = 'Hyra'
expense = 4000
newSalaryDate = '2021-02-28'


conn = sqlite3.connect('economy.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS ' + person + '(incomeCat TEXT, income REAL, expenseCat TEXT, expense REAL, newSalaryDate TEXT)')

def add_income(incomeCategory, income):
    c.execute('INSERT INTO ' + person + '(incomeCat, income, expenseCat, expense, newSalaryDate) VALUES (?, ?, ?, ?, ?)',
    (incomeCat, income, expenseCat, expense, newSalaryDate))
    conn.commit()

def read_from_db():
    money = 0
    c.execute('SELECT income FROM ' + person)
    for row in c.fetchall():
        money += row[0]
    print(money)


create_table()
add_income(incomeCat, income)
read_from_db()

c.close()
conn.close()