"""
Sample Input

4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

"""
#Example of using the HTMLParser module.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        # decide if single line or multi-line
        if len(data.splitlines())>1:
            print(">>> Multi-line Comment")
            [print(line) for line in data.splitlines()]
        else:
            print(">>> Single-line Comment")
            print(data)
        
    def handle_data(self, data):
        if len(data)>1:
            print(">>> Data")
            print(data)
