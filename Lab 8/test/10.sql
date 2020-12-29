.eqp on

.expert
CREATE INDEX orders_idx_o_custkey_o_orderkey ON orders(o_custkey, o_orderkey);
CREATE INDEX customer_idx_c_nationkey_c_custkey ON customer(c_nationkey, c_custkey);
CREATE INDEX nation_idx_n_regionkey_n_nationkey ON nation(n_regionkey, n_nationkey);
CREATE INDEX region_idx_r_name_r_regionkey ON region(r_name, r_regionkey);
select sum(o_totalprice)
from orders, customer, nation, region
where r_name = 'EUROPE' AND
	r_regionkey = n_regionkey AND
	n_nationkey = c_nationkey AND
	c_custkey = o_custkey AND
	o_orderdate like '1996-__-__';
