-- macros/str_to_decimal.sql
{% macro str_to_decimal(num, precision, scale) %}
    CAST(CAST({{ remove_comma(num) }} AS DOUBLE) AS DECIMAL({{ precision }}, {{ scale }}))
{% endmacro %}