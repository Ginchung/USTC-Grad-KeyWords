#coding:utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from scipy.misc import imread

def genPic(req):
    begin=0
    search=""
    if(req=="1"):
        begin=67
        search+="有哪些？<br>"
    elif(req=="2"):
        begin=58
        search+="哪几门：<br>"
    elif(req=="3"):
        begin=49
        search+="教师是：<br>"
    elif(req=="4"):
        begin=63
        search+="建议？<br>"
    elif(req=="5"):
        begin=53
        search+="是什么？<br>"
    end=-5
    
    with open('content.txt','r') as f:
        text=f.readlines()
    
    string="";
    for i in text:
        if(search in i):
            string+=i[begin:end]
    
    
    imgmask="bg-deepblue.bmp" # 或者 "bg-skyblue.bmp" 或其他你选用的图片作为轮廓背景(Mask)
    seg=jieba.cut(string)
    seg_space=' '.join(seg)
    
    alice_color=imread(imgmask)
    
    #wordcloud默认不支持中文，这里的font_path需要指向中文字体，不然得到的词云全是乱码
    wc=WordCloud(font_path='msyh.ttc',max_words=700,background_color='white',mask=alice_color,max_font_size=100,font_step=1).generate(seg_space)
    imagecolor=ImageColorGenerator(alice_color)
    plt.imshow(wc.recolor(color_func=imagecolor))
    plt.axis("off")
    wc.to_file(req+"-db"+".jpg")

def main():
    list=["1","2","3","4","5"]
    for i in list:
        genPic(i)

main()
