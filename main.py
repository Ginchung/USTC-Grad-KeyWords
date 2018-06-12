#coding:utf-8

# Analyse the keyword of graduates of USTC, 2018. 
# by Ginchung
# A learner.
# Updated on 2018.6.12

import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import jieba
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
    
    
    imgmask=".\\backgrounds\\bg-deepblue.bmp" # 或者 "bg-skyblue.bmp" 或其他你选用的图片作为轮廓背景(Mask)
    seg=jieba.cut(string)
    seg_space=' '.join(seg)
    
    pic_mask=imread(imgmask)
    
    #wordcloud默认不支持中文，这里的font_path需要指向中文字体，不然得到的词云全是乱码
    wc=WordCloud(font_path='msyh.ttc',max_words=700,background_color='white',mask=pic_mask,max_font_size=100,font_step=1).generate(seg_space)
    imagecolor=ImageColorGenerator(pic_mask)
    plt.imshow(wc.recolor(color_func=imagecolor))
    plt.axis("off")
    wc.to_file(".\\Results\\"+req+"-db"+".jpg")

def main():
    list=["1","2","3","4","5"]
    for i in list:
        genPic(i)

main()
