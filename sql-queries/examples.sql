with companies as (
    Select
        b.name,
        a.date,
        max(a.rk_id) as max_rk_id
    From 
        payment_date a
        join users b on b.id = a.user_id
        join advertising_companies c on c.id = a.rk_id
    Where 1 = 1
        and owner_id is not null -- признак компании
        and c.is_main = 1
        and a.sum > 0
    Group by
        b.name,
        a.date
)

Select
    bb.name,
    sum(aa.sum) as budget
From advertising_companies aa
join companies bb on bb.max_rk_id = aa.rk_id
Group by bb.name
Order by 1 asc;



with WaitTimes as (
  Select
     strftime('%Y-%m-%d', l2.verdict_time) as field_date,
     julianday(l2.verdict_time) - julianday(l1.verdict_time) as wait_time
  From logs as l1
  inner join logs as l2
    on l1.campaign_id = l2.campaign_id
  Where 1 = 1
        and l1.verdict = 'No' and l2.verdict = 'Yes'
        and l1.verdict_time < l2.verdict_time
        and not exists (
      Select
        1
      From logs as l3
      Where 1 = 1
            and l3.campaign_id = l1.campaign_id
            and l3.verdict = 'No'
            and l1.verdict_time < l3.verdict_time
            and l3.verdict_time < l2.verdict_time
    )
)
Select
   field_date,
   round(avg(wait_time) * 24 * 60) as avg_wait_time
From WaitTimes
Group by 1
Order by 1;



with recursive genre_hierarchy as (
    -- связи треков с жанрами
    Select
        tg.track_id,
        tg.genre_id,
        g.name as genre_name,
        g.parent_genre_id
    From track_genre tg
    join genre g on tg.genre_id = g.id
    
    union all
    
    -- рекурсивный подъём по иерархии вверх
    Select
        gh.track_id,
        g.id as genre_id,
        g.name as genre_name,
        g.parent_genre_id
    From genre_hierarchy gh
    join genre g on gh.parent_genre_id = g.id
)
Select distinct
    gh.track_id,
    t.name AS track_name,
    gh.genre_id,
    gh.genre_name
From genre_hierarchy gh
join track t on gh.track_id = t.id
Order by gh.track_id, gh.genre_id;
