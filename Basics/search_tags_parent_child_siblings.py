from bs4 import BeautifulSoup


html_doc  = """

<html lang="en-US"><head><title>The Dormouse's story</title></head>
  <body>
    <h1 class="title"><b>The Dormouse's story</b></h1>

	<p>KING JATIN</p>
    <p class="story">Once upon a time there were three little sisters; and their names were
      <strong>test</strong>
  <a href="http://example.com/elsie" class="sister wut" id="link1"><strong>Elsie</strong></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p data-original="test">foo</p>

<div class="curr_lang">
<p>
Inside a div.
</p>
</div>
</body>
</html>

"""

soup = BeautifulSoup(html_doc, 'lxml')


#Search for All children
# p = soup.find('p', class_ ='story')
# all_p_children = p.findChildren()
# print all_p_children



#Search for all Parent
# p = soup.find('p', class_ ='story')
# all_p_parent = p.findParent()
# print all_p_parent



#Search for all Siblings
first_a = soup.find('a')
remaining_sib = first_a.findNextSiblings()
print remaining_sib







