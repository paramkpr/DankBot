# Help Responses
commands = '''
*Basic Commands*
 1. Hmmm
 2. Allah hu Akbar
 3. Just do it
 4. Nein
 5. E
 6. Hello there
 7. I don't think so
 8. Wut / Wat / Dude what / What even / What the
 9. Miss me with that gay shit
10. Ironic
11. F / RIP
12. ???

*Advanced Commands*

1. ABC, not XYZ
	Generates a meme using either the Robbie Rotten, Babushka, or Drake
	template in which ABC is chosen over XYZ.

2. Alt:
	Converts text that follows the colon to aLt CaSe.
	Deletes the trigger message if given admin rights.

3. Vapourize:
	Converts text that follows the colon to Vapourwave text.
	Deletes the trigger message if given admin rights.
	
4. 🅱️
	Replaces the first consonant group of a word with 🅱️.
	Doesn't replace those consonants which can (mostly) be pronounced after a b.

5. Alexa / Dankbot play Despacito {x}
	Sends a GIF of the Despacito music video
	along with an audio file of Despacito.
	If a number x is given, certain effects are applied to the audio.
	If not, the audio file has a 10% chance of being extremely bass boosted.
	
6. T: ABC B: XYZ
	Reply to an image to create a meme.
	ABC is the top-text and XYZ is the bottom-text.
	By default, the captions are converted to upper case.
	Replace T with Ts and B with Bs to keep case as it is.


Please note, DankBot needs permission to access messages to work properly.
For additional functionality, such as removing certain trigger messages
after responding, the Bot needs to be an admin on the group.
Admin rights are optional and may be toggled at your discretion.

Use */help* to print commands and */cookbook* for frying help.
'''
cookbook = '''
*Deep Fryer*
Fries images, GIFs, or videos (Experimental).
This includes increasing saturation & contrast,
and adding noise, emojis, lazer eyes, and bulges.

To invoke, reply to a message containing an image, GIF, or video
using one of the following commands:

	a) Fry: 1 cycle of frying.
	b) Nuke: 3 cycles of frying.
	c) Allah hu Akbar: 5 cycles of frying.
	d) Tsar Bomba: 10 cycles of frying.

	Additional parameters (Include in the same message):

	a) Deep: High contrast and saturation increase.
	b) Shallow: Low contrast and saturation increase.

	c) High-fat: Emojis are increased.
	d) Low-fat: Emojis are reduced.
	e) No-fat: Emojis aren't added.

	f) Heavy: Extra bulges are added.
	g) Light: No bulges are added.
	
	h) Vitamin-B: (Experimental) Adds the B emoji on text in the image.
	i) Chilli: (Experimental) Adds laser eyes.

Also note that emojis and bulges are disabled by default for GIFs and Videos.
Use No-fat, Low-fat, or High-fat and Light / Heavy to enable them as needed.


Use */help* to print commands and */cookbook* for frying help.
'''
changes = '''
19 Feb 2019

- GIF fryer functionality is more or less stable.
- Added /changes command.


18 Feb 2019

- Bot now deletes alt: and vapourize: triggers when granted admin rights.
'''
# Vapourwave Text
normal = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890''' \
	+ '''`-=~!@#$%^&*()_+[];',./{}:"|<>?'''
vapour = '''ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ''' \
	+ '''ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０''' \
	+ '''''''`－＝~！＠＃＄％^＆＊（）_＋[]；＇，．／{}："|<>？'''
vapourtext = {normal[x]: vapour[x] for x in range(len(normal))}
vapourtext[' '] = '   '

# B-ify
bs = '🅱️bcdfgjkmnpqtvwx'
exbuded = ['a', 'an', 'and', 'are', 'if', 'the']

# Misc.
chars = 'abcdefghijklmnopqrstuvwxyz'
keys = [
	'shallow', 'deep',
	'no-fat', 'low-fat', 'high-fat',
	'light', 'heavy',
	'chilli',
	'vitamin-b'
]

ironic = '''
Did you ever hear the tragedy of Darth Plagueis The Wise?
I thought not. It's not a story the Jedi would tell you.

It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith,
so powerful and so wise he could use the Force
to influence the midichlorians to create life…

He had such a knowledge of the dark side that
he could even keep the ones he cared about from dying.

The dark side of the Force is a pathway to many abilities
some consider to be unnatural. He became so powerful…

The only thing he was afraid of was losing his power,
which eventually, of course, he did.

Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep.

Ironic. He could save others from death, but not himself.
'''.replace('\n', ' ')
