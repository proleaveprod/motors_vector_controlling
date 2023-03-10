import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from colorama import Fore




t2_lim = -((3/2)**(0.5))
t2 = np.linspace(0,t2_lim,21)

t3 = np.linspace(0, 2, 21)


t1 = np.linspace(0, 2, 10)
t11 = np.linspace(2, 0, 10)

y1 = np.concatenate((t1,t11))


y2 = t2/(np.deg2rad(60))
y3 = t3/(np.deg2rad(-60))


fig, ax = plt.subplots()
ax.set(xlim=[-3, 3], ylim=[-3, 3])
ax.grid()
t = np.arange(0, 2*np.pi, 0.01)          # угол t от 0 до 2pi с шагом 0.01
r = 2                                    # радиус 4
plt.plot(r*np.sin(t), r*np.cos(t), lw=1) # x и у задаем как numpy функции от t
plt.axis('equal')                        # масштаб осей Х и У одинаковый (чтобы круг не был овалом)


line_a = ax.plot(t1[0], y1[0], c="r",lw=2)[0]
line_b = ax.plot(t2[0], y2[0],c="g",lw=2)[0]
line_c = ax.plot(t3[0], y3[0],c="b",lw=2)[0]

vector = ax.quiver([0],[0],[0],[2],color='black',units='xy',scale=1)
vector.set_alpha(0.5)




def update(frame):
    # for each frame, update the data stored on each artist.
    
    speed = 30

    f1 = np.sin(frame/speed) + 1
    f2 = np.sin(frame/speed + np.deg2rad(120)) + 1
    f3 = np.sin(frame/speed + np.deg2rad(240)) + 1

    
    

    #print(Fore.RED + ' ' +str(round(f1,2)) + ' ' +Fore.GREEN+str(round(f2,2))+ '   '+Fore.WHITE+str(round(q_x,2)))


    #print(Fore.RED + ' ' +str(round(f1,2)) + ' ' +Fore.GREEN+str(round(f2,2)) + ' '+Fore.BLUE+str(round(f3,2)))
    


    x1 = 0
    y1 = np.linspace(0,((f1)),20)

        

    x2_lim = 2*np.cos(np.deg2rad(210))
    y2_lim = 2*np.sin(np.deg2rad(210)) 
    x2 = np.linspace(0,(f2*x2_lim/2),20)
    y2 = np.linspace(0,(f2*y2_lim/2),20)

    x3_lim = 2*np.cos(np.deg2rad(330))
    y3_lim = 2*np.sin(np.deg2rad(330)) 
    x3 = np.linspace(0,(f3*x3_lim/2),20)
    y3 = np.linspace(0,(f3*y3_lim/2),20)


    line_a.set_xdata(x1)
    line_a.set_ydata(y1)

    line_b.set_xdata(x2)
    line_b.set_ydata(y2)

    line_c.set_xdata(x3)
    line_c.set_ydata(y3)

    
    x_1 = str(round(x1,2))
    x_2 = str(round(x2[19],2))
    x_3 = str(round(x3[19],2))

    y_1 = str(round(y1[19],2))
    y_2 = str(round(y2[19],2))
    y_3 = str(round(y3[19],2))

    # q_x = x1 + x2[19] + x3[19]
    # q_y = y1[19] + x2[19] + x3[19]
    # vector.set_UVC(q_x,q_y)


    # print(Fore.WHITE + "x:",end='   ')
    # print( Fore.RED +   x_1   ,end='   ')
    # print( Fore.GREEN + x_2   ,end='   ')
    # print( Fore.BLUE +  x_3   ,end='\n')

    # print(Fore.WHITE + "y:",end='   ')
    # print( Fore.RED +   y_1   ,end='   ')
    # print( Fore.GREEN + y_2   ,end='   ')
    # print( Fore.BLUE +  y_3   ,end='\n\n')
    # line_a.set_ydata(y1[:frame])

    k = 1.35
    q_x = x1 + x2[19] + x3[19]
    q_x *= k
    q_y = y1[19] + y2[19] + y3[19]
    q_y *= k
    vector.set_UVC(q_x,q_y)

  
    # line_b.set_xdata(t2[:frame])
    # line_b.set_ydata(y2[:frame])

    # line_c.set_xdata(t3[:frame])
    # line_c.set_ydata(y3[:frame])

    

ani = animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=10)
plt.show()