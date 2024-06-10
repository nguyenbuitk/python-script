import webbrowser

search_term = input("Enter search term: ")
search_url = "https://google.com/search?q=" + search_term
webbrowser.open(search_url)