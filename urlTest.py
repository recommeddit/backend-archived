import url_html as urlEx

redditComment = "code.visualstudio.com is the best code editor"
commentUrl = urlEx.get_url(redditComment)
resolvedUrl = urlEx.check_url(commentUrl)
parsedHtml = urlEx.html_to_text(resolvedUrl)
print(parsedHtml)
