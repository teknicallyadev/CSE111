.eqp on
.expert
CREATE INDEX orders_idx_o_orderpriority_o_orderkey ON orders(o_orderpriority, o_orderkey);
CREATE INDEX nation_idx_n_nationkey ON nation(n_nationkey);
CREATE INDEX supplier_idx_s_suppkey ON supplier(s_suppkey);
CREATE INDEX lineitem_idx_l_orderkey_l_receiptdate ON lineitem(l_orderkey, l_receiptdate);
CREATE INDEX region_idx_r_regionkey_r_name ON region(r_regionkey, r_name);
select substr(o_orderdate, 1, 4) as year,
    r_name, count(*)
from orders, lineitem, supplier, nation, region
where o_orderpriority = '1-URGENT' AND
    o_orderkey = l_orderkey AND
    l_suppkey = s_suppkey AND
    s_nationkey = n_nationkey AND
    n_regionkey = r_regionkey
group by year, r_name
order by year, r_name;
