##########  Author: Evgeniy Chervinko       ##########
##########  email:  proleaveprod@gmail.com  ##########
##########  phone:  +7-911-259-19-88        ##########

#You should install by pip:
#   matplotlib
#   numpy
#   keyboard


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import sqrt
import keyboard

fig, ax = plt.subplots()

ax.set(xlim=[-1.5, 1.5], ylim=[-1.5, 1.5])

ax.grid()
ax.set_autoscale_on(1)
t = np.arange(0, 2*np.pi, 0.01)          # угол t от 0 до 2pi с шагом 0.01
r = 1                                    # радиус 4
plt.plot(r*np.sin(t), r*np.cos(t), lw=1) # x и у задаем как numpy функции от t
plt.axis('equal')                        # масштаб осей Х и У одинаковый (чтобы круг не был овалом)

iabc_alpha = 1
iabc_width = 0.02
Ia = ax.quiver([0],[0],[0],[0],color='red',units='xy',scale=1, alpha=iabc_alpha ,width=iabc_width)
Ib = ax.quiver([0],[0],[0],[0],color='green',units='xy',scale=1, alpha=iabc_alpha ,width=iabc_width)
Ic = ax.quiver([0],[0],[0],[0],color='blue',units='xy',scale=1, alpha=iabc_alpha ,width=iabc_width)
Ia.set_linestyle('dotted')
Ib.set_linestyle('dotted')
Ic.set_linestyle('dotted')
i_alpha = 1
i_width = 0.03
I  = ax.quiver([0],[0],[1],[0],color='black',units='xy',scale=1, alpha=i_alpha ,width=i_width)

i_alfabeta_alpha = 1
i_alfabeta_width = 0.02
Ialfa_vector = ax.quiver([0],[0],[0],[0],color='#FF00FF',units='xy',scale=1,alpha=i_alfabeta_alpha ,width=i_alfabeta_width)
Ibeta_vector = ax.quiver([0],[0],[0],[0],color='#FF00FF',units='xy',scale=1,alpha=i_alfabeta_alpha ,width=i_alfabeta_width)

Ialfabeta_vector = ax.quiver([0],[0],[0],[0],color='#FFD700',units='xy',scale=1,alpha=i_alfabeta_alpha ,width=i_alfabeta_width+0.02)


text_fi = ax.text(1,1,f"θ = {0}")
text_vd = ax.text(1,0.9,f"Vd = {0}")
text_vq = ax.text(1,0.8,f"Vq = {0}")

text_dot_alfa = ax.text(2,2,f"α",weight='bold',color='#FF00FF')
text_dot_beta = ax.text(2,2,f"β",weight='bold',color='#FF00FF')
text_dot_cur_angle = ax.text(2,2,f"θ",weight='bold',color='red',fontsize=15)
text_dot_force = ax.text(2,2,f"F",weight='bold',color='red',fontsize=15)
cur_angle = 0
cur_vd = 0
cur_vq = 1

def angle_by_keyboard():
    global cur_angle
    if keyboard.is_pressed('1'):
        cur_angle+=1
        if cur_angle==360:
            cur_angle=0
    if keyboard.is_pressed('0'):
        cur_angle-=1
        if cur_angle==-1:
            cur_angle=359
    text_fi.set_text(f"θ = {cur_angle}°")
    return np.deg2rad(cur_angle)

def vdq_by_keyboard():
    global cur_vd,cur_vq

    if keyboard.is_pressed('right'):
        cur_vd+=0.01
        if(cur_vd>1):
            cur_vd=-0.99

    if keyboard.is_pressed('left'):
        cur_vd-=0.01
        if(cur_vd<-1):
            cur_vd=0.99

    if keyboard.is_pressed('up'):
        cur_vq+=0.01
        if(cur_vq>1):
            cur_vq=-0.99

    if keyboard.is_pressed('down'):
        cur_vq-=0.01
        if(cur_vq<-1):
            cur_vq=0.99



    text_vd.set_text(f"Vd = {round(cur_vd,2)}")
    text_vq.set_text(f"Vq = {round(cur_vq,2)}")
    return cur_vd,cur_vq

def setVector(vector,r,fi):
    x = r*np.cos(fi)
    y = r*np.sin(fi)
    vector.set_UVC(x,y)

    return x,y

def clarkeparkGetAB(vd,vq,thetta):
    va = vd* np.cos(thetta) - vq*np.sin(thetta)
    vb = vq* np.cos(thetta) - vd*np.sin(thetta)

    return va,vb

def clarkeGetABC(va,vb):
    v_a = va
    v_b = (-va + sqrt(3) * vb)/2
    v_c = (-va-sqrt(3)*vb)/2
    return v_a,v_b,v_c

thetta=0
def update(frame):
    global thetta

        
    mode = 1        #####0 - automatical changing the angle; 1 - controlling of angle by keyboard 0 - decrease 1 - increase the thetta.
    if mode:
        thetta = angle_by_keyboard()
    else:
        thetta +=0.02
        if(thetta==360):
            thetta=0


    vd,vq = vdq_by_keyboard() #####Controling of Vd and Vq variables by keyboard (left,right,up,down arrows)

    Ix,Iy = setVector(I,1,thetta)  
    
    text_dot_cur_angle.set_position([Ix,Iy])

    alpha,beta = clarkeparkGetAB(vd,vq,thetta)


    Ialfabeta_vector.set_UVC(alpha,beta)
    text_dot_force.set_position([alpha,beta])
    I_a,I_b,I_c = clarkeGetABC(alpha,beta)
    Ia_x,Ia_y = setVector(Ia,I_a,np.deg2rad(0))
    Ib_x,Ib_y = setVector(Ib,I_b,np.deg2rad(0+120))
    Ic_x,Ic_y = setVector(Ic,I_c,np.deg2rad(0+240))


ani = animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=10)
plt.show()

