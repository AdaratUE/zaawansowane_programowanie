class Movies:
    def __init__(self, id, title, genre):
        self.id = id
        self.title = title
        self.genre = genre

    def get(self):
        return {'id': self.id,
                'title': self.title,
                'genre': self.genre}
