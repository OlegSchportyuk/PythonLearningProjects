from operator import itemgetter

import requests
from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    # Построение словаря для каждой статьи.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        continue
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, links, num_comments = [], [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    hn_link = submission_dict['hn_link']
    links.append(f"<a href='{hn_link}'>{submission_dict['title'][:15]}</a>")
    num_comments.append(submission_dict['comments'])

# Построение визуализации.
data = [{
    'type': 'bar',
    'x': links,
    'y': num_comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-discussed articles on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Number of comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_articles.html')