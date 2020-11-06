class InfoBundle:

    def __init__(self, tweets):
        self.date = tweets[0].created_at.strftime("%Y-%m-%d")
        txt = ""
        for t in tweets:
            txt += t.full_text
        self.text = txt
