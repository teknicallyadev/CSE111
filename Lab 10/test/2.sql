drop trigger if exists t2;
create trigger t2 
after update on customer
begin
    update customer
    set c_comment = 'Negative balance!!!'
    where c_custkey = new.c_custkey
    and new.c_acctbal < 0
    and old.c_acctbal > 0;
end;

update customer
set c_acctbal = -100
where c_nationkey = 6;


select COUNT(*)
from customer, nation
where c_acctbal < 0
and c_nationkey = n_nationkey
and n_name LIKE "FRANCE";