import jinja2, strip

jinja2.filters.FILTERS['strip_extra_singlequote'] = strip.strip_extra_singlequote