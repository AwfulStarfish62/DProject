#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from tkinter.filedialog import *
from tkinter.messagebox import *
import pickle
import numpy
import numpy as np
from numpy import *
from sklearn.cluster import KMeans
import nltk
nltk.download('punkt')
import scipy
from settings import docs,stem,stopWords,filmsGenre,filmsNum
#docs = docsOld
ddd=len(docs)
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer(stem)
doc=[w for w in docs]
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'
txt = open("txt.txt","a")
txt1 = open("txt1.txt","a")
txt2 = open("txt2.txt","a")
def STart():
    print("start STart")
    #clear_all()
    txt.write(str("Исходные документы\n"))
    for k, v in enumerate(docs):
           txt.write(str(str("Ном.док--%u Текст-%s \n"%(k,v)).encode("utf-8")))
    print(var1)
    if  var1==0:
        print("end STart")
        return word_1()
    elif  var1==1:
        t=" "
        wordDecode = (' ').join(doc)
        #wordDecode = wordDecode.decode('utf-8')
        word=nltk.word_tokenize(wordDecode)
        stopword=[stemmer.stem(w).lower() for w in stopWords]
        print("end STart")
        return WordStopDoc(t,stopword)
def word_1():
     print("start word_1")
     #txt1.delete(1.0, END)
     #txt2.delete(1.0, END)
     wordDecode2 = (' ').join(doc)
     #wordDecode2 = wordDecode2.decode('utf-8')
     word=nltk.word_tokenize(wordDecode2)
     n=[stemmer.stem(w).lower() for w in word if len(w) >1 and w.isalpha()]
     stopword=[stemmer.stem(w).lower() for w in stopWords]
     fdist=nltk.FreqDist(n)
     t=fdist.hapaxes()
     txt1.write(str("Слова которые встричаються только один раз:\n%s"%t))
     txt1.write(str("\n"))   
     print("end word_1")
     return WordStopDoc(t,stopword)
def WordStopDoc(t,stopword):
    print("start WordStopDoc")
    d={}
    c=[]
    p={}
    for i in range(0,len(doc)):
        wordDecode3 = doc[i]
        #wordDecode3 = wordDecode3.decode('utf-8')	
        word=nltk.word_tokenize(wordDecode3)
        word_stem=[stemmer.stem(w).lower()  for w in word if len(w)>1 and  w.isalpha()]
        word_stop=[ w for w in word_stem if w not in stopword]
        words=[ w for w in word_stop if w not in t]
        p[i]=[w for w in words]
        for w in words:
               if w not in c:
                    c.append(w)
                    d[w]= [i]
               elif w in c:
                    d[w]= d[w]+[i]
    txt1.write(str("Стоп-слова:\n"))
    txt1.write(str( stopWords))
    txt1.write(str("\n"))      
    txt1.write(str("Cлова(основа):\n"))
    txt1.write(str(c))
    txt1.write(str("\n"))
    txt1.write(str(" Распределение слов по документам:\n"))
    txt1.write(str(d)) 
    txt1.write(str("\n"))
    print("end WordStopDoc")
    return Create_Matrix(d,c,p)
def Create_Matrix(d,c,p):
    print("start Create_Matrix")
    a=len(c)
    b=len(doc)
    A = numpy.zeros([a,b])
    c.sort()
    for i, k in enumerate(c):
        for j in d[k]:
            A[i,j] += 1
    txt1.write(str( "Первая матрица для проверки заполнения строк и столбцов:\n"))
    txt1.write(str(A))
    txt1.write(str("\n"))
    print("end Create_Matrix")
    return Analitik_Matrix(A,c,p) 
