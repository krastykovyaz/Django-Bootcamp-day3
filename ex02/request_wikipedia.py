import requests, json, dewiki, sys


def req_wiki():
    if len(sys.argv) == 2:
        query = sys.argv[1]
        session = requests.Session()

        url = 'https://en.wikipedia.org/w/api.php'

        arguments = {
            "action": "parse",
            "page": query,
            "prop": "wikitext",
            "format": "json",
            "redirects": True,
            "formatversion": 2
        }

        req = session.get(url=url, params=arguments)
        data = req.json()
        try:
            answer = dewiki.from_string(data['parse']['wikitext'])
        
            res = ""
            for line in answer.split("\n"):
                if len(line) > 0:
                    res += line
                    res += "\n"
            with open(query + ".wiki", "w") as handle:
                handle.write(res)
        except:
            print("Probably this is misspeling. Try again.")


if __name__ == '__main__':
    req_wiki()