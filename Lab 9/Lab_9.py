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


def create_View1(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Create V1")
    # Create a view V1(c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, c_nation, c_region)
    # that appends the country and region name to every customer
    c.execute('''DROP VIEW V1''')
    c.execute('''
        CREATE VIEW V1(c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, c_nation, c_region) AS 
        SELECT c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, n_name AS c_nation, r_name AS c_region 
        FROM customer, region, nation
        WHERE c_nationkey = n_nationkey
        AND n_regionkey = r_regionkey;
        ''')
    print("++++++++++++++++++++++++++++++++++")


def create_View2(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Create V2")
    c.execute('''DROP VIEW V2''')
    c.execute('''
        CREATE VIEW V2(s_suppkey, s_name, s_address, s_phone, s_acctbal, s_comment, s_nation, s_region) AS 
        SELECT s_suppkey, s_name, s_address, s_phone, s_acctbal, s_comment, n_name AS s_nation, r_name AS s_region 
        FROM supplier, region, nation
        WHERE s_nationkey = n_nationkey
        AND n_regionkey = r_regionkey 
        ''')
    print("++++++++++++++++++++++++++++++++++")


def create_View5(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Create V5")
    c.execute('''DROP VIEW V5''')
    c.execute('''
        CREATE VIEW V5(o_orderkey, o_custkey, o_orderstatus, o_totalprice, o_orderyear, o_orderpriority, o_clerk,
        o_shippriority, o_comment) AS 
        SELECT o_orderkey, o_custkey, o_orderstatus, o_totalprice, strftime('%Y', o_orderdate) AS o_orderyear, o_orderpriority, o_clerk,
        o_shippriority, o_comment 
        FROM orders
        ''')
    print("++++++++++++++++++++++++++++++++++")


def create_View10(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Create V10")
    c.execute('''DROP VIEW V10''')
    c.execute('''
        CREATE VIEW V10(p_type, avg_discount) AS 
        SELECT p_type, AVG(l_discount) AS avg_discount 
        FROM part, lineitem
        WHERE p_partkey = l_partkey
        GROUP BY p_type
        ''')
    print("++++++++++++++++++++++++++++++++++")


def create_View151(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Create V151")
    c.execute('''DROP VIEW V151''')
    c.execute('''
        CREATE VIEW V151(c_custkey, c_name, c_nationkey, c_acctbal) AS
        SELECT c_custkey, c_name, c_nationkey, c_acctbal
        FROM customer
        WHERE c_acctbal < 0
        GROUP BY c_name
        ''')
    print("++++++++++++++++++++++++++++++++++")


def create_View152(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Create V152")
    c.execute('''DROP VIEW V152''')
    c.execute('''
        CREATE VIEW V152(s_suppkey, s_name, s_nationkey, s_acctbal) AS
        SELECT s_suppkey, s_name, s_nationkey, s_acctbal
        FROM supplier
        WHERE s_acctbal < 0
        GROUP BY s_name
        ''')
    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")
    # select c_name, sum(o_totalprice)
    # from orders, customer, nation
    # where o_custkey = c_custkey and
    # n_nationkey = c_nationkey and
    # n_name = 'RUSSIA' AND
    # o_orderdate like '1996-__-__'
    # group by c_name;
    # USES VIEW V1
    c.execute('''
        select c_name, ROUND(sum(o_totalprice),2)
        from V1, orders
        where o_custkey = c_custkey 
        and c_nation = 'RUSSIA' 
        and o_orderdate like '1996-__-__'
        group by c_name
        ''')
    results = c.fetchall()
    with open('output/1.out', 'w') as q1:
        for i in results:
            q1.write("%s|%s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")
    # select n_name, count(*)
    # from supplier, nation
    # where s_nationkey = n_nationkey
    # group by n_name;
    c.execute('''
        select s_nation, count(*)
        from V2
        group by s_nation
        ''')
    results = c.fetchall()
    with open('output/2.out', 'w') as q2:
        for i in results:
            q2.write("%s|%s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")
    # select n_name, count(*)
    # from orders, nation, customer, region
    # where c_custkey = o_custkey and
	#    c_nationkey = n_nationkey AND
	#    n_regionkey = r_regionkey AND
	#    r_name = 'ASIA'
    # group by n_name;
    c.execute('''
        select c_nation, count(*)
        from V1, orders
        where c_custkey = o_custkey
        AND c_region = 'ASIA'
        group by c_nation
        ''')
    results = c.fetchall()
    with open('output/3.out', 'w') as q3:
        for i in results:
            q3.write("%s|%s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")
    # select s_name, count(*)
    # from partsupp, supplier, nation, part
    # where p_partkey = ps_partkey
    #	and p_size < 30 
    #	and ps_suppkey = s_suppkey 
    #	and s_nationkey = n_nationkey 
    #	and n_name = 'CHINA'
    # group by s_name;
    c.execute('''
        select s_name, count(*)
        from V2, partsupp, part
        where p_partkey = ps_partkey 
    	    and p_size < 30 
    	    and ps_suppkey = s_suppkey 
    	    and s_nation = 'CHINA' 
        group by s_name
        ''')
    results = c.fetchall()
    with open('output/4.out', 'w') as q4:
        for i in results:
            q4.write("%s|%s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")

def Q5(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")
    # select count(*)
    # from orders, customer, nation
    # where o_custkey = c_custkey 
    #	and c_nationkey = n_nationkey
    #  	and n_name = 'PERU' 
    #	and o_orderdate like '1996-__-__';
    c.execute('''
        select count(*)
        from V1, V5
        where o_custkey = c_custkey
	    and c_nation = 'PERU'
	    and o_orderyear like '1996' 
        ''')
    results = c.fetchall()
    with open('output/5.out', 'w') as q5:
        for i in results:
            q5.write("%s \n" % (i[0]))
    print("++++++++++++++++++++++++++++++++++")


def Q6(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")
    # select s_name, o_orderpriority, count(*)
    # from partsupp, orders, lineitem, supplier, region, nation
    # where ps_partkey = l_partkey 
	# and ps_suppkey = l_suppkey
	# and l_orderkey = o_orderkey
	# and ps_suppkey = s_suppkey
	# and s_nationkey = n_nationkey
	# and n_regionkey = r_regionkey
	# and r_name = 'AMERICA'
    # group by s_name, o_orderpriority;
    c.execute('''
        select s_name, o_orderpriority, count(*)
        from partsupp, lineitem, supplier, region, nation, V5
        where ps_partkey = l_partkey 
	    and ps_suppkey = l_suppkey
	    and l_orderkey = o_orderkey
	    and ps_suppkey = s_suppkey
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
	    and r_name = 'AMERICA'
        group by s_name, o_orderpriority;
        ''')
    results = c.fetchall()
    with open('output/6.out', 'w') as q6:
        for i in results:
            q6.write("%s|%s|%s \n" % (i[0], i[1], i[2]))
    print("++++++++++++++++++++++++++++++++++")


def Q7(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")
    # select n_name, o_orderstatus, count(*)
    # from orders, customer, nation, region
    # where o_custkey = c_custkey 
	# and c_nationkey = n_nationkey
	# and n_regionkey = r_regionkey
	# and r_name = 'EUROPE'
    # group by n_name, o_orderstatus;
    c.execute('''
        select c_nation, o_orderstatus, count(*)
        from V1, V5
        where o_custkey = c_custkey
	    and c_region = 'EUROPE'
        group by c_nation, o_orderstatus
    ''')
    results = c.fetchall()
    with open('output/7.out', 'w') as q7:
        for i in results:
            q7.write("%s|%s|%s \n" % (i[0], i[1], i[2]))
    print("++++++++++++++++++++++++++++++++++")


def Q8(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")
    # select n_name, count(distinct o_orderkey) as tot_orders
    # from orders, nation, supplier, lineitem
    # where o_orderdate like '1994%'
	# and o_orderstatus = 'F'
	# and o_orderkey = l_orderkey 
	# and l_suppkey = s_suppkey
	# and s_nationkey = n_nationkey
    # group by n_name
    # having tot_orders > 300;
    c.execute('''
        select s_nation, count(distinct o_orderkey) as tot_orders
        from V2, V5, lineitem
        where o_orderyear like '1994%'
	    and o_orderstatus = 'F'
	    and o_orderkey = l_orderkey 
	    and l_suppkey = s_suppkey
        group by s_nation
        having tot_orders > 300;
        ''')
    results = c.fetchall()
    with open('output/8.out', 'w') as q8:
        for i in results:
            q8.write("%s|%s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")


def Q9(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")
    # select count(DISTINCT o_clerk)
    # from orders, supplier, nation, lineitem
    # where o_orderkey = l_orderkey 
	# and l_suppkey = s_suppkey 
	# and s_nationkey = n_nationkey 
	# and n_name = 'CANADA';
    c.execute('''
        select count(DISTINCT o_clerk)
        from lineitem, V2, V5
        where o_orderkey = l_orderkey 
	    and l_suppkey = s_suppkey 
	    and s_nation = 'CANADA';
        ''')
    results = c.fetchall()
    with open('output/9.out', 'w') as q9:
        for i in results:
            q9.write("%s \n" % (i[0]))
    print("++++++++++++++++++++++++++++++++++")


def Q10(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")
    c.execute('''
        select p_type, ROUND(avg_discount, 16)
        from V10
        where p_type like '%PROMO%'
        ''')
    results = c.fetchall()
    with open('output/10.out', 'w') as q10:
        for i in results:
            q10.write("%s|%s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")
    c.execute('''
        select s_nation, s_name, s_acctbal
        from V2 V2_1
        where s_acctbal = 
        (select max(s_acctbal)
        from V2 V2_2
        where V2_1.s_nation = V2_2.s_nation)
        ORDER BY s_nation ASC
        ''')
    results = c.fetchall()
    with open('output/11.out', 'w') as q11:
        for i in results:
            q11.write("%s|%s|%s \n" % (i[0], i[1], i[2]))
    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")
    c.execute('''
        select s_nation, ROUND(avg(s_acctbal), 11)
        from V2
        group by s_nation
        ''')
    results = c.fetchall()
    with open('output/12.out', 'w') as q12:
        for i in results:
            q12.write("%s|%s \n" % (i[0], i[1]))
    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")
    c.execute('''
        select count(*)
        from orders, lineitem, customer
        where o_orderkey = l_orderkey
        and o_custkey = c_custkey
        and l_suppkey in (
        select s_suppkey
        from V2
        where s_region = 'ASIA')
        and c_custkey in (
        select c_custkey
        from V1
        where c_nation = 'ARGENTINA')
        ''')
    results = c.fetchall()
    with open('output/13.out', 'w') as q13:
        for i in results:
            q13.write("%s \n" % (i[0]))
    print("++++++++++++++++++++++++++++++++++")


def Q14(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")
    c.execute('''
        select custRegion, suppRegion, count(*) 
        from orders
        join
        (select o_orderkey as custOrder, c_region as custRegion
        from orders, V1
        where o_custkey = c_custkey
        ) on o_orderkey = custOrder
        join
        (select l_orderkey as suppOrder, s_region as suppRegion
        from lineitem, V2
        where l_suppkey = s_suppkey
        ) on o_orderkey = suppOrder
        group by custRegion, suppRegion;
        ''')
    results = c.fetchall()
    with open('output/14.out', 'w') as q14:
        for i in results:
            q14.write("%s|%s|%s \n" % (i[0],i[1],i[2]))
    print("++++++++++++++++++++++++++++++++++")


def Q15(_conn):
    c = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")
    c.execute('''
        select count(DISTINCT o_orderkey)
        from orders, lineitem
        where o_orderkey = l_orderkey
        and o_custkey in
        (select c_custkey
        from V151
        where c_acctbal < 0)
        and l_suppkey in
        (select s_suppkey
        from V152
        where s_acctbal < 0);
        ''')
    results = c.fetchall()
    with open('output/15.out', 'w') as q15:
        for i in results:
            q15.write("%s \n" % (i[0]))
    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"data/tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        create_View1(conn)
        Q1(conn)

        create_View2(conn)
        Q2(conn)

        Q3(conn)
        Q4(conn)

        create_View5(conn)
        Q5(conn)

        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)

        create_View10(conn)
        Q10(conn)

        Q11(conn)
        Q12(conn)
        Q13(conn)
        Q14(conn)

        create_View151(conn)
        create_View152(conn)
        Q15(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
