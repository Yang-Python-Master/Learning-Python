class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # 这个方法决定了：当别人想把你的对象转成字符串时，显示什么内容
    def __str__(self):
        return f"水果：{self.name}, 价格：{self.price}元\n"

# 准备数据
fruit_data = [['香蕉', 5], ['苹果', 6], ['橘子', 7]]

# 写入文件
with open('fruits.txt', 'a', encoding='utf-8') as f:
    for item in fruit_data:
        # 1. 先照着图纸捏出水果
        p = Fruit(item[0], item[1])
        # 2. 把水果转成字符串，写进硬盘
        f.write(str(p)) 

print("水果存好了，去检查下 fruits.txt！")