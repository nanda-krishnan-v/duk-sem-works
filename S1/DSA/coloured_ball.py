def array(n):
    ball = []
    blue= n//3
    green= n//3
    red= n-(blue+green)
    while blue>0:
        ball.append('blue')
        blue -=1
    while green>0:
        ball.append('Green')
        green-=1
    while red>0:
        ball.append('Red')
        red-=1
    return ball
n=int(input("Enter the total number of balls:"))
if n>3:
 ball=array(n)
 print("Generated array of balls",ball)
else:
 print("Insufficient amount of balls to generate.")