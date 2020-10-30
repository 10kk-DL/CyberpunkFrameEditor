# Cyberpunk Frame Editor
# by Flezzo (vk.com/flezzo)
# All rights reserved (no)

from PIL import Image, ImageDraw, ImageFont


def save():
	path = input('\n\tВведите путь сохранения файла (можно не указывать):\n')
	if path == '':
		img.save('cyberpunk_edited.jpg')
		print('\tФайл успешно сохранен в папку с программой.')
	else:
		path = path[:-1] if path.endswith('/') else path
		finalPath = f'{path}/cyberpunk_edited.jpg'
		img.save(finalPath)
		print(f'\tФайл успешно сохранен по пути:\t{finalPath}')

def edit():
	global img
	img = Image.open('photo.png')
	font = ImageFont.truetype('BlenderPro-Book.ttf', 35)
	text = ImageDraw.Draw(img)
	pos = [150, 225]
	print(f'\tДобро пожаловать в Cyberpunk Frame Editor!\n\tЧтобы закончить ввод текста, напишите /end.\n')
	while True:
		userText = input()
		if userText == '/end':
			save()
			return
		value = 0
		for i in userText:
			text.text((pos[0], pos[1]), i, font=font, fill=('#000000'))
			pos[0] += 20
			value += 1
			if value == 85:
				pos[0] = 150
				pos[1] += 50
				value = 0
		pos[0] = 150
		pos[1] += 50

edit()