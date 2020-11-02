#!/usr/bin/python3
# Cerberus Nuclear Ltd

"""
    This module creates all the CSS used in the HTML output
"""


def i(arg):
    """ Indent the arg string to make the html more readable """
    return f'   {arg}'


def reset():
    """ CSS reset to remove any inbuilt CSS in the web browser. """
    return """
        /*
        html5doctor.com Reset Stylesheet
        v1.6.1
        Last Updated: 2010-09-17
        Author: Richard Clark - http://richclarkdesign.com
        Twitter: @rich_clark
        */

        html, body, div, span, object, iframe,
        h1, h2, h3, h4, h5, h6, p, blockquote, pre,
        abbr, address, cite, code,
        del, dfn, em, img, ins, kbd, q, samp,
        small, strong, sub, sup, var,
        b, i,
        dl, dt, dd, ol, ul, li,
        fieldset, form, label, legend,
        table, caption, tbody, tfoot, thead, tr, th, td,
        article, aside, canvas, details, figcaption, figure,
        footer, header, hgroup, menu, nav, section, summary,
        time, mark, audio, video {
            margin:0;
            padding:0;
            border:0;
            outline:0;
            font-size:100%;
            vertical-align:baseline;
            background:transparent;
        }

        body {
            line-height:1;
        }

        article,aside,details,figcaption,figure,
        footer,header,hgroup,menu,nav,section {
            display:block;
        }

        nav ul {
            list-style:none;
        }

        blockquote, q {
            quotes:none;
        }

        blockquote:before, blockquote:after,
        q:before, q:after {
            content:'';
            content:none;
        }

        a {
            margin:0;
            padding:0;
            font-size:100%;
            vertical-align:baseline;
            background:transparent;
        }

        /* change colours to suit your needs */
        ins {
            background-color:#ff9;
            color:#000;
            text-decoration:none;
        }

        /* change colours to suit your needs */
        mark {
            background-color:#ff9;
            color:#000;
            font-style:italic;
            font-weight:bold;
        }

        del {
            text-decoration: line-through;
        }

        abbr[title], dfn[title] {
            border-bottom:1px dotted;
            cursor:help;
        }

        table {
            border-collapse:collapse;
            border-spacing:0;
        }

        /* change border colour to suit your needs */
        hr {
            display:block;
            height:1px;
            border:0;
            border-top:1px solid #cccccc;
            margin:1em 0;
            padding:0;
        }

        input, select {
            vertical-align:middle;
        }

        /* End of CSS Reset */
        /*------------------------------------------------*/

        """


def write_css(f):
    """ Write standard CSS for the HTML output. """
    # HTML CSS STYLING FOR SECTIONS
    f.write(i('<style type="text/css">\n'))
    f.write(reset())
    f.write(i('\n\n'))

    # general
    f.write(i('html, body {height: 100%; background-color: white; font-family: "Work Sans", Raleway, sans-serif;}\n'))
    f.write(i('p {text-align: center; color: #333333}\n'))
    f.write(i('h1 {text-align: center; padding: 10px 0px; color: #1c76bc; font-size: 28px; margin-top: 20px;}\n'))
    f.write(i('h2 {text-align: center; padding: 10px 0px; color: #333333; font-size: 20px;}\n'))
    f.write(i('h3 {text-align: center; padding: 10px 0px; color: #333333;; font-size: 16px;}\n'))
    f.write(i('div {padding: 20px 0px;}\n'))
    f.write(i('div .tally-results {padding: 5px 0px;}\n'))
    f.write(i('div .tally-checks {padding: 5px 0px;}\n'))
    f.write(i('.case-details {font-size: 16px}\n'))

    # tables
    f.write(i('.table {text-align:center; border-collapse:collapse; margin:auto; line-height:10px; border:1px solid black;}\n'))
    f.write(i('.table td {padding:10px; line-height: 120%; font-size:14px; color: #333333; border:1px solid black;}\n'))
    f.write(i('.table th {padding:10px; line-height: 120%; font-size:14px; color: #333333; border:1px solid black; background-color: #cce0ff;  }\n'))

    # navbar
    f.write(i('''.navbar {
        position: fixed;
        background-color: #cce0ff;
        margin: 0;
        border-bottom: 1px solid #1c76bc ;
        width: 100%; 
        height: auto;
        padding: 5px;
        }\n'''))
    f.write(i('''.navbar ul {
        list-style: none;
        display: flex; 
        flex-direction: row; 
        flex-wrap: wrap; 
        justify-content: center; 
        }'''))
    f.write(i('''.navbar li a {
        padding: 5px 20px;
        line-height: 170%;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        color: rgba(51,51,51,1);
        }\n'''))
    f.write(i('.navbar a:hover {background-color: #1c76bc; color: #FFFFFF}\n'))

    # cerberus logo
    f.write(i('#logo {text-align: center; padding-top: 100px;} \n'))
    f.write(i('#logo img{width: 50%; height: auto;} \n'))


    # details
    f.write(i('#details .table {border: none; padding: 10px; table-layout: fixed; width: 100%;}'))
    f.write(i('#details td {border: none; padding: 10px; font-size: 20px; width: 50%;} \n'))

    # parameters
    f.write(i('#parameters table {border: none; padding: 10px; table-layout: fixed; width: 100%;} \n'))
    f.write(i('#parameters td {border: none; padding: 5px 10px; font-size: 20px; line-height: 120%; width: 50%;} \n'))


    # warnings
    f.write(i('#warnings, #duplicates, #comments {text-align: center;}\n'))
    f.write(i('#warning_messages, #duplicate_messages, #comment_messages {display:inline-block; padding: 5px}\n'))
    f.write(i('#warning_messages, p {text-align: left; padding: 5px; }\n'))
    f.write(i('#duplicate_messages, p {text-align: left; padding: 5px; }\n'))

    # comments
    #f.write(i('#comments {text-align: center;}\n'))
    #f.write(i('#comment_messages {display:inline-block;}\n'))
    f.write(i('#comment_messages p {text-align: left; padding: 5px;}\n'))

    # mcnp input
    f.write(i('#input_file {text-align: center;}\n'))
    f.write(i('#input {display:inline-block; }\n'))
    f.write(i('#input p {white-space:pre; font-family: Courier,monospace; font-weight:bold; text-align:left; }\n'))
    f.write(i('</style>\n'))
