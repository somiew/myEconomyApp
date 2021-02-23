# python 3.8.7
import sqlite3


# ----------
# WARNING, script is stupid because when I call this from another script, 
# I need to have access to the cursor without having started the rest of the script.
# Probable solvable in a better way somehow...
# ----------


# Function that creates table
def create_table(person):
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS ' + person + '(incomeCat TEXT, income REAL, expenseCat TEXT, expense REAL, newSalaryDate TEXT)')

    c.close()
    conn.close()

# Functions that add to tables in different ways
def add_income(person, incomeCategory, income):
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()

    c.execute('INSERT INTO ' + person + '(incomeCat, income) VALUES (?, ?)',
    (incomeCategory, income))
    conn.commit()

    c.close()
    conn.close()

def add_expense(person, expenseCategory, expense):
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()

    c.execute('INSERT INTO ' + person + '(expenseCat, expense) VALUES (?, ?)',
    (expenseCategory, expense))
    conn.commit()

    c.close()
    conn.close()


def add_newSalaryDate(person, newSalaryDate):
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()

    c.execute('INSERT INTO ' + person + '(newSalaryDate) VALUES (?)',
    (newSalaryDate,))
    conn.commit()

    c.close()
    conn.close()

# Functions that read tables 
def read_income(person):
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()

    totalIncome = 0
    c.execute('SELECT income FROM ' + person + ' WHERE income IS NOT NULL')
    for row in c.fetchall():
        totalIncome += row[0]

    c.close()
    conn.close()

    return totalIncome

def read_expense(person):
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()

    totalExpense = 0
    c.execute('SELECT expense FROM ' + person + ' WHERE expense IS NOT NULL')
    for row in c.fetchall():
        totalExpense += row[0]

    c.close()
    conn.close()

    return totalExpense

def read_newSalaryDate(person):
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()

    # fetches the lastest date that has been added
    # there's probably a more effective way to do this without going through every entry...
    date = '1970-01-01'
    c.execute('SELECT newSalaryDate FROM ' + person + ' WHERE newSalaryDate IS NOT NULL')
    for row in c.fetchall():
        date = row
    
    c.close()
    conn.close()

    return date

# Read line from file
def read_line(document, line):
    with open(document, "r") as f:
        lines = f.readlines()
        return lines[line].strip()

# Write line to file
def write_line(document, message):
    with open(document, "w") as f:
        f.write(message)


# not sure I'm doing this correct, but I think so?
# in theory this isn't running when I'm using economy.py in other scripts?
if __name__ == "__main__":
    person = read_line('person.txt', 0)
    incomeCat = 'Lön'
    income = 10000
    expenseCat = 'Hyra'
    expense = 4000
    newSalaryDate = '2021-02-25'

    create_table(person)
    #add_income(person, incomeCat, income)
    #add_expense(person, expenseCat, expense)
    #add_newSalaryDate(person, newSalaryDate)
    inc = read_income(person)
    exp = read_expense(person)
    newdate = read_newSalaryDate(person)
    print(person, int(inc), int(exp), newdate[0])
