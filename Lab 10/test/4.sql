--ONLY WORKS FOR LAB 10 NOT LAB 9 TPCH
drop trigger if exists t4;
create trigger t4 
after insert on lineitem
begin
	update orders
	set o_orderpriority = 'high'
	where o_orderkey = new.l_orderkey;
end;

select count(*)
from orders
where  o_orderdate like "1996-11-%"
and o_orderpriority like "high";
