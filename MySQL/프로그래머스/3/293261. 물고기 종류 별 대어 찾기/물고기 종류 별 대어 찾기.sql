-- 코드를 작성해주세요
SELECT
    FISH_INFO.ID, FISH_NAME_INFO.FISH_NAME, FISH_INFO.LENGTH
FROM
    FISH_INFO
JOIN
    FISH_NAME_INFO 
ON
    FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE
WHERE
    FISH_INFO.LENGTH = (SELECT 
                            max(FISH_INFO.LENGTH) 
                        FROM 
                            FISH_INFO 
                        WHERE 
                            FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE)