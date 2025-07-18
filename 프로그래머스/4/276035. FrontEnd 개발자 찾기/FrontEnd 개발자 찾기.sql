WITH FRONTEND_SKILL AS (
    SELECT
        SUM(CODE) AS TOTAL_CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)

SELECT
    D.ID,
    D.EMAIL,
    D.FIRST_NAME,
    D.LAST_NAME
FROM DEVELOPERS D
JOIN FRONTEND_SKILL F 
    ON D.SKILL_CODE & F.TOTAL_CODE > 0
ORDER BY D.ID ASC;