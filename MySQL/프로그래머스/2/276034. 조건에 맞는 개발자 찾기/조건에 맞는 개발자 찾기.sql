-- 코드를 작성해주세요
# SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
# FROM DEVELOPERS
# WHERE (SKILL_CODE & 256) or (SKILL_CODE & 1024)
# ORDER BY ID ASC

select distinct(d.ID), d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from DEVELOPERS d
join SKILLCODES s on d.SKILL_CODE & s.CODE
where s.NAME = 'C#'
    or s.NAME = 'Python'
order by ID;