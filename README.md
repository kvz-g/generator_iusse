# Generator_iusse

  我在学习python中generator的过程中，定义一个生成器，生成seq的全部可能的排列组合。在函数gen_perms_v1的实现方式下（也是我开始采用的方式），OJ一直不通过，但在我Debug的过程中，我使用for循环，print输出generator结果，发现结果是正确的。而后我查看OJ判断的标准是采用了print(sorted(generator))的方式，进而发现sorted函数会输出与for循环不同的结果(详细请运行一下main.py）。在网上查询后，并未得出结论。但修改最后插入操作的实现后(即main中gen_perms_v2)，两种方式输出又一致了。

## 函数实现思想
  将seq第一个元素插入到剩余元素的所有可能的排列组合中的每个间隔中，用递归的方式实现。

## PS
我只是一个新手，实在是不知道为什么会出现这样的情况，按常理说输出应该一致，这是sorted函数和list method有什么奇怪的联动吗？求一个解释。
PPS
题目来源：cs61a 2022 Fall homework05
