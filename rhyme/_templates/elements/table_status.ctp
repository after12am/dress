{% if datasource == 'mysql' %}
    {% include "elements/table_status.mysql.ctp" %}
{% elif datasource == 'sqlite3' %}
    {% include "elements/table_status.sqlite3.ctp" %}
{% elif datasource == 'postgresql' %}
    {% include "elements/table_status.postgresql.ctp" %}
{% endif %}