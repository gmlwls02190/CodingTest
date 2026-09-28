-- 코드를 작성해주세요
select
    sum(g.score) as score,
    e.emp_no,
    e.emp_name,
    e.position,
    e.email
from hr_employees as e
join hr_grade as g
on e.emp_no=g.emp_no
group by e.emp_no
having score>= all(
select
    sum(g.score)
from hr_grade as g
join hr_employees as e
on g.emp_no=e.emp_no
group by e.emp_no);