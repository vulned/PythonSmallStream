from collections import deque  # 少量使用mod中的变量、方法
import collections as cls  # 大量使用mod中的变量、方法
# from collections import *  # 不建议：*内容过多，变量、方法极易混淆

queue01 = deque(["YuanShuai", "MaoZedong", "Eric"])
queue02 = cls.deque(["YuanShuai", "MaoZedong", "Eric"])

print(queue01)
print(queue02)