def Analitik_Matrix(A,c,p):
    print("start Analitik_Matrix")
    print(A)
    print("\n\n\n")
    print(c)
    print("\n\n\n")
    print(p)
    print("\n\n\n")
    wdoc = sum(A, axis=0)
    pp=[]
    q=-1
    for w in wdoc:
        q=q+1
        if w==0:
            pp.append(q)
    if len(pp)!=0:
        for k in pp:
            doc.pop(k)
        #word_1()  
    elif len(pp)==0:
        rows, cols = A.shape
        txt1.write(str("Исходная частотная матрица число слов---%u больше либо равно числу документов-%u \n"%(rows,cols))) 
        nn=[]
        for i, row in enumerate(A):
            st=(c[i], row)
            stt=sum(row)
            nn.append(stt)
            txt1.write(str(st)) 
            txt1.write(str("\n"))
        if  var==0:
            print("end Analitik_Matrix")
            return TF_IDF(A,c,p)
        elif var==1:
            l=nn.index(max(nn))
            print("end Analitik_Matrix")
            return U_S_Vt(A,c,p,l)
def TF_IDF(A,c,p):
     print("start TF_IDF")
     wpd = sum(A, axis=0)
     dpw= sum(asarray(A > 0,'i'), axis=1)
     rows, cols = A.shape
     txt1.write(str("Нормализованная по методу TF-IDF матрица: строк- слов -%u столбцов - документов--%u \n"%(rows,cols))) 
     for i in range(rows):
         for j in range(cols):
             m=float(A[i,j])/wpd[j]
             n=log(float(cols) /dpw[i])
             A[i,j] =round(n*m,2)
     gg=[]
     for i, row in enumerate(A):
         st=(c[i], row)
         stt=sum(row)
         gg.append(stt)    
         txt1.write(str(st)) 
         txt1.write(str("\n"))
     l=gg.index(max(gg))
     print("end TF_IDF")
     return U_S_Vt(A,c,p,l)
def U_S_Vt(A,c,p,l):
    print("start U_S_Vt")
    U, S,Vt = numpy.linalg.svd(A)
    rows, cols = U.shape
    for j in range(0,cols):
        for i  in range(0,rows):
            U[i,j]=round(U[i,j],4)   
    txt1.write(str(" Первые 2 столбца ортогональной матрицы U слов, сингулярного преобразования нормализованной матрицы: строки слов -%u\n"%rows)) 
    for i, row in enumerate(U):
        st=(c[i], row[0:2])
        txt1.write(str(st))
        txt1.write(str("\n"))

    txt1.write(str(" Первые 2 строки диагональной матрица S \n"))
    Z=np.diag(S)
    txt1.write(str(Z[0:2,0:2] ))
    txt1.write(str("\n"))
    rows, cols = Vt.shape
    for j in range(0,cols):
        for i  in range(0,rows):
            Vt[i,j]=round(Vt[i,j],4)
    txt1.write(str(" Первые 2 строки ортогональной матрицы Vt документов сингулярного преобразования нормализованной матрицы: столбцы документов -%u\n"%cols)) 
    st=(-1*Vt[0:2, :])
    txt1.write(str(st))
    txt1.write(str("\n"))
    res3=(-1*Vt[0:1, :])
    res4=(-1*Vt[1:2, :])
    X=numpy.dot(U[:,0:2],Z[0:2,0:2])
    Y=numpy.dot(X,Vt[0:2,:] )
    txt1.write(str(" Матрица для выявления скрытых связей \n"))
    rows, cols =Y.shape
    for j in range(0,cols):
        for i  in range(0,rows):
           Y[i,j]=round( Y[i,j],2)
    for i, row in enumerate(Y):
        st=(c[i], row)
        txt1.write(str(st))
        txt1.write(str("\n")) 
    print("end U_S_Vt")
    return Save_Load_Data(res3,res4,c)

def Save_Load_Data(res3,res4,c):
	if  var3==0:
		print("end SaveData")
		print("res3 = \n")
		print(res3)
		print("res4 = \n")
		print(res4)
		return Grafics_End(res3,res4,c)
	elif  var3==1:
		print("end LoadData")
		return Grafics_End(res3,res4,c) 

