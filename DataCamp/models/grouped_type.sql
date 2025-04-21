WITH  grouped_type as (SELECT TYPE,
               AVG(BENEFIT_PER_ORDER),
               AVG(SALES_PER_CUSTOMER)

             FROM
              {{source('db','supply')}}
             group by TYPE
)

select 
  *
  from grouped_type

