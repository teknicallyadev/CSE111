--WORKS FOR LAB 10 NOT LAB 9 TPCH
drop trigger if exists t5;
create trigger t5 
after delete on part
begin
	delete from lineitem where l_partkey = old.p_partkey;
	delete from partsupp where ps_partkey = old.p_partkey;
end;

select n_name, count(p_partkey)
from nation, part, region, supplier, partsupp
where s_nationkey = n_nationkey
and n_regionkey = r_regionkey
and r_name = "EUROPE"
and s_suppkey = ps_suppkey
and ps_partkey = p_partkey
group by n_name
order by n_name asc;