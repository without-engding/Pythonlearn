#正则表达式：用于表示一组字符串的表达式
'''
python
pythonnnn            =python    +    #用简洁的方式表示，常用于文本处理
pythonnnnnnn          #字符  操作符
                                .表示任何单个字符
                                +表示前一个字符出现1次或多次  python+表示python,pythonnn,pythonnnn等
                                *表示前一个字符出现0次或多次，python*表示python,python,pythonnn等
                                ？表示前一个字符出现0次或1次，Python？表示pytho,python
                                ^表示限定字符串开头，^python表示字符串开头一定是python
                                $表示限定字符串结尾，python$表示字符串结尾一定是python
                                ()表示将多个字符组合起来，pyth(on)+表示python,pythonon
                                []表示指定单个字符的范围，python[ab]表示pythona，pythonb
                                [^]表示排除单个字符的范围，python[^a]
                                {m}表示指定前一个字符出现m次，pyth{2}on表示pythhon
                                {m,n}表示指定前一个字符出现m到n次，pyth{1,2}on表示python，pythhon
                                |表示左右表达式任意一个 python|c++
                                
python\++可以表达python+,python++,python+++,python++++
'''
import re#正则表达式的匹配
#re.search(pattern,      string,       flags=0)#扫描整个字符串并返回成功的匹配
        # 正则表达式，待匹配字符串，控制匹配方式
match=re.search('python+','pythonnnn')
print(match.group())#group方法：返回匹配结果
match=re.search('python+','1989pythonnnn')
print(match.group())
match=re.search('python+','1989pythonnnn2019')
print(match.group())
match=re.match('python+','pythonnnn')
print(match.group())#group方法：返回匹配结果
match=re.match('python+','pythonnnn2019')
print(match.group())