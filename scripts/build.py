import json
from datetime import datetime
import os


def read_data():
    start = "const searchDocuments ="
    with open("./searchDocuments.js") as f:
        data = f.read()[len(start) :]
        data = json.loads(data)
    return data


def short_date(created_at):
    date = datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")
    if date.year == datetime.now().year:
        return date.strftime("%b %d")
    return date.strftime("%b %d, %Y")


def url(item):
    return "https://twitter.com/b0rk/status/" + item["id_str"]


def get_page(item):
    date = short_date(item["created_at"])
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>julia's twitter archive</title>
  <link rel="stylesheet" href="../../../nitter.css">
  <link rel="stylesheet" href="../../../twitter.css">
  <link rel="stylesheet" href="../../../fonts/css/fontello.css">
  <link rel="stylesheet" href="../../../styles.css">
</head>
<body>
  <div class="wrapper" id="app">
    <h1><a href="../../..">julia's twitter archive</a></h1>

    <div class="timeline">
      <div class="timeline-item">
        <a class="tweet-link" href="{url(item)}"></a>
        <div class="tweet-body">
          <div><div class="tweet-header">
              <a class="tweet-avatar" href="/"><img class="avatar round" src="../../../profile.jpg" alt=""></a>
              <div class="tweet-name-row">
                <div class="fullname-and-username">
                  <a class="fullname" href="/" title="🔎Julia Evans🔍">🔎Julia Evans🔍</a>
                  <a class="username" href="/" title="@b0rk">@b0rk</a>
                </div>
                <span class="tweet-date"><a href="{url(item)}" title="{date}">{date}</a></span>
              </div>
            </div></div>
            <div class="tweet-content media-body" dir="auto"> {item['full_text']} </div>
            <div class="tweet-stats">
              <span class="tweet-stat"><div class="icon-container"><span class="icon-retweet" title=""></span> {item['retweet_count']}</div></span>
              <span class="tweet-stat"><div class="icon-container"><span class="icon-heart" title=""></span> {item['retweet_count']}</div></span>
            </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""


def main():
    data = read_data()
    for item in data:
        os.makedirs(f"b0rk/status/{item['id_str']}", exist_ok=True)
        with open(f"./b0rk/status/{item['id_str']}/index.html", "w") as f:
            f.write(get_page(item))


if __name__ == "__main__":
    main()
