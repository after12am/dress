<table style="min-width:100%;">
    <tr>
        <th>Fielda</th>
        <th>Type</th>
        <th>Null</th>
        <th>Key</th>
        <th>Default</th>
    </tr>
    {% for c in item.columns %}
    <tr>
        <td>{{c[1]}}</td>
        <td>{{c[2]}}</td>
        <td>{% if c[3] == 1 %}NO{% else %}YES{% endif %}</td>
        <td>{% if c[5] == 1 %}PRI{% endif %}</td>
        <td>{{c[4]}}</td>
    </tr>
    {% endfor %}
</table>