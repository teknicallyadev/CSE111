-- 1.sql
CREATE INDEX customer_idx_c_name ON customer(c_name);
-- 2.sql
CREATE INDEX supplier_idx_s_acctbal ON supplier(s_acctbal DESC);
-- 3.sql
CREATE INDEX lineitem_idx_l_returnflag_l_receiptdate ON lineitem(l_returnflag, l_receiptdate);
-- 4.sql 
-- 5.sql
CREATE INDEX customer_idx_c_mktsegment ON customer(c_mktsegment DESC);
-- 6.sql
CREATE INDEX nation_idx_n_nationkey ON nation(n_nationkey);
CREATE INDEX customer_idx_c_custkey ON customer(c_custkey);
CREATE INDEX orders_idx_o_orderdate ON orders(o_orderdate);
-- 7.sql
--CREATE INDEX lineitem_idx_l_orderkey_l_receiptdate ON lineitem(l_orderkey, l_receiptdate);
CREATE INDEX customer_idx_c_name_c_custkey ON customer(c_name, c_custkey);
-- 8.sql
CREATE INDEX supplier_idx_s_nationkey_s_acctbal ON supplier(s_nationkey, s_acctbal);
CREATE INDEX nation_idx_n_regionkey_n_nationkey ON nation(n_regionkey, n_nationkey);
CREATE INDEX region_idx_r_name_r_regionkey ON region(r_name, r_regionkey);
-- 9.sql
CREATE INDEX supplier_idx_s_nationkey ON supplier(s_nationkey);
CREATE INDEX nation_idx_n_name ON nation(n_name);
-- 10.sql
--CREATE INDEX orders_idx_o_custkey_o_orderkey ON orders(o_custkey, o_orderkey);
CREATE INDEX customer_idx_c_nationkey_c_custkey ON customer(c_nationkey, c_custkey);
--CREATE INDEX nation_idx_n_regionkey_n_nationkey ON nation(n_regionkey, n_nationkey);
--CREATE INDEX region_idx_r_name_r_regionkey ON region(r_name, r_regionkey);
-- 11.sql
CREATE INDEX lineitem_idx_l_orderkey_l_discount ON lineitem(l_orderkey, l_discount);
CREATE INDEX orders_idx_o_custkey ON orders(o_custkey);
-- 12.sql
--CREATE INDEX region_idx_r_regionkey_r_name ON (r_regionkey, r_name);
--CREATE INDEX nation_idx_n_nationkey ON nation(n_nationkey);
--CREATE INDEX customer_idx_c_custkey ON customer(c_custkey);
CREATE INDEX orders_idx_o_orderstatus ON orders(o_orderstatus);
-- 13.sql
--CREATE INDEX nation_idx_n_regionkey_n_nationkey ON nation(n_regionkey, n_nationkey);
--CREATE INDEX region_idx_r_name_r_regionkey ON region(r_name, r_regionkey);
--CREATE INDEX customer_idx_c_mktsegment ON customer(c_mktsegment);
-- 14.sql
--CREATE INDEX customer_idx_c_nationkey_c_custkey ON customer(c_nationkey, c_custkey);
CREATE INDEX nation_idx_n_name_n_nationkey ON nation(n_name, n_nationkey);
CREATE INDEX orders_idx_o_orderpriority_o_custkey ON orders(o_orderpriority, o_custkey);
-- 15.sql
CREATE INDEX orders_idx_o_orderpriority_o_orderkey ON orders(o_orderpriority, o_orderkey);
--CREATE INDEX nation_idx_n_nationkey ON nation(n_nationkey);
CREATE INDEX supplier_idx_s_suppkey ON supplier(s_suppkey);
CREATE INDEX lineitem_idx_l_orderkey_l_receiptdate ON lineitem(l_orderkey, l_receiptdate);
CREATE INDEX region_idx_r_regionkey_r_name ON region(r_regionkey, r_name);
CREATE INDEX orders_idx_o_custkey_o_orderkey ON orders(o_custkey, o_orderkey);