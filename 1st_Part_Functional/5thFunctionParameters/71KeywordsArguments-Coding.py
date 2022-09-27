def func1(*, a, b):
    print(a)
    print(b)


func1(a=10, b=20)
# func1(10, 20) # it is not going to work


def func1(a, b=20, *args, d=0, e='n/a'):
    print(a, b, args, d, e)


func1(5, 4, 3, 2, 1, d=0, e='all engines running')
func1(0, 600, d='goooood morning', e='python!')
func1(11, 'm/s', 24, 'mph', d='unladen', e='swallow')
