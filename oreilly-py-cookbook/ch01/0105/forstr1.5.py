#!/usr/bin/env python
'''
ȥ���ַ������˵Ŀո��ַ��������lstrip��rstrip��strip��������Ϊ����������Ƶġ��⼸������������Ҫ���������ǻ�ֱ�ӷ���һ��ɾ���˿�ͷ��ĩβ�������˵Ŀո��ԭ
�ַ����Ŀ�����
'''

x = '  hej  '
print '|', x.lstrip(), '|', x.rstrip(), '|', x.strip(), '|'

'''
��ʱ����Ҫ���ַ�������һЩ�ո��������Ԥ�ȹ涨�Ĺ̶����ȣ���������Ҷ���
����ж��룬����ʱҲ��Ҫ�������Ƴ����еĿո񣨿հס��Ʊ��������з��ȣ���Python
���ַ������������3���������ṩ���ֹ��ܡ�����ѡ��ȥ�������ַ���ֻ���ṩһ���ַ�����Ϊ��3�������Ĳ���
'''

y = 'xyxxyy hejyx yyx'
print '|'+x.strip('xy')+'|'