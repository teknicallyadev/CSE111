-- SQLite

--1
select c_name, sum(o_totalprice)
from orders, customer, nation
where o_custkey = c_custkey and
	n_nationkey = c_nationkey and
	n_name = 'RUSSIA' AND
	o_orderdate like '1996-__-__'
group by c_name;

--2
select n_name, count(*)
from supplier, nation
where s_nationkey = n_nationkey
group by n_name;

--3
select n_name, count(*)
from orders, nation, customer, region
where c_custkey = o_custkey and
	c_nationkey = n_nationkey AND
	n_regionkey = r_regionkey AND
	r_name = 'ASIA'
group by n_name;

--4
select s_name, count(*)
from partsupp, supplier, nation, part
where p_partkey = ps_partkey
	and p_size < 30 
	and ps_suppkey = s_suppkey 
	and s_nationkey = n_nationkey 
	and n_name = 'CHINA'
group by s_name;

--5
select count(*)
from orders, customer, nation
where o_custkey = c_custkey 
	and c_nationkey = n_nationkey
	and n_name = 'PERU' 
	and o_orderdate like '1996-__-__';

--6
select s_name, o_orderpriority, count(*)
from partsupp, orders, lineitem, supplier, region, nation
where ps_partkey = l_partkey 
	and ps_suppkey = l_suppkey
	and l_orderkey = o_orderkey
	and ps_suppkey = s_suppkey
	and s_nationkey = n_nationkey
	and n_regionkey = r_regionkey
	and r_name = 'AMERICA'
group by s_name, o_orderpriority;

--7
select n_name, o_orderstatus, count(*)
from orders, customer, nation, region
where o_custkey = c_custkey 
	and c_nationkey = n_nationkey
	and n_regionkey = r_regionkey
	and r_name = 'EUROPE'
group by n_name, o_orderstatus;

--8
select n_name, count(distinct o_orderkey) as tot_orders
from orders, nation, supplier, lineitem
where o_orderdate like '1994%'
	and o_orderstatus = 'F'
	and o_orderkey = l_orderkey 
	and l_suppkey = s_suppkey
	and s_nationkey = n_nationkey
group by n_name
having tot_orders > 300;

--9
select count(DISTINCT o_clerk)
from orders, supplier, nation, lineitem
where o_orderkey = l_orderkey 
	and l_suppkey = s_suppkey 
	and s_nationkey = n_nationkey 
	and n_name = 'CANADA';

--10
select p_type, avg(l_discount)
from lineitem, part
where l_partkey = p_partkey
	and p_type like '%PROMO%'
group by p_type;

--11
select n_name, s_name, s_acctbal
from supplier s, nation n
where s_nationkey = n_nationkey
	and s_acctbal = 
		(select max(s_acctbal)
		from supplier s1
		where s.s_nationkey = s1.s_nationkey
		);

--12
select n_name, avg(s_acctbal)
from supplier, nation
where s_nationkey = n_nationkey
group by n_name;

--13
select count(*)
from orders, lineitem, customer
where o_orderkey = l_orderkey
	and o_custkey = c_custkey
	and l_suppkey in (
		select s_suppkey
		from supplier, nation, region
		where s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA'
		)
	and c_custkey in (
		select c_custkey
		from customer, nation
		where c_nationkey = n_nationkey
			and n_name = 'ARGENTINA'
		);

--14
select custRegion, suppRegion, count(*) as no
from
	orders
	join
	(select o_orderkey as custOrder, r_name as custRegion
	from orders, nation, region, customer
	where o_custkey = c_custkey
		and c_nationkey = n_nationkey
		and n_regionkey = r_regionkey
	) on o_orderkey = custOrder
	join
	(select l_orderkey as suppOrder, r_name as suppRegion
	from lineitem, region, nation, supplier
	where l_suppkey = s_suppkey
		and s_nationkey = n_nationkey
		and n_regionkey = r_regionkey
	) on o_orderkey = suppOrder
group by custRegion, suppRegion;

--15
select count(DISTINCT o_orderkey)
from orders, lineitem
where o_orderkey = l_orderkey
	and o_custkey in
		(select c_custkey
		from customer
		where c_acctbal < 0)
	and l_suppkey in
		(select s_suppkey
		from supplier
		where s_acctbal < 0);
