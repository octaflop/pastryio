import sys
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def int_to_b64(i):
    return urlsafe_base64_encode(
        str(i).encode())


def b64_to_int(b64):
    return int(urlsafe_base64_decode(b64))


def _quick_test(length):
    for i in range(0, length):
        b64 = int_to_b64(i)
        result = b64_to_int(b64) == i
        output = "{i} → {b64}, {result}".format(
            i=i,
            b64=b64,
            result=result
            )
        print(output)


def _benchmark():
    import timeit
    print(timeit.timeit("_quick_test(10000)", setup="from __main__ import _quick_test"), number=5)
