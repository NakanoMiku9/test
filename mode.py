# import random
#
# a = []
# for i in range(4):
#     b = random.randint(0, 59)
#     a.append(b)
# print(a)
# dict = {}
# for key in a:
#     dict[key] = dict.get(key, 0) + 1
# print(dict)
# a1 = sorted(dict.items(), key=lambda x: x[0])
# print(a1)
# # namelist=["蔡智","郭小东","胡成安","位鹏飞","康锦波","吴长鑫","李子谦",
# #       "朱玲慧","朱振宇","马之秋","米杰辉","田超","赵世煊","祝欢",
# #       "陈航","徐文豪","王汉文","朱鑫鑫","吴昊霖","李治豪","黄子豪",
# #       "熊宇昆","陈子豪","赵梦良","宗顺","李文程","王浩","钱政","刘晨曦",
# #       "游旭","余源浩","熊丹","朱杰","朱健","张新健","黄庆强","严妍",
# #       "田一聪","柯于永","贺兴威","刘港","王梓成","聂圣才","郑重",
# #       "贾国庆","吴书豪","李森","吴浩然","王星伟","胡家旺","孙飞燕",
# #       "乐昕媛","赵恒创","杨文杰","曾令洪","杨跃","赵金浩","谢亚东",
# #       "李黎明","黎慈庆"]
# # print(namelist[60])



def Sorted(v):
    t = v[::]
    r = []
    while t:
        tt = min(t)
        r.append(tt)
        t.remove(tt)
    return r
print(d)
sorted(5)
