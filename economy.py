# python 3.8.7
import sqlite3

person = 'SamuelLindsköld'
incomeCat = 'Lön'
income = 10000
expenseCat = 'Hyra'
expense = 4000
newSalaryDate = '2021-02-25'

conn = sqlite3.connect('economy.db')
c = conn.cursor()


# Function that creates table
def create_table(person):
    c.execute('CREATE TABLE IF NOT EXISTS ' + person + '(incomeCat TEXT, income REAL, expenseCat TEXT, expense REAL, newSalaryDate TEXT)')

# Functions that add to tables in different ways
def add_income(person, incomeCategory, income):
    c.execute('INSERT INTO ' + person + '(incomeCat, income) VALUES (?, ?)',
    (incomeCat, income))
    conn.commit()

def add_expense(person, expenseCategory, expense):
    c.execute('INSERT INTO ' + person + '(expenseCat, expense) VALUES (?, ?)',
    (expenseCat, expense))
    conn.commit()

def add_newSalaryDate(person, newSalaryDate):
    c.execute('INSERT INTO ' + person + '(newSalaryDate) VALUES (?)',
    (newSalaryDate,))
    conn.commit()

# Functions that read tables 
def read_income(person):
    totalIncome = 0
    c.execute('SELECT income FROM ' + person + ' WHERE income IS NOT NULL')
    for row in c.fetchall():
        totalIncome += row[0]
    return totalIncome

def read_expense(person):
    totalExpense = 0
    c.execute('SELECT expense FROM ' + person + ' WHERE expense IS NOT NULL')
    for row in c.fetchall():
        totalExpense += row[0]
    return totalExpense

def read_newSalaryDate(person):
    # fetches the lastest date that has been added
    # there's probably a more effective way to do this without going through every entry...
    date = '1970-01-01'
    c.execute('SELECT newSalaryDate FROM ' + person + ' WHERE newSalaryDate IS NOT NULL')
    for row in c.fetchall():
        date = row
    return date


# not sure I'm doing this correct, but I think so?
# in theory this isn't running when I'm using economy.py in other scripts?
if __name__ == "__main__":
    create_table(person)
    #add_income(person, incomeCat, income)
    #add_expense(person, expenseCat, expense)
    #add_newSalaryDate(person, newSalaryDate)
    inc = read_income(person)
    exp = read_expense(person)
    newdate = read_newSalaryDate(person)
    print(int(inc), int(exp), newdate[0])

c.close()
conn.close()