-- models/staging/stg_gdp.sql
WITH gdp AS (
    SELECT
        gdp."年" AS year,
        gdp."期" AS period,
        CONCAT(SUBSTR(gdp."年", 1, 3), '0') AS ten_years,
        gdp."国内総生産(支出側)" AS gdp
    FROM gdp_actual AS gdp
)
SELECT
    g.year AS year,
    CONCAT(g.year, '-01-01') AS year_full,
    CASE
        WHEN g.period = '4-6' THEN 'Q1'
        WHEN g.period = '7-9' THEN 'Q2'
        WHEN g.period = '10-12' THEN 'Q3'
        ELSE 'Q4'
    END AS quarter,
    g.ten_years,
    {{ str_to_decimal('gdp', 38, 1) }} AS gdp
FROM gdp AS g
