from requests import get


class Memory:

    newslist = dict()
    xs = []

    def getbutton(self, topic, index):

        if topic in self.newslist:
            return self.newslist[topic][index]

        x = self.get_noticias(topic)
        return x[index]

    def get_noticias(self, topic):

        if topic in self.newslist:
            return self.newslist[topic]

        endpoint = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY"

        headers = {
            'Content-Type': 'application/json'
        }

        querystring = {"q": input}

        querystring = {
            "q": topic,
            "sortBy": "popularity"
        }

        data = get(endpoint, headers=headers, params=querystring).json

        if data["status"] != "ok":
            ValueError("status not ok in the api")

        if len(self.newslist) > 1000:
            self.newslist.pop(self.xs.pop())

        self.newslist[topic] = data["articles"]
        self.xs.append(topic)

        return data['articles']


