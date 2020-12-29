--ONLY WORKS FOR LAB 10 NOT LAB 9
drop trigger if exists t3;
create trigger t3 
after update on customer
begin
    update customer
    set c_comment = 'Positive balance'
    where c_custkey = new.c_custkey
    and new.c_acctbal > 0
    and old.c_acctbal < 0;
end;

update customer
set c_acctbal = 100
where c_nationkey = 19;

select count(*)
from customer, region, nation
where c_nationkey = n_nationkey
    and n_regionkey = r_regionkey
    and r_name like "EUROPE"
    and c_acctbal < 0;