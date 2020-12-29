Question One (Correct)
SELECT c_address, c_phone, c_acctbal FROM customer WHERE c_name = "Customer#000000127";
Question Two (Correct)
SELECT MAX(s_acctbal) FROM supplier;
Question Three (Correct)
SELECT l_orderkey, l_partkey, l_suppkey, l_linenumber, l_quantity, l_extendedprice, l_discount, l_tax, l_returnflag, l_linestatus, l_shipdate, l_commitdate, l_receiptdate, l_shipinstruct, l_shipmode, l_comment FROM lineitem WHERE l_returnflag = "R" AND l_receiptdate = "1992-05-30";
Question Four (Correct) 
SELECT AVG(juliANDay(l_shipdate)-juliANDay(l_commitdate)) FROM lineitem WHERE l_shipdate >= l_commitdate;
Question Five (Correct)
SELECT c_mktsegment, MIN(c_acctbal), MAX(c_acctbal), AVG(c_acctbal), SUM(c_acctbal) FROM customer GROUP BY c_mktsegment;
Question Six (Correct)
SELECT DISTINCT nation.n_name FROM nation, customer, orders WHERE customer.c_custkey = orders.o_custkey AND nation.n_nationkey = customer.c_nationkey AND orders.o_orderdate BETWEEN '1995-03-10' AND '1995-03-12' ORDER BY n_name ASC;
Question Seven (Correct)
SELECT l_receiptdate, COUNT(*) FROM lineitem, orders, customer WHERE l_orderkey = o_orderkey AND o_custkey = c_custkey AND c_name = "Customer#000000106" GROUP BY l_receiptdate;
Question Eight (Correct)
SELECT DISTINCT s_name FROM supplier, customer, nation, region WHERE s_nationkey = n_nationkey AND n_nationkey = c_nationkey AND r_regionkey = n_regionkey AND s_acctbal <= '1000' AND r_regionkey = 2 ORDER BY s_name ASC;
Question Nine (Correct)
SELECT n_name, MIN(s_acctbal) FROM nation, supplier WHERE n_nationkey = s_nationkey GROUP BY s_nationkey HAVING COUNT(*) < 3;
Question Ten (Correct)
SELECT SUM(o_totalprice) FROM orders, customer, nation, region WHERE o_custkey = c_custkey AND c_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = 'EUROPE' AND o_orderdate LIKE '1996-%%-%%';
Question Eleven
SELECT c_custkey, COUNT(l_quantity) FROM customer, lineitem, orders WHERE l_discount >= 0.05 AND o_custkey = c_custkey AND l_orderkey = o_orderkey GROUP BY c_custkey HAVING COUNT(l_quantity) >= 70; 
Question Twelve
SELECT r_name, Count(o_orderstatus) FROM region, orders, customer, nation WHERE r_regionkey = n_regionkey AND n_nationkey = c_nationkey AND o_custkey = c_custkey AND o_orderstatus = 'F' GROUP BY r_name ORDER BY r_name;
Question Thirteen
SELECT AVG(c_acctbal) FROM (SELECT c_acctbal, c_mktsegment FROM customer, region, nation WHERE r_name = 'AFRICA' AND r_regionkey = n_regionkey AND n_nationkey = c_nationkey) WHERE c_mktsegment = 'MACHINERY';
Question Fourteen
SELECT count(*) FROM customer, orders, nation WHERE o_orderpriority = '1-URGENT' AND n_name = 'FRANCE' AND n_nationkey = c_nationkey AND c_custkey = o_custkey AND o_orderdate >= '1994-01-01' AND o_orderdate <= '1996-12-31';
Question Fifteen
SELECT substr(o_orderdate, 1, 4), r_name, COUNT(*) FROM orders, nation, supplier, region, lineitem WHERE s_suppkey = l_suppkey AND l_orderkey = o_orderkey AND s_nationkey = n_nationkey AND r_regionkey = n_regionkey AND o_orderpriority = '1-URGENT' GROUP BY substr(o_orderdate, 1, 4), r_name;









