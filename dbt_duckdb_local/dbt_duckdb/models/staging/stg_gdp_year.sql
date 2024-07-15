-- models/staging/stg_gdp_year.sql
SELECT 
    year,
    SUM(gdp) AS gdp_sum,
    AVG(gdp) AS gdp_average
FROM {{ ref('stg_gdp') }}
GROUP BY year
ORDER BY year