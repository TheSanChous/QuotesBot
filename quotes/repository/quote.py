class Quote:
    id = int()
    dialogue = False
    private = False
    tags = []
    url = None
    favorites_count = int()
    upvotes_count = int()
    downvotes_count = int()
    author = None
    body = None

    def __init__(self, d: dict):
        self.__dict__.update(d)
        pass
