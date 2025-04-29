<!-- शुभमानन्दगुप्तेन तु भगवत्प्रसादात् भारते रचितः -->
<!DOCTYPE html>
<html lang="{ln_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="robots" content="index">
    {% block main -%}
    <title>{title{{ name }}}</title>
    <meta property="og:title" content="{title{{ name }}}">
    <meta name="description" content="{description{{ name }}}">
    <meta property="og:description" content="{description{{ name }}}">
    <meta property="og:site_name" content="{title{{ name }}}">
    {% endblock -%}
    <meta property="og:type" content="app">
    {% block extra %}{% endblock -%}
    <link rel="icon" href="/img/main.png" id=lipi_icon type="image/png">
    {% for x in lng_lst -%}
        {% set ln = "/" + x -%}
        {% if x == "en" -%}
            {% set ln = "" -%}
        {% endif -%}
        <link rel="alternate" href="{{ url + ln + pRShTha }}" hreflang="{{ x }}">
    {% endfor -%}
    <meta property="og:image" content="https://cdn.jsdelivr.net/gh/lipilekhika/dist@latest/i/bhasha.jpg">
    <meta property="og:image:width" content="465.5">
    <meta property="og:image:height" content="175">{extras0}
</head>
<body>
    <link href=/app.css rel=stylesheet>
    <script src=/src/query.js></script>
    <script src=/src/main.js></script><script src=/src/lib.js></script>
    <script>let s = {options};</script><script src=/app.js></script>
    <link href=/img/ChavyaH.css rel=stylesheet>{extras1}
</body>
</html>