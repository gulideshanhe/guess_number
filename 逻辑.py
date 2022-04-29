import random
import sys

num = random.randint(1, 500)
print(num)
i = 0
names = []


class People:
	def __init__(self, all):
		self.People_Times = 0
		self.People_All = all

	def add_one(self):
		self.People_Times += 1

	def print_times(self):
		return self.People_Times


def out():
	try:
		a = eval(ui.tuess.text())
	except:
		ui.end.setText("非法输入！")
	global i
	global num
	if a > num:
		ui.end.setText("猜测数据较大，猜小一点")
		names[i].add_one()
	elif a < num:
		ui.end.setText("猜测数据较小，猜大一点")
		names[i].add_one()
	else:
		print(i)
		if i < names[0].People_All - 1:
			ui.end.setText("猜中了!\n请下一位玩家继续")
			i += 1
			num = random.randint(1, 500)
			print(num)
		else:
			ui.end.setText("游戏结束！")
			ui.times.setDisabled(True)
			ui.sure.setEnabled(False)
			ui.tuess.setDisabled(True)
			times = {}
			for time in range(i + 1):
				times[f"{time}号"] = names[time].print_times()
			times = sorted(times.items(), key = lambda x: x[1], reverse = False)
			results = ""
			for times_list in times:
				results += f" {times_list[0]}"
			# result = " ".join(results)
			ui.result.setText(results)
			ui.begin.setText("再来一局")
			ui.begin.setEnabled(True)
			ui.people.setReadOnly(False)
			ui.people.clear()

	ui.times.setText(str(names[i].print_times()))
	ui.tuess.clear()


def begin():
	try:
		people = eval(ui.people.text())
	except:
		ui.people.setText("非法输入！")
	ui.end.setText("游戏开始！")
	ui.result.setText("等待游戏结束")
	ui.times.setReadOnly(True)
	ui.times.setText("0")
	global names
	for name_times in range(people):
		names.append(name_times)
		names[name_times] = People(people)
	ui.people.setReadOnly(True)
	ui.tuess.setDisabled(False)
	ui.times.setDisabled(False)
	ui.sure.setEnabled(True)
	ui.begin.setEnabled(False)


def view():
	import ui_untitled as name
	app = name.QApplication([])
	MainWindow = name.QWidget()
	# MainWindow.move(0, 0)  # 定义初始位置
	global ui
	ui = name.Ui_Form()
	ui.setupUi(MainWindow)
	ui.sure.setEnabled(False)
	ui.end.setReadOnly(True)
	ui.times.setDisabled(True)
	ui.result.setReadOnly(True)
	ui.tuess.setDisabled(True)
	ui.times.setDisabled(True)
	ui.begin.clicked.connect(begin)
	ui.sure.clicked.connect(out)
	ui.exit.clicked.connect(sys.exit)
	MainWindow.show()
	app.exec()


if __name__ == '__main__':
	view()