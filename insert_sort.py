#coding:utf8

"""算法描述：
	1.从第一个元素开始，该元素可以认定已排序
	2.取出下一个元素，在已经排序的元素列表中从后向前扫描
	3.若该元素（已排序）大于新元素，将该元素移至到下一个位置
	4.重复3步骤，直到找到已排序元素小于或者等于新元素
	5.将新元素插入到该位置后
	6.重复步骤2-5
	"""
def insert_sort(data_list):
    for i in range(1, len(data_list)):
        current_element = data_list[i]
        j = i - 1
        while j >=0 and current_element < data_list[j]:
            data_list[j+1] = data_list[j]
            j -= 1
        data_list[j+1] = current_element
    return data_list

if __name__ =="__main__":

	data_list = [7,3,1,24,5,5,6,8,9,0]
	print("原始列表为：%s"%data_list)
	insert_sort(data_list)
	print("排序后新列表为：%s"%data_list)
