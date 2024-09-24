html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>
    <h1 id="header">Python Kursu</h1>
    <div class="grup1">
        <h2> Programlama</h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup2"></div>
        <h2> Modüller</h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body
result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2.string

result = soup.find_all('h2')[0]

result = soup.find_all('div')[1].ul.find_all('li')[1]
print (result)