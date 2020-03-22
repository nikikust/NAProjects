import argparse


def xor_files(fn_a, fn_b, fn_res):
    file_a = bytearray(open(fn_a, 'rb').read())
    file_b = bytearray(open(fn_b, 'rb').read())
    open(fn_res, 'wb').write(xor_bytes(file_a, file_b))


def xor_bytes(ba_a, ba_b):
    ba_res = bytearray(min(len(ba_a), len(ba_b)))
    for i in range(len(ba_res)):
        ba_res[i] = ba_a[i] ^ ba_b[i]
    return ba_res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename_a', type=str)
    parser.add_argument('filename_b', type=str)
    parser.add_argument('filename_res', type=str)
    args = parser.parse_args()
    xor_files(args.filename_a, args.filename_b, args.filename_res)