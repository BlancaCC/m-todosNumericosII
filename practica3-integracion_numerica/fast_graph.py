'''PINTA GRÁFICAS RÁPIDO 
    xx = array numpy con nodos
    yy = valores de esos nodos 
'''
import matplotlib.pyplot as plt

def draw_one(xx,yy,my_label='aprox'):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(xx, yy, label=my_label)   
    ax.legend()
    fig.tight_layout()
    return fig

def multiple_draw(vx,vy,vlabel):
    fig, ax = plt.subplots(figsize=(8, 4))
    
    for i in range(len(vy)):
        ax.plot(vx[i],vy[i], label=f'aprox n={vlabel[i]}')
    
    ax.legend()
    fig.tight_layout()
    return fig
 
