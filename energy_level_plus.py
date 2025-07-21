"""Plot examples of SciencePlot styles."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import scienceplots
import matplotlib as mpl
from scipy.stats import norm

name='b2p_tda'
plot='soc'
xunits='nm'
# range
xmin=0.5
xmax=4.7
ymin=-0.05
ymax=2.9

pparam = dict(xlabel='Geometry(BDP-Per dihedral, BDP-Phen dihedral)', ylabel='Energy, eV')

# calculated curve
i1, a1, b1, c1, d1 = np.genfromtxt(name+'.txt', skip_header=1, unpack=True)

# generate df
label_x=['S0','S1','T3','T1']
label_y=['gs','s1','t1','t2','t3','soc_t1','soc_t2','soc_t3','zpve']
#index=labels
df1=pd.DataFrame([a1,b1,c1,d1],index=label_x,columns=label_y) 
#df1.set_index(df1.iloc[:,0])
df1=df1.transpose()
print (df1)

#ground state
s0_gs=(a1[0]-a1[0])*27.2114
s1_gs=(b1[0]-a1[0])*27.2114
t3_gs=(c1[0]-a1[0])*27.2114
t1_gs=(d1[0]-a1[0])*27.2114

#totalizer
df1['S0_totE']=a1 + s0_gs
df1['S1_totE']=b1 + s1_gs
df1['T3_totE']=c1 + t3_gs
df1['T1_totE']=d1 + t1_gs

df1['S0_totE'][0]=s0_gs
df1['S1_totE'][0]=s1_gs
df1['T3_totE'][0]=t3_gs
df1['T1_totE'][0]=t1_gs

#rounder
df1=df1.round(decimals = 2)

#final_df
print (df1)

v_size=5.5
line_size=800
lw=1
v_left=-0.3
v_midleft=-0.25
v_right=0.2
v_midright=0.02
v_under=-0.35
v_over=0.01
v_center=-0.1
h_left=-0.217
h_right=0.225
h_under=0
h_over=0.01
l_above=0.0
l_below=-0.22
s_above=0.05
s_below=-0.12
s_left=-0.15
s_midleft=-0.05
s_mid=0.1
s_right=0.22
s_midright=0.13
s_size=5.5

with plt.style.context(['science', 'nature']):
    #fig, ax = plt.subplots(figsize=(4,3))
    fig, ax = plt.subplots()
    #ax.scatter(x3, y3, marker="+", label='B2P PES')
    
    ########## x=1 ##########
    x=1
    index=['0','1','2','3','4']
    color=['black','r','dodgerblue','darkorange','limegreen']
    label=['S$_0$: ','S$_1$: ','T$_1$: ','T$_2$: ','T$_3$: ']
    for i, j, k in zip(index, color, label):
        y=df1['S0_totE'][int(i)]
        ax.scatter(x, y, marker="_", color=j,s=line_size,linewidth=lw)
        l_x=x+s_midright
        l_y=y+s_above
        if i == '1':
            l_y=y+s_below
            l_x=x+s_midright
        if i == '0':
            l_x=x+s_left

        ax.annotate(text=k + "{:.2f}".format(y),xy=(l_x,l_y), size=s_size, alpha=1,rotation=0,color='black')
    
    ########## x=2 ##########
    x=2
    index=['0','1','2','3','4']
    color=['black','r','dodgerblue','darkorange','limegreen']
    label=['S$_0$: ','S$_1$: ','T$_1$: ','T$_2$: ','T$_3$: ']
    for i, j, k in zip(index, color, label):   
        y=df1['S1_totE'][int(i)]    
        ax.scatter(x, y, marker="_", color=j,s=line_size,linewidth=lw)
        l_x=x+s_midright
        l_y=y+s_above
        if i=='0':
            l_x=x+s_left         
        if i=='1' or i=='2':
            l_y=y+s_below
        plt.annotate(text=k + "{:.2f}".format(y),xy=(l_x,l_y), size=s_size, alpha=1,rotation=0,color='black')
        
    #y=df1['S1_totE'][int(1)]
    ##ax.scatter(x, y, marker="_",color='r',s=line_size,linewidth=lw)
    #plt.annotate(text='S$_1$: ' + "{:.2f}".format(y),xy=(x+s_right, y+s_below), size=s_size, alpha=1,rotation=0,color='black')
        
    ########## x=3 ##########
    x=3
    index=['0','1','2','3','4']
    color=['black','r','dodgerblue','darkorange','limegreen']
    label=['S$_0$: ','S$_1$: ','T$_1$: ','T$_2$: ','T$_3$: ']
    for i, j, k in zip(index, color, label):
        y=df1['T3_totE'][int(i)]
        ax.scatter(x, y, marker="_", color=j,s=line_size,linewidth=lw)
        l_x=x+s_midright
        l_y=y+s_above
        if i=='0':
            l_x=x+s_left
        if i>='4':
            l_y=y+s_below
        if i=='2':
            l_x=x+s_left
            l_y=y+s_below
       # if i=='2'or'4':
        #    y=y+s_below
        plt.annotate(text=k + "{:.2f}".format(y),xy=(l_x, l_y), size=s_size, alpha=1,rotation=0,color='black')
    
    #y=df1['T3_totE'][int(4)]
    #ax.scatter(x, y, marker="_",color='limegreen',s=400,linewidth=1)
    #plt.annotate(text='T$_3$: ' + "{:.2f}".format(y),xy=(x+s_right, y+s_below), size=4, alpha=0.5,rotation=0)
    #    
    #y=df1['T3_totE'][int(2)]
    #ax.scatter(x, y, marker="_",color='dodgerblue',s=400,linewidth=1)
    #plt.annotate(text='T$_1$: ' + "{:.2f}".format(y),xy=(x-0.1, y+s_below), size=4, alpha=0.5,rotation=0)
        
    ########## x=4 ##########
    x=4
    index=['0','1','2','3','4']
    color=['black','r','dodgerblue','darkorange','limegreen']
    label=['S$_0$: ','S$_1$: ','T$_1$: ','T$_2$: ','T$_3$: ']
    for i, j, k in zip(index, color, label):
        y=df1['T1_totE'][int(i)]
        ax.scatter(x, y, marker="_", color=j,s=line_size,linewidth=lw)
        l_x=x+s_midright
        l_y=y+s_above
        if i=='0':
            l_x=x+s_left
        if i=='1':
            l_y=y+s_below
        plt.annotate(text=k + "{:.2f}".format(y),xy=(l_x, l_y), size=s_size, alpha=1,rotation=0,color='black')
        
    ############ Arrows #############
    column=['1','2','3','4']
    state=["df1['S0_totE']","df1['S0_totE']","df1['S0_totE']","df1['S0_totE']"]
    
    #connecting_lines
    #xyA=(1+v_left,df1['S0_totE'][0])
    #xyB=(1+v_left,df1['S0_totE'][1])
    #plt.annotate(text='', xy=xyB, xytext=xyA, arrowprops=dict(arrowstyle='->', shrinkA=0, shrinkB=0, linewidth=0.3),color='black')
    #s0s1 = ConnectionPatch(xyA, xyB, coordsA='data', coordsB='data', color='gray',
    #                      arrowstyle="-|>", shrinkA=1, shrinkB=0, mutation_scale=7, fc="w", linewidth=0.5)
    #ax.add_artist(s0s1)

    ############ vertical lines ###########
    
    ########## x=1 ##########
    
    y1=df1['S0_totE'][1]
    l_y=df1['S0_totE'][1]+v_under
    index=['0','2','3','4']
    offset=[v_left,v_midleft,v_center,v_midright]
    #label=['','5','6','7']
    for i, j, in zip(index, offset):
        ls='dotted'
        label=df1['S0'][(int(i)+3)]
        lab='....'+"{:.2f}".format(label)
        style='->'
    #s1s1_s0s1
        if i=='0':
            ls='solid'
            lab=''
            style='<-'
        #+'cm$^{-1}$'
        x=1+j
        y2=df1['S0_totE'][int(i)]+h_under
        xyA=(x,y1)
        xyB=(x,y2)
        xyL=(x,l_y)
        #(y2-y1)/2)+y1-0.022)
        plt.annotate(text='', xy=xyB, xytext=xyA, arrowprops=dict(arrowstyle=style, shrinkA=0, shrinkB=0, linewidth=0.3, linestyle=ls),color='black')
        plt.annotate(text=lab, xy=xyL, size=v_size, alpha=1,rotation=-90,color='black')
    
    ########## x=2 ##########
    l_y=df1['S1_totE'][1]+v_under
    y1=df1['S1_totE'][1]
    index=['0','2','3','4']
    offset=[v_left,v_midleft,v_center,v_midright]
    #label=['','5','6','7']
    for i, j, in zip(index, offset):
    #s1s1_s0s1
        if i=='0':
            ls='solid'
            lab=''
        else:
            ls='dotted'
            label=df1['S1'][(int(i)+3)]
            lab='....'+"{:.2f}".format(label)
        x=2+j
        y2=df1['S1_totE'][int(i)]+h_under
        xyA=(x,y1)
        xyB=(x,y2)
        xyL=(x,l_y)
        #(y2-y1)/2)+y1-0.022)
        plt.annotate(text='', xy=xyB, xytext=xyA, arrowprops=dict(arrowstyle='->', shrinkA=0, shrinkB=0, linewidth=0.3, linestyle=ls),color='black')
        plt.annotate(text=lab, xy=xyL, size=v_size, alpha=1,rotation=-90,color='black')
    
    ########## x=3 ##########
    l_y=df1['T3_totE'][1]-0.4
    y1=df1['T3_totE'][1]
    index=['0','2','3','4']
    offset=[v_left,v_midleft,v_center,v_midright]
    label=['1.00x10$^{-12}$','1.00x10$^{-12}$','1.00x10$^{-12}$','1.00x10$^{-12}$']
    for i, j, in zip(index, offset):
    #s1s1_s0s1
        if i=='0':
            ls='solid'
            lab=''
        else:
            ls='dotted'
            label=df1['T3'][(int(i)+3)]
            lab='......'+"{:.2f}".format(label)
        x=3+j
        y2=df1['T3_totE'][int(i)]+h_under
        if i=='2':
            y3=((y2-y1)/2)+y1-0.1          
        else:
            y3=((y2-y1)/2)+y1
        xyA=(x,y1)
        xyB=(x,y2)
        #xyL=(x,y3-0.022-0.4)
        xyL=(x,l_y)
        plt.annotate(text='', xy=xyB, xytext=xyA, arrowprops=dict(arrowstyle='->', shrinkA=0, shrinkB=0, linewidth=0.3, linestyle=ls),color='black')
        plt.annotate(text=lab, xy=xyL, size=v_size, alpha=1,rotation=-90,color='black')
    
    ########## x=4 ##########
    l_y=df1['T1_totE'][1]+v_under
    y1=df1['T1_totE'][1]
    index=['0','2','3','4']
    offset=[v_left,v_midleft,v_center,v_midright]
    label=[df1['T1'][5],df1['T1'][6],df1['T1'][7]]
    for i, j, in zip(index, offset):
    #s1s1_s0s1
        if i=='0':
            ls='solid'
            lab=''
        else:
            ls='dotted'
            label=df1['T1'][(int(i)+3)]
            lab='.....'+"{:.2f}".format(label)
        x=4+j
        y2=df1['T1_totE'][int(i)]+h_under
        if i=='2':
            y3=((y2-y1)/2)+y1+0.1          
        else:
            y3=((y2-y1)/2)+y1
        xyA=(x,y1)
        xyB=(x,y2)
        xyL=(x,l_y)
        plt.annotate(text='', xy=xyB, xytext=xyA, arrowprops=dict(arrowstyle='->', shrinkA=0, shrinkB=0, linewidth=0.3, linestyle=ls))
        plt.annotate(text=lab, xy=xyL, size=v_size, alpha=1,rotation=-90,color='black')
    
        
    #m=((y2-y1/x2-x1))
    #b=(y2)-m*(x2)
    #y=((y2-y1)/2)+y1
    #plt.annotate(text='......', xy=xyB, xytext=(x,y), size=4, alpha=0.5,rotation=0)
    
        ############# tilted lines ###############
    
    ########## x=1.25 ##########
    #s1s0_s1s1
    x1=1+h_right
    x2=2+h_left
    y1=df1['S0_totE'][1]
    y2=df1['S1_totE'][1]+h_under
    x=1.25
    xyA=(x1,y1)
    xyB=(x2,y2)
    #plt.annotate(text='', xy=xyB, xytext=xyA, arrowprops=dict(arrowstyle='->', shrinkA=0, shrinkB=0, linewidth=0.3, linestyle='dotted'))
    m=((y2-y1/x2-x1))
    b=(y2)-m*(x2)
    y=m*x+b+l_below
    #plt.annotate(text='', xy=xyB, xytext=(x,y), size=4, alpha=0.5,rotation=-15)
    
    ########## x=2.5 ##########
    #s0s1_s1t3
    x1=1+h_right
    x2=3+h_left
    y1=df1['S0_totE'][1]
    y2=df1['T3_totE'][1]+h_under
    xyA=(x1,y1)
    xyB=(x2,y2)
    #plt.annotate(text='', xy=xyB, xytext=xyA, arrowprops=dict(arrowstyle='->', shrinkA=0, shrinkB=0, linewidth=0.5, linestyle='dotted'))
    x=2.5+h_left
    m=((y2-y1/x2-x1))
    b=(y2)-m*(x2)
    y=m*x+b+l_below
    #plt.annotate(text='', xy=xyB, xytext=(x,y), size=4, alpha=0.5,rotation=-15)
    
    
    ########  x=3.5 ###########
    column=4
    #t1t3_t1t1
    x1=3+h_right
    x2=4+h_left
    y1=df1['T3_totE'][2]
    y2=df1['T1_totE'][2]+h_under
    xyA=(x1,y1)
    xyB=(x2,y2)
    #plt.annotate(text='', xy=xyB, xytext=xyA, arrowprops=dict(arrowstyle='->', shrinkA=0, shrinkB=0, linewidth=0.3, linestyle='dotted'))
    x=3.25
    m=((y2-y1/x2-x1))
    b=(0)-m*(x2-x1)
    y=m*x+b+l_below
    #plt.annotate(text='', xy=xyB, xytext=(x,y), size=4, alpha=0.5,rotation=-15)
    
    
    ax.autoscale(tight=True)
    ax.set(**pparam)
    plt.xlim(xmin,xmax)
    plt.xticks([1,2,3,4],['S$_0$(58$^\circ$,102$^\circ$)','S$_1$(41$^\circ$,111$^\circ$)',
                          'T$_3$(44$^\circ$,111$^\circ$)','T$_1$(53$^\circ$,102$^\circ$)'],rotation = 0)
    #ax.set_xticklabels(['','S$_0$','','S$_1$','','T$_3$','','T$_1$',''])
    plt.ylim(ymin,ymax)
    #fig.savefig('fig2c.pdf')
    fig.savefig(name +'_'+ plot +'.png', dpi=300)