def Grafics_End(res3,res4,c): # Построение график с программным управлением масштабом
    print("start Grafics_End")
    plt.title('Semantic space', size=14)
    plt.xlabel('x-axis', size=14)
    plt.ylabel('y-axis', size=14)

    e3=(max(res3[0])-min(res3[0]))/len(doc)
    e4=(max(res4[0])-min(res4[0]))/len(doc)

    plt.axis([min(res3[0])-e3, max(res3[0])+e3, min(res4[0])-e4, max(res4[0])+e4])
    plt.plot(res3[0], res4[0], color='b', linestyle=' ', marker='o',ms=10,label='Documents №')
    plt.legend(loc='best')

    allFilmsNum = 0
    for j in range(0,len(filmsNum)):
        k={}
        xvMass=[]
        yvMass=[]
        print("filmsNum["+ str(j) +"] = " + str(filmsNum[j]))
        for i in range(0,filmsNum[j]):
            xv=float((res3[0])[i+allFilmsNum])
            yv=float((res4[0])[i+allFilmsNum])
            xvMass.append(xv)
            yvMass.append(yv)
            if (xv,yv) not in k.keys():
                k[xv,yv]=str(i+allFilmsNum)
            elif (xv,yv) in k.keys():
                k[xv,yv]= k[xv,yv]+','+str(i+allFilmsNum)
            #plt.annotate(k[xv,yv], xy=((res3[0])[i], (res4[0])[i]), xytext=((res3[0])[i]+0.015, (res4[0])[i]+0.015),arrowprops=dict(facecolor='blue', shrink=0.1),)
        allFilmsNum+=filmsNum[j]
        print("\n\nSUM")
        print(xvMass)
        print(yvMass)
        plt.plot(np.array(xvMass).sum()/len(xvMass), np.array(yvMass).sum()/len(yvMass), color='b', linestyle=' ', marker='o',ms=10,label='Documents №')
        plt.annotate(filmsGenre[j], xy=(np.array(xvMass).sum()/len(xvMass), np.array(yvMass).sum()/len(yvMass)), xytext=(np.array(xvMass).sum()/len(xvMass)+0.015, np.array(yvMass).sum()/len(yvMass)+0.015),arrowprops=dict(facecolor='blue', shrink=0.1),)

    plt.grid()
    plt.show() 
    print("end Grafics_End")
def close_win():
     if askyesno("Exit", "Do you want to quit?"):
          tk.destroy()
def save_text():
    save_as = asksaveasfilename()
    try:
        x = txt.get(1.0, END)+ '\n'+txt1.get(1.0, END) + '\n'+txt2.get(1.0, END)
        f = open(save_as, "w")
        f.writelines(x)
        f.close()
    except:
        pass 
    clear_all()
def clear_all():
     txt.delete(1.0, END)
     txt1.delete(1.0, END)
     txt2.delete(1.0, END)

var = 1
var1 = 0
var2 = 0
var3 = 0
STart()

# tk= Tk()
# tk.geometry('700x650')
# main_menu = Menu(tk)
# tk.config(menu=main_menu)
# file_menu = Menu(main_menu)
# main_menu.add_cascade(label="LSA", menu=file_menu)
# file_menu.add_command(label="Start", command=  STart)
# file_menu.add_command(label="Save text", command= save_text)
# file_menu.add_command(label="Clear all fields", command= clear_all)
# file_menu.add_command(label="Exit", command= close_win)
# txt = Text(tk, width=72,height=10,font="Arial 12",wrap=WORD)
# txt.pack()
# txt1= Text(tk, width=72,height=10,font="Arial 12",wrap=WORD)
# txt1.pack()
# txt2= Text(tk, width=72,height=10,font="Arial 12",wrap=WORD)
# txt2.pack()
# var = IntVar()
# ch_box = Checkbutton(tk, text="to use TF_IDF/no to use TF_IDF", variable=var)
# ch_box.pack()
# var1 = IntVar()
# ch_box1 = Checkbutton(tk, text="to exclude words used once/no to exclude words used once", variable=var1)
# ch_box1.pack()
# var2 = IntVar()
# ch_box2 = Checkbutton(tk, text="Evckid distance/cos distance", variable=var2)
# ch_box2.pack()

# var3 = IntVar()
# ch_box3 = Checkbutton(tk, text="Saving in file/loading from file", variable=var3)
# ch_box3.pack()
# tk.title("System of the automated semantic analysis")
# tk.mainloop()
