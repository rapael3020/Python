Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> score = [60,61,16,55,99]
>>> name = 0
>>> for scores in score:
	name = name + 1
	if score >= 60:
		print("%d번 학생은 합격입니다." %name)
	else:
		print("%d번 학생은 불합격입니다." %name)
	