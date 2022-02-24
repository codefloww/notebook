"""module that implements Notebook program"""
from note import Note


class Notebook:
    def __init__(self, notes: list = []) -> None:
        """constructor for Notebook class

        Args:
            notes (list): list of objects of class Note

        >>> notebook = Notebook()

        """
        self.notes = notes

    def search(self, filter: str) -> list:
        """filters notes by filter in tags or text

        Args:
            filter (str): substring to search for

        Returns:
            list: list of notes

        >>> notebook = Notebook([Note('my first note',['tag'])])

        >>> len(notebook.search('tag'))
        1
        """
        proper_notes = []
        for note in self.notes:
            if note.match(filter):
                proper_notes.append(note)
        return proper_notes

    def new_note(self, memo: str, tags: list = []) -> None:
        """adds note to notebook

        Args:
            memo (str): text of the new note
            tags (list, optional): tags for a new note. Defaults to [].

        >>> notebook = Notebook()

        >>> notebook.new_note("new note", ['tag'])

        """
        new_note = Note(memo, tags)
        self.notes.append(new_note)

    def modify_memo(self, note_id: int, memo: str) -> None:
        """modifies certain note in notebook

        Args:
            note_id (int): id of the note
            memo (str): new text of the note

        >>> notebook = Notebook([Note('my first note',['tag'])])

        >>> notebook.modify_memo(0, 'some new text')

        """
        correct_id = False
        for note in self.notes:
            if note.id == note_id:
                note.text = memo
                correct_id = True
                break
        if not correct_id:
            print("No note with such id")

    def modify_tags(self, note_id: int, tags: list) -> None:
        """modifies tags of the certain note

        Args:
            note_id (int): note's id in the notebook
            tags (list): list of new tags for the note

        >>> notebook = Notebook([Note('my first note',['tag'])])

        >>> notebook.modify_tags(1, ['new', 'tags'])

        """
        correct_id = False
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                correct_id = True
                break
        if not correct_id:
            print("No note with such id")


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
