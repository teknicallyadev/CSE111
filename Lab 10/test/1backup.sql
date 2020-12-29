drop trigger if exists t1;
create trigger t1
after insert on orders
begin
    update orders
    set o_orderdate = '2020-12-01'
    where o_orderkey = new.o_orderkey;
end;

insert into orders(o_orderkey, o_custkey, o_orderstatus, o_totalprice, o_orderdate, o_orderpriority, o_clerk, o_shippriority, o_comment) 
select *
from orders
where o_orderdate LIKE '1995-11-%%'
group by o_orderdate;

select count(DISTINCT o_orderkey)
from orders
where o_orderdate LIKE '%2020-%-%';