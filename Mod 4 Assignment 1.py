
# [ 1 ]define (def) a simple function called yell_it() and call the function. The function should be your name in all caps, Call the function.
def yell_it():
    print("Brayden!".upper())
yell_it()


#[2 ]create a function that prints your favorite song and its lyrics. Call the function
def favorite_song():
    print("My favorite song is 'Clutch Kick' by kiLLa Laharl. The lyrics are: 'Look me in my eyes, let me bleed and now you gonna wait Caught me in my mind, light a blunt, know what you wanna say Cocaine in the line, shoot the clip, I waste another day Fuck me in the night, come another day, she on the way Pull up on your block then I slide through when I come through going in with a clutch kick I ran them with a Glock, see the one two, what you gon' do with this big .40 drumstick? I pull up on your block, shoot your whole crew, see the tattoo then you know, get your wig split Don't running with the flock, now you all knew when I come through dig a hole get a kill slit And now I done handful of shots, need my Hennessy I can't feel my head, damn I feeling like Lil Kennedy I can't sell my soul to another one of my enemy I can't be my own when I'm wasted on ketamine Look me in my eyes, let me bleed and now you gonna wait Caught me in my mind, light a blunt, know what you wanna say Cocaine in the line, shoot the clip, I waste another day Fuck me in the night, come another day, she on the way Look me in my eyes, let me bleed and now you gonna wait Caught me in my mind, light a blunt, know what you wanna say Cocaine in the line, shoot the clip, I waste another day Fuck me in the night, come another day, she on the way Riding round town in a Gelik with a top rim high beam paint it all black Never old yet for the Bentley, drop the top off, come in with a new track Back of the club, shawty come in liquor on me, 21 on my blackjack Back of the car, got a truck all full of cash, counting on with a new stack What you want now? I ain't spare your life hoe, shut up and take the last shot What you want now with your eyes all open? See you go with a dead knot You ain't make it out here, see the red dot, headshot Riding round town with my name, now your man die Look me in my eyes, let me bleed and now you gonna wait Caught me in my mind, light a blunt, know what you wanna say Cocaine in the line, shoot the clip, I waste another day Fuck me in the night, come another day, she on the way Look me in my eyes, let me bleed and now you gonna wait Caught me in my mind, light a blunt, know what you wanna say Cocaine in the line, shoot the clip, I waste another day Fuck me in the night, come another day, she on the way'")

# [ 3.1] define/create a function called yell_this()
# [ 3.2] get user input in the variable words_to_yell
#[ 3.3]in the function print() the variable is all caps
# [3.4 ] call yell_this function with words as argument
def yell_this(words_to_yell):
    print(words_to_yell.upper())
words_to_yell = input("Enter some words to yell!")
yell_this(words_to_yell)
