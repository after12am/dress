<!DOCTYPE html>
<!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{database.name}} {{version}} documentation</title>
<link href='https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic|Roboto+Slab:400,700|Inconsolata:400,700' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="_static/css/theme.css" type="text/css" />
<link rel="stylesheet" href="_static/css/custom.css" type="text/css" />
<link rel="top" title="{{database.name}} {{version}} database documentation" href="#"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.6.2/modernizr.min.js"></script>
<script src="_static/jquery.js"></script>
</head>
<body class="wy-body-for-nav" role="document">
    <div class="wy-grid-for-nav">
        <nav data-toggle="wy-nav-shift" class="wy-nav-side">
            <div class="wy-side-nav-search">
                <a href="#" class="fa fa-home"> {{database.name}}</a>
                <!-- 
                <div role="search">
                    <form id ="rtd-search-form" class="wy-form" action="search.html" method="get">
                        <input type="text" name="q" placeholder="Search docs" />
                        <input type="hidden" name="check_keywords" value="yes" />
                        <input type="hidden" name="area" value="default" />
                    </form>
                </div>
                 -->
            </div>
            <div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="main navigation">
                <ul class="simple">
                    {% for table in database.tables %}
                    <li class="toctree-l1" data-hash="{{table}}"><a href="#{{table}}">{{table}}</a></li>
                    {% endfor %}
                </ul>
            </div>
            &nbsp;
        </nav>
        <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">
            <nav class="wy-nav-top" role="navigation" aria-label="top navigation">
                <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
                <a href="#">{{database.name}}</a>
            </nav>
            <div class="wy-nav-content">
                <div class="rst-content">
                    <div role="navigation" aria-label="breadcrumbs navigation">
                        <h1>Welcome to {{database.name}}&#8217;s database documentation!<a class="headerlink" href="#welcome-to-{{database.name}}-s-documentation" title="Permalink to this headline">¶</a></h1>
                         <hr/>
                    </div>
                    <div role="main" class="document">
                        {% for table, item in database.tables.iteritems() %}
                            <div id="{{table}}" class="section">
                                <h2>{{table}}<a class="headerlink" href="#welcome-to-{{database.name}}-s-documentation" title="Permalink to this headline">¶</a></h2>
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
                            </div>
                            {% if not loop.last %}
                                <hr/>
                            {% endif %}
                        {% endfor %}
                    </div>
                    <footer>
                        <hr/>
                        <div role="contentinfo">
                            <p>&copy; Copyright {{today.year}}, {{author}}.</p>
                        </div>
                        <a href="https://github.com/snide/sphinx_rtd_theme">Sphinx theme</a> provided by <a href="https://readthedocs.org">Read the Docs</a>
                    </footer>
                </div>
            </div>
        </section>
    </div>
<script type="text/javascript">

function update_navi(hash) {
    $('.wy-menu li').removeClass('current');
    $('.wy-menu li[data-hash=' + hash + ']').toggleClass('current');
}

$(function() {
    update_navi(location.hash.split('#')[1]);
    $('.wy-menu li a').click(function() {
        var hash = $(this).parent().attr('data-hash');
        update_navi(hash);
    });
});

</script>
<script type="text/javascript" src="_static/jquery.js"></script>
<script type="text/javascript" src="_static/underscore.js"></script>
<script type="text/javascript" src="_static/js/theme.js"></script>    
</body>
</html>