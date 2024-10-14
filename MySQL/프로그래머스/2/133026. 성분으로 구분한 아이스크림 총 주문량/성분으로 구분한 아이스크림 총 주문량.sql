-- 코드를 입력하세요
SELECT
    i.INGREDIENT_TYPE, sum(f.TOTAL_ORDER)
FROM
    FIRST_HALF as f
JOIN
    ICECREAM_INFO as i
ON
    f.FLAVOR = i.FLAVOR
GROUP BY
    i.INGREDIENT_TYPE
ORDER BY
    f.TOTAL_ORDER