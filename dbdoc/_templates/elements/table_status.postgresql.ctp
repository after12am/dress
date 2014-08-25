<table>
    <tr>
        <th>Field</th>
        <th>Type</th>
        <th>Collation</th>
        <th>Null</th>
        <th>Key</th>
        <th>Default</th>
        <th>Extra</th>
        <th>Comment</th>
    </tr>
    {% for c in item.columns %}
    <tr>
        <td>{{c[0]}}</td>
        <td>{{c[1]}}{% if c[2] %}({{c[2]}}){% endif %}</td>
        <td>{{c[3]}}</td>
        <td>{{c[4]}}</td>
        <td>{% if c[8] %}{{c[8]}}{% endif %}</td>
        <td>{{c[5]}}</td>
        <td>{{c[6]}}</td>
        <td>{{c[7]}}</td>
    </tr>
    {% endfor %}
</table>