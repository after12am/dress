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
        <td>{{c[1]}}</td>
        <td>{{c[2]}}</td>
        <td>{{c[3]}}</td>
        <td>{{c[4]}}</td>
        <td>{{c[5]}}</td>
        <td>{{c[6]}}</td>
        <td>{{c[8]}}</td>
    </tr>
    {% endfor %}
</table>