"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!

References:
    https://www.youtube.com/watch?v=EbJtYqBYCV8
    http://www.azlyrics.com/lyrics/plainwhitets/heytheredelilah.html
    http://www.songfacts.com/detail.php?id=6691
=======================================================================
"""

# Instructions: Find and fix the errors in this program so it displays the complete song.
#     Do not delete functions or change the basic structure of the program; just fix it!


def main():
    """Main program to 'sing' each part of the song."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Sing each individual verse/chorus; comment/un-comment these lines as you work.
    title()
    verse1( "New York" )
    verse2()
    chorus1( 4 )
    verse3( "good" )
    verse4()
    chorus2( "4" )
    verse5()
    verse6()
    chorus3( "four" )


def title():
    """Show the title and author of the song."""
    print( 'Hey There Delilah' )
    print( 'by Plain White T's' )
    print( '------------------' )
    print()


def verse1( city ):
    """Sing the first verse.

    :param str city: The city where Delilah currently lives.
    """
    print( "Hey there, Delilah" )
    print( "What's it like in", city "city?" )
    print( "I'm a thousand miles away" )
    print( "But girl, tonight you look so pretty" )
    print( "Yes you do" )
    print( "Times Square can't shine as bright as you" )
    print( "I swear it's true" )
    print()


def verse2():
    """Sing the second verse."""
    print( "Hey there, Delilah" )
    print( "Don't you worry about the distance" )
    print( "I'm right there if you get lonely" )
    print( "Give this song another listen" )
    print( "Close your eyes"
    print( "Listen to my voice, it's my disguise" )
    print( "I'm by your side )
    print()


def chorus1( how_many ):
    """Sing the chorus line the number of times specified.

    :param int how_many: How many times to repeat the line in this singing of the chorus.
    """
    for _ in how_many:
        print( "Oh it's what you do to me" )

    print( "What you do to me" )
    print()


def verse3( adjective ):
    """Sing the third verse.

    :param str adjective: Adjective describing how they'll have it and his word.
    """
    print( "Hey there, Delilah" )
    print( "I know times are getting hard" )
    print( "But just believe me, girl" )
    print( "Someday I'll pay the bills with this guitar" )
    print( "We'll have it", adjective )
    print( "We'll have the life we knew we would" )
    print( "My word is", adgective )
    print()


def verse4( name ):
    """Sing the fourth verse.

    :param str name: The name of the song's title character.
    """
    print( "Hey there,", name )
    print( "I've got so much left to say" )
    print( "If every simple song I wrote to you" )
    print( "Would take your breath away" )
    print( "I'd write it all" )
    print( "Even more in love with me you'd fall" )
    print( "We'd have it all" )
    print()


def chorus2( how_many ):
    """Sing the chorus line at least once, plus how many more specified.

    :param int how_many: How many times to repeat the line in this singing of the chorus.
    """
    for _ in range( 1 + how_many ):
        print( "Oh it's what you do to me" )

    print()


def verse5():
    """Sing the fifth verse."""
    print( "A thousand miles seems pretty far" )
    print( "But they've got planes and trains and cars" )
    print( "I'd walk to you if I had no other way" )
    print( "Our friends would all make fun of us" )
    print( "and we'll just laugh along because we know" )
    print( "That none of them have felt this way" )
    print( "Delilah, I can promise you" )
    print( "That by the time that we get through" )
    print( "The world will never ever be the same" )
    print( "And you're to blame" )
    print()


def verse6():
    """Sing the sixth verse."""
    print( "Hey there, Delilah" )
    print( "You be good and don't you miss me" )
    print( "Two more years and you'll be done with school" )
    print( "And I'll be making history like I do" )
    print( "You'll know it's all because of you" )
    print( "We can do whatever we want to" )
    print( "Hey there, Delilah, here's to you" )
    print( "This one's for you" )
    print()


def chorus3( how_many ):
    """Sing the chorus line at least two times, plus how many more specified.

    :param int how_many: How many times to repeat the line in this singing of the chorus.
    """
    # Convert to int just in case the parameter passed is something unexpected.
    how_many = int( how_many )

    # Now sing the appropriate number of times.
    for _ in range( how_many ):
        print( "Oh it's what you do to me" )

    print( "What you do to me" )
    print()


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()