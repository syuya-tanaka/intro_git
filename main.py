# こちらmain.pyでございます
print("Hello World2")

# 変更を加える

f = ["asdf", "asdfe", "sdf"]
if "aaa" not in f:
    print("eeeeeeeeeee")


class Sample():
    def sample(self):
        self.x = 'eieie'


class SSample(Sample):
    def sample(self):
        super().sample()
        print(self.x)

xx = SSample()
xx.sample()

# 変更部分の追加
