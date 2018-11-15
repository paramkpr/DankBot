from io import BytesIO
from os.path import abspath, split as path_split

from PIL import Image, ImageDraw, ImageFont
from numba import jit
from telegram.ext.dispatcher import run_async

bin_path = path_split(abspath(__file__))[0]
font = ImageFont.truetype(bin_path + '/Resources/raleway.ttf', 32)


@run_async
def brain(update, ts):
	bio = BytesIO()
	bio.name = '%s_%s_%s.png' % (update.message.chat_id, update.message.first_name, update.message.message_id)
	img = Image.open(bin_path + '/Brain/%s.png' % len(ts))
	draw = ImageDraw.Draw(img)

	y = 129
	for i in ts:
		__draw_text(draw, i, y)
		y += 258

	img.save(bio, 'PNG')
	bio.seek(0)
	update.message.reply_photo(photo=bio)


@jit(fastmath=True)
def __get_lines(t):
	w, _ = font.getsize(t)
	if w <= 320:
		return [t]
	t = t.split()
	for i in range(len(t), -1, -1):
		w, _ = font.getsize(" ".join(t[:i]))
		if w <= 320:
			return [" ".join(t[:i])] + __get_lines(" ".join(t[i:]))
	for i in range(len(t[0]), -1, -1):
		w, _ = font.getsize("".join(t[:i]))
		if w <= 320:
			return ["".join(t[0][:i])] + __get_lines(" ".join(["".join(t[0][i:])] + t[1:]))


def __draw_text(draw, t, y):
	t = t.strip()
	w, h = font.getsize(t)

	if w <= 320:
		draw.text((480 - (w / 2), y - (h / 2)), t, (255, 255, 255), font=font)
		return True

	lines = __get_lines(t)
	num_lines = len(lines)
	dims = [font.getsize(x) for x in lines]
	ws, hs = [x[0] for x in dims], [x[1] for x in dims]
	total = sum(hs)

	if total > 258:
		return False

	h = y - (total / 2)
	for i in range(num_lines):
		draw.text((480 - (ws[i] / 2), h), lines[i], (255, 255, 255), font=font)
		h += hs[i]

	return True
