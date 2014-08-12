<!DOCTYPE html>
<!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Welcome to sample’s documentation! &mdash; sample 0.1.0 documentation</title>
<link href='https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic|Roboto+Slab:400,700|Inconsolata:400,700' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="_static/css/theme.css" type="text/css" />
<link rel="top" title="sample 0.1.0 documentation" href="#"/> 
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.6.2/modernizr.min.js"></script>
<style type="text/css">
.wy-nav-content {
    max-width: none;
}
table, caption, tbody, tfoot, thead, tr, th, td {
	margin: 0;
	padding: 0;
	border: 0;
	outline: 0;
	font-size: 100%;
	vertical-align: baseline;
	background: transparent;
}
table {border-spacing: 0; } /* IMPORTANT, I REMOVED border-collapse: collapse; FROM THIS LINE IN ORDER TO MAKE THE OUTER BORDER RADIUS WORK */
/*
Table Style - This is what you want
------------------------------------------------------------------ */
.table {
    margin-top: 30px;
    padding-top: 10px;
}

.table:first-child {
    margin-top: 0;
}

table a:link {
	color: #666;
	font-weight: bold;
	text-decoration:none;
}
table a:visited {
	color: #999999;
	font-weight:bold;
	text-decoration:none;
}
table a:active,
table a:hover {
	color: #bd5a35;
	text-decoration:underline;
}
table {
/*          font-family:Arial, Helvetica, sans-serif;*/
	color:#666;
	font-size:.8em;
	letter-spacing: .04em;
/*          text-shadow: 1px 1px 0px #fff;*/
	background:#eaebec;

	border:#ccc 1px solid;

	-moz-border-radius:3px;
	-webkit-border-radius:3px;
	border-radius:3px;

	-moz-box-shadow: 0 1px 2px #d1d1d1;
	-webkit-box-shadow: 0 1px 2px #d1d1d1;
	box-shadow: 0 1px 2px #d1d1d1;

	min-width: 1000px;
}
table th {
	padding:21px 25px 22px 25px;
    border:1px solid #2980b9;
/*  background: #ededed;
    background: -webkit-gradient(linear, left top, left bottom, from(#ededed), to(#ebebeb));
	background: -moz-linear-gradient(top,  #ededed,  #ebebeb);*/
	background: #2980b9;
	color: #fff;
}
table th:first-child{
	text-align: left;
	padding-left:20px;
}
table tr:first-child th:first-child{
	-moz-border-radius-topleft:3px;
	-webkit-border-top-left-radius:3px;
	border-top-left-radius:3px;
}
table tr:first-child th:last-child{
	-moz-border-radius-topright:3px;
	-webkit-border-top-right-radius:3px;
	border-top-right-radius:3px;
}
table tr{
	text-align: center;
	padding-left:20px;
}
table tr td.lalign {
	text-align: left;
}
table tr td:first-child{
	text-align: left;
	padding-left:20px;
	border-left: 0;
}
table tr td {
	padding:18px;
	border-top: 1px solid #ffffff;
	border-bottom:1px solid #e0e0e0;
	border-left: 1px solid #e0e0e0;

	background: #fafafa;
	background: -webkit-gradient(linear, left top, left bottom, from(#fbfbfb), to(#fafafa));
	background: -moz-linear-gradient(top,  #fbfbfb,  #fafafa);
}
table tr.even td{
	background: #f6f6f6;
	background: -webkit-gradient(linear, left top, left bottom, from(#f8f8f8), to(#f6f6f6));
	background: -moz-linear-gradient(top,  #f8f8f8,  #f6f6f6);
}
table tr:last-child td{
	border-bottom:0;
}
table tr:last-child td:first-child{
	-moz-border-radius-bottomleft:3px;
	-webkit-border-bottom-left-radius:3px;
	border-bottom-left-radius:3px;
}
table tr:last-child td:last-child{
	-moz-border-radius-bottomright:3px;
	-webkit-border-bottom-right-radius:3px;
	border-bottom-right-radius:3px;
}
table tr:hover td{
	background: #f2f2f2;
	background: -webkit-gradient(linear, left top, left bottom, from(#f2f2f2), to(#f0f0f0));
	background: -moz-linear-gradient(top,  #f2f2f2,  #f0f0f0);	
}
</style>
</head>
<body class="wy-body-for-nav" role="document">
    <div class="wy-grid-for-nav">
        
        <nav data-toggle="wy-nav-shift" class="wy-nav-side">
            <div class="wy-side-nav-search">
                <a href="#" class="fa fa-home"> {{database}}</a>
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
                    {% for table in tablestatus %}
                    <li class="toctree-l1"><a href="#{{table}}">{{table}}</a></li>
                    <!-- <li class="toctree-l1"><a class="current" href="#">{{table}}</a></li> -->
                    {% endfor %}
                </ul>
            </div>
            
            &nbsp;
        </nav>

        <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">
            <nav class="wy-nav-top" role="navigation" aria-label="top navigation">
                <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
                <a href="#">sample</a>
            </nav>
            
            <div class="wy-nav-content">
                <div class="rst-content">
                    <div role="navigation" aria-label="breadcrumbs navigation">
                        <h1>Welcome to {{database}}&#8217;s database documentation!<a class="headerlink" href="#welcome-to-sample-s-documentation" title="Permalink to this headline">¶</a></h1>
                         <hr/>
                    </div>
                    
                    <div role="main" class="document">
                        
                        {% for table in tablestatus %}
                        <div id="{{table}}" class="section">
                            <h2>{{table}}<a class="headerlink" href="#welcome-to-sample-s-documentation" title="Permalink to this headline">¶</a></h2>
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
                                {% for item in columns[table] %}
                                <tr>
                                    <td>{{item[0]}}</td>
                                    <td>{{item[1]}}</td>
                                    <td>{{item[2]}}</td>
                                    <td>{{item[3]}}</td>
                                    <td>{{item[4]}}</td>
                                    <td>{{item[5]}}</td>
                                    <td>{{item[6]}}</td>
                                    <td>{{item[8]}}</td>
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
                            <p>&copy; Copyright 2014, satoshi.</p>
                        </div>

                        <a href="https://github.com/snide/sphinx_rtd_theme">Sphinx theme</a> provided by <a href="https://readthedocs.org">Read the Docs</a>
                    </footer>
                </div>
            </div>
        </section>
    </div>

<!-- <script type="text/javascript">
var DOCUMENTATION_OPTIONS = {
    URL_ROOT:'./',
    VERSION:'0.1.0',
    COLLAPSE_INDEX:false,
    FILE_SUFFIX:'.html',
    HAS_SOURCE:    true
};
</script> -->
<script type="text/javascript" src="_static/jquery.js"></script>
<script type="text/javascript" src="_static/underscore.js"></script>
<!-- <script type="text/javascript" src="_static/doctools.js"></script> -->
<script type="text/javascript" src="_static/js/theme.js"></script>    
<script type="text/javascript">
jQuery(function () {
    SphinxRtdTheme.StickyNav.enable();
});
</script>
</body>
</html>