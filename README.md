This script takes a list of characters from a novel or other manuscript, reads
the text file of that manuscript, and prints a Seaborn
univariate chart (distribution and rug chart) for the incidences of each character's name in the text.

# Installing

Get the code:

    $ git clone https://github.com/BenQuigley/char_counter/
    $ cd char_counter

Install pandas, matplotlib, and seaborn:

    $ pip install -r REQUIREMENTS.txt

# Using

Before using the code, edit the user_config file to indicate the name of the text, the location of the text
file, and the list of characters' names. Each characters' name can be a single name, or a list of their various
names. This example shows how the file can be configured for the novel *Siddhartha*:

    user_config = {
        'book title': "Siddhartha",
        'text file': 'siddhartha/siddhartha.txt',
        'character names': ['Siddhartha',
                            'Govinda',
                            ["Siddhartha's father", 'father'],
                            ['Guatama', 'Buddha'],
                            'Kamala',
                            'Kamaswami',
                            'Vasudeva',
                             ]
    }

Once the user config file is updated, the script can be run with:

    python main.py