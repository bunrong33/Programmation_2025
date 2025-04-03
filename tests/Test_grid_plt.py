import matplotlib.pyplot as plt 

color = [[1,2,4],[0,1,3]]
value = [[11,2,3],[5,3,4]]

def plot(n:int, m: int):
    fig, ax = plt.subplots(figsize =(m,n))
    color_mapping = {
        0:'white',
        1: 'red',
        2: 'blue',
        3:'green',
        4:'black'
    }
    for i in range(n):
        for j in range(m):
            facecolor = color_mapping.get(color[i][j],'gray')
            rect = plt.Rectangle((j,n-1-i),1,1, linewidth=1,edgecolor = "pink", facecolor = facecolor)
            ax.add_patch(rect)
            text_color = 'black' if color[i][j] != 4 else 'white'
            ax.text(j+0.5,n-1-i+0.5,str(value[i][j]),ha = 'center', va = 'center',fontsize = 30, color = text_color)

    ax.set_xlim(0,m)
    ax.set_ylim(0,n)
    ax.set_xticks(range(m))
    ax.set_yticks(range(n))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    # ax.grid(True,which = 'both', color = 'black', linewidth = 1)
    plt.show()


plot(2,3)
