# Help Responses
commands = '''
*Basic Commands*
 1. Hmmm
 2. Allah hu Akbar
 3. Do it
 4. Nein
 5. Damnnn
 6. E
 7. Hello there
 8. I don't think so
 9. Wut / Dude what / What even
10. Wat
11. What the
12. Miss me with that gay shit
13. Ironic
14. F / RIP
15. ???

*Advanced Commands*

1. ABC, not XYZ
	Generates a meme using either the Robbie Rotten, Babushka, or Drake template in which ABC is chosen over XYZ.

2. Alt:
	Converts text that follows the colon to aLt CaSe.

3. Vapourize:
	Converts text that follows the colon to Vapourwave text.
	
4. 🅱️:
	Replaces the first consonant group of a word with 🅱️.
	Doesn't replace those consonants which can (mostly) be pronounced after a b.

5. Alexa / Dankbot play Despacito
	Sends a GIF of the Despacito music video along with an audio file of Despacito.
	The audio file has a 10% chance of being extremely bass boosted.


Use */help* to print all commands and */cookbook* for frying help.
'''
cookbook = '''
*Deep Fryer*
Fries images, GIFs, or videos.
This includes increasing saturation & contrast, and adding noise, emojis, lazer eyes, and bulges.
To invoke, reply to a message containing an image, GIF, or video using one of the following commands:

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

Also note that emojis and bulges are disabled by default for GIFs and Videos.
Use No-fat, Low-fat, or High-fat and Light / Heavy to enable them as needed.


Use */help* to print all commands and */cookbook* for frying help.
'''

# Vapourwave Text
normal = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`-=~!@#$%^&*()_+[];',./{}:"|<>?'''
vapour = '''ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０`－＝~！＠＃＄％^＆＊（）_＋[]；＇，．／{}："|<>？'''
vapourtext = {normal[x]: vapour[x] for x in range(len(normal))}
vapourtext[' '] = '   '

# B-ify
bs = '🅱️bcdfgjkmnpqtvwx'
exbuded = ['a', 'an', 'and', 'are', 'if', 'the']

# Misc.
chars = 'abcdefghijklmnopqrstuvwxyz'
keys = ['shallow', 'deep', 'no-fat', 'low-fat', 'high-fat', 'light', 'heavy']
ironic = '''
Did you ever hear the tragedy of Darth Plagueis The Wise?
I thought not. It's not a story the Jedi would tell you.
It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith,
so powerful and so wise he could use the Force to influence the midichlorians to create life…
He had such a knowledge of the dark side that he could even keep the ones he cared about from dying.
The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful…
The only thing he was afraid of was losing his power, which eventually, of course, he did.
Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
Ironic. He could save others from death, but not himself.
'''.replace('\n', ' ')
