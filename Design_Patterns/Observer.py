class Channel:
    def __init__(self):
        self.subs = []
    def subscribe(self, fn):
        self.subs.append(fn)
    def post(self, msg):
        for fn in self.subs:
            fn(msg)

yt = Channel()
yt.subscribe(lambda m: print(f"User 1: {m}"))
yt.subscribe(lambda m: print(f"User 2: {m}"))
yt.post("New video up!")