-- macros/remove_comma.sql
{% macro remove_comma(num) %}
    replace({{ num }}, ',', '')
{% endmacro %}