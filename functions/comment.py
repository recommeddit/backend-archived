from collections import namedtuple

Bounds = namedtuple('Bounds', "start end")


#
# class Keyword:
#     def __init__(self, text, bounds_list):
#         self.bounds_list = bounds_list
#         self.comments =
#         self.set_bounds()
#
#     @classmethod
#     def from_extraction(cls, extraction):
#         return cls(dict["text"], dict["score"], dict["url"])
#
#     def set_bounds(self):
#         for i, comment in enumerate(self.comments):
#             if i == 0:
#                 offset = 0
#             else:
#                 offset = self.bounds_list[i - 1].end + 2  # we add 2 because there is "\n\n" between comments
#             self.bounds_list[i] = Bounds(offset, offset + len(str(self.comments[i])))
#
#     def __str__(self):
#         return self.text


class Comment:
    def __init__(self, text, score, url):
        self.text = text
        self.score = score
        self.url = url

    @classmethod
    def from_dict(cls, dict):
        return cls(dict["text"], dict["score"], dict["url"])

    def __str__(self):
        return self.text


class CommentList:
    def __init__(self, comments):
        self.bounds_list = [Bounds(0, 0)] * len(comments)
        self.comments = comments
        self.set_bounds()

    def chunk(self, limit=42000):
        next_chunk_start_index = next((i for i, bounds in enumerate(self.bounds_list) if bounds.end >= limit),
                                      None)
        if next_chunk_start_index is None:
            return [ChunkedComment(self.comments)]
        next_chunk = CommentList(self.comments[next_chunk_start_index:])
        return [ChunkedComment(self.comments[0:next_chunk_start_index])] + next_chunk.chunk()

    def to_list(self):
        return self.comments

    def set_bounds(self):
        for i, comment in enumerate(self.comments):
            if i == 0:
                offset = 0
            else:
                offset = self.bounds_list[i - 1].end + 2  # we add 2 because there is "\n\n" between comments
            self.bounds_list[i] = Bounds(offset, offset + len(str(self.comments[i])))


class ChunkedComment(CommentList):
    def __init__(self, comments):
        super().__init__(comments)

    def __str__(self):
        text = ""
        for comment in self.comments[:-1]:
            text += str(comment) + "\n\n"
        text += str(self.comments[-1])

        return text
