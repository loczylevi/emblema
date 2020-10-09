import turtle               
wn = turtle.Screen()        
alex = turtle.Turtle()        
def haromszog(h, n, sz):
    for i in range(4):
        alex.color(sz)
        alex.forward(70)
        alex.left(99)
        alex.forward(88)
    
haromszog(70, 120, "brown")
haromszog(20, 72, "green")
haromszog(44, 150, "red")
