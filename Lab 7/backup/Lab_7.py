import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn


def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    c.execute('''CREATE TABLE warehouse
                (w_warehousekey decimal(9,0) not null,
                w_name char(100) not null,
                w_capacity decimal(6,0) not null,
                w_suppkey decimal(9,0) not null,
                w_nationkey decimal(2,0) not null
                )''')
    _conn.commit()
    print("YOU HAVE MADE THE TABLE")
    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    c.execute('DROP TABLE warehouse')
    _conn.commit()
    print("YOU HAVE DROPPED THE TABLE")
    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    count = 0
    c.execute("SELECT s_suppkey, s_name FROM supplier")
    supplierThings = c.fetchall()
    for i in supplierThings:
        print(i[0])
        c.execute("SELECT n_name, c_nationkey, l_suppkey FROM nation, lineitem, customer, orders WHERE o_orderkey = l_orderkey AND l_suppkey = ? AND c_custkey = o_custkey AND n_nationkey = c_nationkey GROUP BY c_nationkey ORDER BY COUNT(o_orderkey) DESC, n_name ASC LIMIT 2", (i[0],))
        nationName = c.fetchall()
        print(nationName)
        for j in nationName:
            c.execute("SELECT SUM(p_size*2) FROM lineitem, part, orders, customer WHERE l_suppkey = ? AND l_partkey = p_partkey AND c_custkey = o_custkey AND o_orderkey = l_orderkey GROUP BY c_nationkey ORDER BY SUM(p_size*2) DESC LIMIT 1", (j[2],))
            w_capacity = c.fetchone()
            count = count + 1
            print(w_capacity)
            c.execute("INSERT INTO warehouse VALUES(?, ?, ?, ?, ?)", [count, (i[1] + "___" + j[0]), w_capacity[0], i[0], j[1]])

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")
    c.execute("SELECT * FROM warehouse")
    results = c.fetchall()
    with open('output/1.out', 'w') as q1:
        q1.write("%s %s %s %s %s \n" % ("wId", "wName", "wCap", "sId", "nId"))
        for i in results:
            q1.write("%s %s %s %s %s \n" % (i[0], i[1], i[2], i[3], i[4]))

    print("++++++++++++++++++++++++++++++++++")

def Q2(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")
    c.execute("SELECT n_name, COUNT(w_name), SUM(w_capacity) FROM warehouse, nation WHERE w_nationkey = n_nationkey GROUP BY n_name ORDER BY COUNT(w_name) DESC, SUM(w_capacity) DESC, n_name ASC")
    results = c.fetchall()
    with open('output/2.out', 'w') as q2:
        q2.write("%s %s %s \n" % ("nation", "numW", "totCap"))
        for i in results:
            q2.write("%s %s %s \n" % (i[0], i[1], i[2]))
    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")
    data = []
    file = open("./input/3.in", "r")
    data = file.readlines()
    nation = data[0].strip()
    print(nation)
    file.close()

    c.execute("SELECT s_name, n2.n_name, w_name FROM supplier, nation n1, nation n2, warehouse WHERE n1.n_name = ? AND w_nationkey = n1.n_nationkey AND s_nationkey = n2.n_nationkey AND s_suppkey = w_suppkey ORDER BY w_name ASC", (nation,   ))
    results = c.fetchall()
    with open('output/3.out', 'w') as q3:
        q3.write("%s %s %s \n" % ("supplier", "nation", "warehouse"))
        for i in results:
            q3.write("%s %s %s \n" % (i[0], i[1], i[2]))
    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")
    data = []
    file = open("./input/4.in", "r")
    data = file.readlines()
    region = data[0].strip()
    print(region)
    capacity = data[1].strip()
    print(capacity)
    file.close()

    c.execute("SELECT w_name, w_capacity FROM warehouse, nation, region WHERE w_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = ?AND w_capacity > ? ORDER BY w_capacity DESC", (region, capacity,))
    results = c.fetchall()
    with open('output/4.out', 'w') as q4:
        q4.write("%s %s \n" % ("warehouse", "capacity"))
        for i in results:
            q4.write("%s %s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")
    data = []
    file = open("./input/5.in", "r")
    data = file.readlines()
    nation = data[0].strip()
    print(nation)
    file.close()

    c.execute("SELECT r_name, CAST(total(w_capacity) AS INT) FROM region, nation LEFT JOIN (SELECT * FROM warehouse, supplier, nation WHERE n_name = ? AND s_suppkey = w_suppkey AND n_nationkey = s_nationkey) ON nation.n_nationkey = w_nationkey WHERE r_regionkey = nation.n_regionkey GROUP BY r_name",(nation,))
    results = c.fetchall()
    with open('output/5.out', 'w') as q5:
        q5.write("%s %s \n" % ("region", "capacity"))
        for i in results:
            q5.write("%s %s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"data/tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTable(conn)

        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
