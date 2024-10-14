-- 코드를 작성해주세요
SELECT
    sum(PRICE) as TOTAL_PRICE
FROM
    ITEM_INFO 
WHERE
    RARITY = "LEGEND"
    