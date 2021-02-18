def rbarea():  #點選area選項按鈕後處理函式
    global sitelist, listradio
    sitelist.clear()  #清除原有site list
    for r in listradio:  #移除原有site選項按鈕
        r.destroy()
    n=0
    for c1 in data["sarea"]:
        #逐一取出選取area的site
        if(c1 == area.get()):
            sitelist.append(data.ix[n, 3])
        n += 1    
    sitemake()  #建立site選項按鈕
    rbSite()  #顯示ubike訊息

def rbSite():  #點選site選項按鈕後處理函式
    n = 0
    for s in data.ix[:, 3]:  #逐一取得site
        if(s == site.get()):  #取得點選的站名
            sbi = data.ix[n, 12]  
            bemp=data.ix[n,"bemp"]
            des=data.ix[n,"ar"]
            result.set(s + "站"+"\n"+"可借的車數為：" + str(sbi) +"\n"+"可還的空位數為："+str(bemp)+"\n"+"地址："+des)
            break  #找到點選站名就離開迴圈
        n += 1
    
def clickRefresh():  #重新讀取資料
    global data
    data = pd.read_csv("http://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=csv")
    rbSite()  #更新站名資料

def sitemake():  #建立站名選項按鈕
    global sitelist, listradio
    for i in range(0,7):    #7列選項按鈕
        for j in range(0,5):  #每列5個選項按鈕
            n=i*5+j
            if(n<len(sitelist)):
                site1=sitelist[n]
                #建立選項按鈕
                rbtem = tk.Radiobutton(frame2, text=site1, variable=site, value=site1, command=rbSite, font=("新細明體", 10),bg='white')  
                #加入選項按鈕串列
                listradio.append(rbtem)  
                #設定選項按鈕位置
                rbtem.grid(row=i, column=j)  
                if(n==0):
                    rbtem.select()

def ShowInfo():
    data=pd.read_csv("http://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=csv")
    a=b=c=d=e=f=g=h=0
    for i in range(len(data)):
      if (data['sarea'][i]=="八德區"):
        a+=data['sbi'][i]
      if (data['sarea'][i]=="大園區"):
        b+=data['sbi'][i]
      if (data['sarea'][i]=="大溪區"):
        c+=data['sbi'][i]
      if (data['sarea'][i]=="中壢區"):
        d+=data['sbi'][i]
      if (data['sarea'][i]=="平鎮區"):
        e+=data['sbi'][i]
      if (data['sarea'][i]=="桃園區"):
        f+=data['sbi'][i]
      if (data['sarea'][i]=="龜山區"):
        g+=data['sbi'][i]
      if (data['sarea'][i]=="蘆竹區"):
        h+=data['sbi'][i]
    
    x = { '八德區': a, '大園區': b, '大溪區': c, '中壢區': d,
        '平鎮區': e, '桃園區': f, '龜山區': g, '蘆竹區': h}
    
    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(x)]
    
    p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@country: @value")
    
    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='country', source=data)
    show(p)
    
    
import pandas as pd
import tkinter as tk
from math import pi
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum

#匯入API
data=pd.read_csv("http://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=csv")

#建立UI網頁
win=tk.Tk()
win.configure(background="white")
win.geometry("750x470")
win.title("桃園ubike即時查詢")


area=tk.StringVar()  #地區文字變數
site=tk.StringVar()  #站名文字變數
result=tk.StringVar()   #訊息文字變數
arealist=[] #地區串列
sitelist=[]
listradio=[] #地區選項按鈕串列

for a1 in data["sarea"]:
    if(a1 not in arealist):  #如果串列中無該area就將其加入
        arealist.append(a1)
#建立第1個area的site串列
count=0
for s1 in data["sna"]:
    if(s1==arealist[0]):
        sitelist.append(data.ix[count,0])
    count+=1

label1=tk.Label(win,text="你想要找哪個區的呢?",fg="#FFAA5E", font=("新細明體", 12), pady=15,background="white")
label1.pack()
frame1=tk.Frame(win,bg='white')
frame1.pack()
for i in range(0,2):     #2列選項按鈕
    for j in range(0,4):  #每列4個選項按鈕
        n=i*4+j
        if(n<len(arealist)):  #取得area名稱
            area1=arealist[n]
             #建立選項按鈕
            rbtem = tk.Radiobutton(frame1, text=area1, variable=area, value=area1, command=rbarea, font=("新細明體", 10),background="white")
            rbtem.grid(row=i, column=j)  #設定選項按鈕位置
            if(n==0):  #選取第1個區域
                rbtem.select()

label2 = tk.Label(win, text="站名：", pady=6, fg="#FFAA5E", font=("新細明體", 12),bg='white')
label2.pack()
frame2 = tk.Frame(win,bg='white')  #site容器
frame2.pack()
sitemake()
btnDown = tk.Button(win, text="更新資料", font=("新細明體", 12),bg="#FAF0E6",command=clickRefresh)
btninfo = tk.Button(win, text="顯示區域剩餘車數", font=("新細明體", 12),bg="#FAF0E6",command=ShowInfo)
btnDown.pack(pady=6)
btninfo.pack(pady=6)
lblResult1 = tk.Label(win, textvariable=result, fg="#FF665E", font=("新細明體", 14),bg='white')
lblResult1.pack(pady=6)
rbSite()  #顯示site訊息

win.mainloop()         
        
