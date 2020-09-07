import requests
import lxml.html


url = str(input("Enter site url: "))


def lxml_title(html_text):
    tree = lxml.html.document_fromstring(html_text)
    text_original = tree.xpath("/html/head/title/text()")
    print(text_original)


def main(siteurl):
    html_text = requests.get(siteurl).text
    lxml_title(html_text)


if __name__ == '__main__':
    main(url)