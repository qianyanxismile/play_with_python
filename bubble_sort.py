# coding:utf-8

def bubble_sort(alist):
	# 结算列表长度
	n = len(alist)
    # 外层循环控制从头到尾的次数
	for j in  range(n-1):
		# 用一个count记录一共交换的次数，可以排除已经排好的序列
		count = 0
		# 内层循环控制走一次的过程
		for i in range(0,n-1-j):
			# 如果前一个元素大于后一个元素，则交换两个元素（升序）
			if alist[i]>alist[i+1]:
				# 交换元素
				alist[i],alist[i+1] = alist[i+1],alist[i]
				# 记录交换次数
				count += 1
				
		# count == 0代表没有交换
		if 0 == count:
		    break


if __name__ =="__main__":
	alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
	print ("原列表为：%s"%alist)
	bubble_sort(alist)
	print ("排序后列表为：%s"%alist)