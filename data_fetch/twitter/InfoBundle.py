class InfoBundle:

    def __init__(self, tweets):
        self.date = tweets[0].created_at.strftime("%Y-%m-%d")
        self.text = " ".join([t.full_text for t in tweets])
