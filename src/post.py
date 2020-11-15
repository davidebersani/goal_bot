class Post() :
    def __init__(self, post_id, timestamp, text_to_publish) :
        self.post_id = post_id
        self.timestamp = timestamp
        self.text_to_publish = text_to_publish

    def __eq__(self, other):
        return self.post_id == other.post_id
    
    