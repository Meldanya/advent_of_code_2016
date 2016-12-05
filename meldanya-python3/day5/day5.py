import hashlib


def all_(xs):
    xs_ = [True if x != '_' else False for x in xs]
    return all(xs_)


def main():
    inp = 'uqwqemis'

    # Part 1
    i, j = 0, 0
    password = ['_'] * 8
    password2 = ['_'] * 8
    while not (all_(password) and all_(password2)):
        h = hashlib.md5((inp + str(i)).encode('utf-8')).hexdigest()
        if h[:5] == '00000':
            # First one
            if not all_(password):
                password[j] = h[5]
                j += 1

            # Second one
            try:
                pos = int(h[5])
                if 0 <= pos and pos < 8 and password2[pos] == '_':
                    password2[pos] = h[6]
            except ValueError:
                pass
            print('password: ', ' '.join(password))
            print('password2:', ' '.join(password2))
        i = i+1
    print(''.join(password), ''.join(password2))


if __name__ == '__main__':
    main()
