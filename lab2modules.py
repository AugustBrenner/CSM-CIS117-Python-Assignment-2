#!/usr/local/bin/python3
# Name: August Brenner
# File name: lab2.modules.py
# Date: July 3rd, 2013


# module for generating header HTML
def HTML_START(title):
    HTML_START = """
    <html>
        <head>
            <style type='text/css'>
                td {
                    text-align: right;
                    padding-left: 0.5em;
                    padding-right: 0.5em;
                }
                #top-nav ul li {
                    display: inline;
                    padding-right: 1em;
                }
            </style>
        </head>
        <body>
            <div id="top-nav">
                <ul>
                   <li><a href="lab2.1.py">lab2.1.py</a></li>
                   <li><a href="lab2.2.py">lab2.2.py</a></li>
                   <li><a href="lab2.3.py">lab2.3.py</a></li>
                </ul>
            </div>
            <p>********** """ + title + """ **********</p>
    """
    print(HTML_START)


HTML_END = """
    </body>
</html>"""


# function for generating table from a list of words
def table(cell_array, cells_per_row):
    i = 0
    print('''<pre><table border="1"><tr>''')
    for cell in cell_array:
        if i % cells_per_row == 0:
            print('</tr><tr>')
        print('<td>' + str(cell) + '</td>')
        i += 1

    if len(cell_array) % cells_per_row != 0:
        extra_cells = cells_per_row - (len(cell_array) % cells_per_row)
        print('<td></td>' * extra_cells)

    print('</tr></table></pre>')