<table>
    <tr>
        <th>Field</th>
        <th>Type</th>
        <th>Collation</th>
        <th>Null</th>
        <th>Key</th>
        <th>Default</th>
        <th>Comment</th>
    </tr>
    {% for c in item.columns %}
    <tr>
        <td>{{c[3]}}</td>
        <td>{{c[27]}}{% if c[8] %}({{c[8]}}){% endif %}</td>
        <td>{{c[21]}}</td>
        <td>{{c[6]}}</td>
        <td>{{c[45]}}</td>
        <td>{{c[5]}}</td>
        <td>{{c[44]}}</td>
    </tr>
    {% endfor %}
</table>