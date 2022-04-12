numbers = [5,2,5,2,2]
for x_count in numbers:
    #print ('x'*x_count)  this is the shortcut method. however, we would make this using nested loops
    output = ''
    for count in range (x_count):
        output = output + 'x'
    print(output)
