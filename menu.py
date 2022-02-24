"""module for UI of the notebook"""
from notebook import Notebook
import abc
import sys


class Menu(Notebook):
    """Abstract class for the interface that the
    user has to work with notebooks and notes.
    """

    def __init__(self, notebook=None, choices={}):
        """Initializes a menu with an empty notebook
        and the options available to work with it.
        """
        self.notebook = notebook
        self.choices = choices
        pass

    @abc.abstractmethod
    def display_menu(self):
        """Displays the menu to the user.
        Returns the choice as string.
        """
        pass

    @abc.abstractmethod
    def display_notes(self):
        """Displays the notes to the user."""
        pass

    @abc.abstractmethod
    def search(self):
        """Asks the user for a search pattern.
        Displays any matching note found.
        """
        pass

    @abc.abstractmethod
    def new_note(self):
        """Modifies the text and tags for a note."""
        pass

    @abc.abstractmethod
    def modify_note(self):
        """Modifies the text and tags for a note."""
        pass

    def run(self):
        """Display the menu and respond to choices"""
        while True:
            choice = self.display_menu()
            if choice in self.choices:
                action = self.choices[choice]
                print("{0} is a valid choice".format(choice))
                action()
            else:
                print("{0} isn't a valid choice".format(choice))

    def quit(self):
        """Exit from the notebook."""
        print("Exiting")
        sys.exit()


class CommandOption(Menu):
    """A class that provides a command line interface for the menu."""

    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1": self.display_notes,
            "2": self.search,
            "3": self.new_note,
            "4": self.modify_note,
            "5": self.quit,
        }
        Menu.__init__(self, self.notebook, self.options)

    def display_menu(self):
        """Displays the menu to the user.
        Returns the choice as string.
        """
        print(
            """
        Notebook Menu
        
        1. Display All Notes
        2. Search For Notes
        3. Add New Note
        4. Modify Note
        5. Quit
        """
        )
        return input("Enter an option: ")

    def display_notes(self):
        """Displays the notes to the user."""
        for note in self.notebook.notes:
            print("\n{0}".format(note))

    def search(self):
        """Asks the user for a search pattern.
        Displays any matching note found.
        """
        search_string = input("\nEnter the filter to search for: ")
        matching_notes = self.notebook.search(search_string)
        print(
            'There are {0} notes matching the filter "{1}":'.format(
                len(matching_notes), search_string
            )
        )
        for note in matching_notes:
            print("\n{0}".format(note))

    def new_note(self):
        """Modifies the text and tags for a note."""
        note_text = input("\nEnter the text for the note: ")
        note_tags = input("Enter tags for the note with spaces: ")
        self.notebook.new_note(note_text, note_tags.split())
        print("Note has been added")

    def modify_note(self):
        """Modifies the text and tags for a note."""
        try:
            note_id = int(input("\nEnter a note id: "))
            note_text = input("\nEnter the text for the note: ")
            note_tags = input("Enter tags for the note: ").split()
            if note_text:
                self.notebook.modify_memo(note_id, note_text)
            if note_tags:
                self.notebook.modify_tags(note_id, note_tags)
        except:
            print("Invalid id number")


if __name__ == "__main__":
    cm = CommandOption()
    cm.run()
