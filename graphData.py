import numpy as np
import matplotlib.pyplot as plt

filename = 'testData/tree_data_farach_mbp_random_data_varying_alphabet'
title = 'SOME TITLE'
xlabel = 'length of input'
ylabel = 'construction time in seconds'
outputimgfile = 'fig3.png'

def plot(filename, label, color):
	global ax
	x  = []
	y = []
	minmax = []
	temp = []
	temp_x = 0
	with open(filename, "rb") as fp:
		for line in fp.readlines():

			tup = line.split(b",")
			x_n = float(tup[0].decode())
			time = float(tup[1].decode())
			if x_n == temp_x:
				temp.append(time)
				
				minmax[-1] = (min(time, minmax[-1][0]),max(time, minmax[-1][1]))
				continue
			if temp_x != 0:
				temp.sort()
				y.append(temp[int(len(temp)/2)])
				temp = []

			temp_x = x_n
			temp.append(time)
			x.append(x_n)
			minmax.append((time,time))
	temp.sort()
	y.append(temp[int(len(temp)/2)])

	plt.plot(x,y, marker='o', markersize=3, color=color, label=label)
	l1, l2 = zip(*minmax)
	# ax.fill_between(x, [y/x for x,y in zip(x, l1)], [y/x for x,y in zip(x, l2)], hatch="////", color="#55AA55", linewidth=0.0, alpha=0.5)
	ax.fill_between(x, l1, l2, hatch="////", color=color, linewidth=0.0, alpha=0.5)

# plt.yscale('log')
# plt.grid(True)

fig, ax = plt.subplots()
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.grid(True)

plot(filename, "test", "green")


legend = ax.legend(loc='upper right', shadow=True)

frame = legend.get_frame()
frame.set_facecolor('0.90')


for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
     label.set_linewidth(1.5)  # the legend line width

fig.savefig(outputimgfile, bbox_inches='tight')
