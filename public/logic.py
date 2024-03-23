from browser import document as D, html as H, ajax as JSON
def arrived_all_posts(response):
    TBODY = []
    for row in response.json:
        TBODY.append(
            H.TR([
                H.TD(row["author"]), 
                H.TD(row["title"])
            ])
        )
    D <= H.TABLE(TBODY)
def get_all_posts():
    JSON.get("http://localhost:3000/posts", oncomplete = arrived_all_posts)
get_all_posts()
D <= H.H1("Hello!")
