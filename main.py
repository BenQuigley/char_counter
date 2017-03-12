import matplotlib.pyplot as plt
import seaborn as sns
import itertools

from user_config import *

class Character():
    
    def __init__(self, names):

        # Create a character with a list of their names. Ex.
        # potter = Character('Harry', 'Harry Potter', 'the boy who lived')

        self.names = names
        self.name = names[0]
        self.line_mentions = []

    def count_mentions(self, text):

        # For each line, search it for the character's names.

        for i, line in enumerate(text):
            for name in self.names:
                if name.lower() in line.lower():
                    self.line_mentions.append(i)
                    break
        print("{}'s line mentions: {}".format(self.name, self.line_mentions))


class Book():

    def __init__(self, name):
        self.name = name
        self.chars = []

    def get_text(self, location):

        # Read the text of the book to a list of lines.

        with open(location, 'r') as infile:
            self.text = [line for line in infile]
        self.length = len(self.text)

    def add_chars(self, lists):

        # Add the characters in the book.

        for names in lists:

            # Handle either a single name string, or a list of name strings for
            # characters with many names such as:
            # vol = Character(['Voldemort',  'Tom Riddle', 'he who must not be named'])

            if type(names) == list:
                char = Character(names)
            elif type(names) == str:
                char = Character([names])
            char.count_mentions(self.text)
            self.chars.append(char)

    def show_mentions(self):

        # Create a plot for each character's line mentions.

        plots = len(self.chars)
        rows = int(plots/3)+1
        plt.figure('Distribution of Character Mentions in {}'.format(self.name))
        palette = itertools.cycle(sns.color_palette('muted'))
        i = 0
        for char in self.chars:
            if char.line_mentions:
                plt.subplot(rows, 3, i+1)
                mentions = char.line_mentions
                ax = sns.distplot(mentions, hist=False, rug=True, kde_kws={"shade": True},
                             color=next(palette),
                             )
                plt.title(char.name)
                ax.set(xlim=(0, self.length))
                ax.set(ylim=(0, .00140))
                ax.set(yticklabels=[])
                i += 1
        plt.show()

def main():
    saga = Book(user_config['book title'])
    saga.get_text(user_config['text file'])
    saga.add_chars(user_config['character names'])
    saga.show_mentions()

if __name__ == '__main__':
    main()