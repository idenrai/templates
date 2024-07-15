-- models/marts/gdp_total_info.sql
WITH gdp AS (
    SELECT * FROM {{ ref('stg_gdp') }}
),
gdp_year AS (
    SELECT * FROM {{ ref('stg_gdp_year') }}
),
final AS (
    SELECT
        gdp.year AS year,
        gdp.gdp AS quarter_gdp,
        gdp_year.gdp_sum AS year_sum_gdp,
        gdp_year.gdp_average AS year_avg_gdp
    FROM gdp
    LEFT OUTER JOIN gdp_year ON
        gdp.year = gdp_year.year
)
SELECT *
FROM final
ORDER BY final.year