def run(_string_in, _universal_set, _lambda_func):

    if _string_in.startwith('{') and _string_in.endwith('}'):
        _set_in = _string_in[1,-1].split(',')

        _set_in = [_lambda_func(i) for i in _set_in]

        _set_out = []
        for i in _universal_set:
            if i in _set_in:
                _set_out.append(i)

        return _set_out


if __name__ == '__main__':
    universal_set = list(range(0,11))
    lambda_func  = lambda val:int(val) - 1
    while True:
        run(input(), universal_set, lambda_func)
