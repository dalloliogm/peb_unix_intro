

class TutorialMessage:
    '''
    Define a tutorial message

    Using a class is a bit more organized than a dictionary,
    because we make sure that each element has the same structure
    '''
    def __init__(self, label, text, minline=12, maxline=None):
        self.label      = label
        self.text       = text
        self.minline    = minline
        self.maxline    = maxline

tutorial_messages = [
        TutorialMessage(['start', ' start ', ' start', 'start '], """
 ______________________________
/ Congrats!                    \  
|  You've used grep correctly, |
\  and found a cow.            /
 ------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||



The command grep allows to search
for a pattern in a text file.

It will print all the matching 
lines to the screen.
"""),
        TutorialMessage(['stOLDart', ' stOLDart ', ' stOLDart', 'stOLDart '], """
 ______________________________
/ Congrats!                    \  
|  You've used grep correctly, |
\  and found a cow.            /
 ------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||



The command grep allows to search
for a pattern in a text file.

It will print all the matching 
lines to the screen.

=================
Next Exercise
=================

In the next exercise we will see 
how to access grep's documentation.

Grep the following word to continue:
  _            _        
 | |          | |       
 | |__    ___ | | _ __  
 | '_ \  / _ \| || '_ \ 
 | | | ||  __/| || |_) |
 |_| |_| \___||_|| .__/ 
                 | |    
                 |_|  

"""),
    TutorialMessage(['help', ' help ', 'help '], """
The documentation for grep can 
be accessed through man:

    $: man grep

Scroll down to see all the 
parameters for grep and their description.

Use / to search for text.
Press the q key to exit.



==============
Next exercise
==============

For the next exercise, you will need to open 
grep's documentation and identify two options:

- the option for case-insensitive searches
- the option for counting 
  the number of matching lines, 
  instead of printing them to the screen.

Once you have identified these options, 
do a case-insensitive search on this file for the word 
"ignorecase", then count the number of lines.

    """, minline=57, maxline = 178
    ),
    TutorialMessage('ignorecase', '''
        
Remember that, to continue with the exercise, 
you need to do a case-insensitive search for the word''', maxline=20),
    TutorialMessage(['ignOrecase', 'ignorecase', 'IgnorEcase', 'IGNORECASE'], '''
 _____________
/ Good Job!   \ 
| You did a   |
| case-insens |
| itive       |
\ search      /
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||


    ''', minline=185),
    TutorialMessage('21', '''

 ____________________
/ Congrats! Yes      \ 
| the answer to the  |
| case-insensitive   |
| and count question |
| is 21.             /
 --------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\  
                ||----w |
                ||     ||

=============
Next topic
=============

We are going to make a break from
the exercises to talk about the Unix
piping system. 

This will also help you reading this
output more easily, by piping it into
another Unix command such as less or
head. 

For example, try 
$: grep 21 2_searching_patterns.txt | less

to read this output easily.

The output of grep can be very long, and it may be
difficult to read it all on the screen without
redirecting it. 

The same applies to other Unix commands - in general,
redirecting the output to less makes it easier to read.

    '''), 
    TutorialMessage('file32', '''

Regular Expressions allow to identify complex pattern.

The folder genes/ contains a sequence file called sequences.fasta

==============
Next Exercise
==============

- Use grep on the file genes/sequences.fasta
- You will need to identify the grep option for 
    printing one line above of the match 
    (see man grep)
- Search for AAA, followed by any two characters, 
    then TTT.
    '''),
    TutorialMessage('secrets','''
 _____________
( There are   )
( no secrets  )
( in this     )
( tutorial, I )
( swear       )
 -------------
        o   ^__^
         o  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||
'''),
    TutorialMessage('randomcow','''
 _____________
( This is     )
( just a      )
( random cow, )
( to add      )
( complexity  )
( to the file )
 -------------
        o   ^__^
         o  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||
'''),
    TutorialMessage('bored','''
 _________________
( If you finished )
( the exercises   )
( early, you can  )
( have a look at  )
( the scripts     )
( folder. Please  )
( be quiet        )
 -----------------
        o   ^__^
         o  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||
''')

    ]

multiplefiles_message = TutorialMessage('regex', '''

Good! You've found the 
file containing the word "regex"

To continue, 
grep file32 2_searching_patterns.txt

''')


dnamessage = TutorialMessage(['AAActTTT', 'AAAccTTT', 'AAAaaTTT', 'AAAgtTTT'], '''
 ________________
/ Congrats! This \  
| was the last   |
\ grep exercise  / 
 ----------------
        \   ^__^
         \  (oo)\_______
             (__)\       )\/\  
                ||----w |
                ||       ||
''')
