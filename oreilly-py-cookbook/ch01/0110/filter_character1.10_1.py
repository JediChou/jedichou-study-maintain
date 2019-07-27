#!/usr/bin/env python
'''
1.10_1Unicode字符串过滤字符串中不属于指定集合的字符
'''
import sets
class Keeper(object):
    def __init__(self, keep):
        self.keep = sets.Set(map(ord, keep))
    def __getitem__(self, n):
        if n not in self.keep:
            return None
        return unichr(n)
    def __call__(self, s):
        return unicode(s).translate(self)
makefilter = Keeper
if __name__ == '__main__':
    just_vowels = makefilter('aeiouy')
    print just_vowels(u'four score and seven years ago')
    print just_vowels(u'tiger, tiger burning bright')
