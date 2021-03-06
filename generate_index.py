import os

def get_li(file_name):
    return f'<li><a href="Pages/{file_name}">{file_name.replace(".html","")}</a></li>'

links = "\n".join([get_li(file) for file in os.listdir("Pages") if ".html" in file])

html = f"""<!DOCTYPE html>
<link rel="stylesheet" href="Pages/markdown.css" />
<html>
<head>
<meta charset="UTF-8">
<title>UVA CS 4501 - Machine Learning Notes</title>
</head>
<body background="background.jpg">
<h1>UVA CS 4501 - Machine Learning</h1>
<ul>
   {links}
</ul>
</body>
 <head>
 <style type ="text/css" >
   .footer{{ 
       position: fixed;     
       text-align: center;    
       bottom: 0px; 
       width: 100%;
   }}  
</style>
</head>
<body>
    <div class="footer"><a href="https://github.com/jrodal98">My github</a></div>
</body>
</html>
"""

with open("index.html","w") as f:
    f.write(html)
