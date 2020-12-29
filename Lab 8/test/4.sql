.eqp on

.expert
select
    avg(julianday(l_shipdate) - julianday(l_commitdate))
from lineitem
where l_shipdate >= l_commitdate;
