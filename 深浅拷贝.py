#浅拷贝：外层不同，内层相同,copy()
#深拷贝：import copy, copy.deepcopy()
import copy
# l1 = [1, 2, 3]  #深拷贝
# l2 = copy.deepcopy(l1)
# print(l2)
l1 = [1, 2, 3]  #浅拷贝
l2 = l1.copy()
print(l2)
