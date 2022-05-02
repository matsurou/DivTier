def run(_string_in, _universal_interval, _lambda_func):

    if _string_in.startwith('[') and _string_in.endwith(']'):
        _interval_in = _string_in[1,-1].split(',')

        _interval_in = [_lambda_func(i) for i in _interval_in]

        _interval_out = [
            max(_universal_interval[0], min(_interval_in[0], _interval_in[1])) ,
            min(_universal_interval[1], max(_interval_in[0], _interval_in[1]))
        ]

        return _interval_out


if __name__ == '__main__':
    universal_interval = [0,10]
    lambda_func  = lambda val:int(val) - 1
    while True:
        run(input(), universal_interval, lambda_func)
