import cmath
for y in range(17):
    sum = 0
    for x in range(17):
        expValue = cmath.exp((2*cmath.pi*1j*x*y)/18)
        if ((4**x)%21)==16:
            sum = sum + (expValue * (1/cmath.sqrt(6)))
    sum = sum * (1/cmath.sqrt(18))
    print str(y) + "yields " + str(sum)
