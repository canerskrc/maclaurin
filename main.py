from math import factorial, pi


def maclaurin(iterations):
      trueval = 0.7071067812
      x = pi / 4
      output = 0
      for i in range(iterations):
            a = (x ** (2 * i + 1)) / (factorial(2 * i + 1))
            # print("yah ",factorial(2*i+1));
            if i % 2 == 0:
                  a *= -1
                  x + a
            output -= a
            et = abs((((trueval - output) / trueval) * 100) * -1)
            ea = abs((((output - x) / output) * 100) * -1)
            print('\n\t Order: ', i)
            print('Approximation Error is : ', output)
            print('Et is : ', et)
            print('Ea is : ', ea)

      return output


iterations = int(input('Input the Number of iteration: '))

if iterations == 1:
      trueval = 0.7071067812
      x = pi / 4
      et = (((trueval - x) / trueval) * 100) * -1

      print('\n\t Order: 0')
      print('Approximation Error is : ', x)
      print('True value is : ', trueval)
      print('Et is : ', et)

elif iterations >= 2:
      maclaurin(iterations)