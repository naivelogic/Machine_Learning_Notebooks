# Basics on SQLite
## Statistics and Machine Learning in Python

import pandas as pd
import sqlite3
import tempfile, os.path

tempdir = tempfile.gettempdir()

db_filename = os.path.join(tempdir, "users.db")

conn = sqlite3.connect(db_filename)     # connect

# creating tables with pandas
url = 'https://raw.github.com/neurospin/pystatsml/master/datasets/salary_table.csv'
salary = pd.read_csv(url)

salary.to_sql("salary", conn, if_exists="replace")

# Push Modifications
cur = conn.cursor()
values = (100, 14000, 5, 'Bachelor', 'N')
cur.execute("insert into salary values (?, ?, ?, ?, ?)", values)
conn.commit()

# Reading results into a pandas DataFrame
salary_sql = pd.read_sql_query("select * from salary;", conn)
print(salary_sql.head())

pd.read_sql_query("select * from salary;", conn).tail()
pd.read_sql_query("select * from salary where salary>25000;", conn)
pd.read_sql_query("select * from salary where experience=16;", conn)
pd.read_sql_query('select * from salary where education="Master";', conn)

conn.close()

df = salary

# Boxplot
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x="education", y="salary", hue="management", data=salary)
plt.show()

sns.boxplot(x="management", y="salary", hue="education", data=salary)
plt.show()

sns.stripplot(x="management", y="salary", hue="education", data=salary, jitter=True, dodge=True, linewidth=1)   # Jitter and split options separate datapoints according to group"
plt.show()

# Density Plot with one figure containing multiple axis
## set up the matplotlib figure 3x1 axis
f, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

i = 0
for edu, d in salary.groupby(['education']):
    sns.distplot(d.salary[d.management == "Y"], color = "b", bins = 10, label = "Manager", ax=axes[i])
    sns.distplot(d.salary[d.management == "N"], color="r", bins = 10, 
    label="Employee", ax=axes[i])
    axes[i].set_title(edu)
    axes[i].set_ylabel('Density')
    i += 1
plt.show()

g = sns.PairGrid(salary, hue="management")
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend()
plt.show()
