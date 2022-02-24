"""help module with Note class for notebook module"""
import datetime

available_ids = (i for i in range(1000))


class Note:
    """implements certain notes in notebook with text,creation date and tags"""

    def __init__(self, memo: str, tags: list = []) -> None:
        """constructor for class with automatic id assigning

        Args:
            memo (str): text of the note
            tags (list, optional): tags for search. Defaults to [].

        >>> n1 = Note("My first note", ["hi", "first"])

        """
        self.text = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
        self.id = available_ids.__next__()

    def match(self, search_filter: str) -> bool:
        """checks whether note appeared in filtered notes by text or tags

        Args:
            search_filter (str): substring to search in texts or tags

        Returns:
            bool: substring in text or tags

        >>> n1 = Note("My first note", ["hi", "first"])

        >>> n1.match('hi')
        True
        """
        return search_filter in self.text or search_filter in self.tags

    def __str__(self) -> str:
        """represents Note object in string

        Returns:
            str: string with text, tags, date and id of the note

        >>> n1 = Note("My first note", ["hi", "first"])

        >>> print(n1)
        Note contains: My first note; note tags: ['hi', 'first'], date: 2022-02-24, id = 1.
        """
        return f"Note contains: {self.text}; note tags: {self.tags}, date: {self.creation_date}, id = {self.id}."


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    # n1 = Note("My first note", ["hi", "first"])
    # n2 = Note("Second note")
    # print(n1.match("My first note"))
    # print(n1)
    # print(n2)
