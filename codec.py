def get_bin_form(n, std_len=None):
    bin_form = ''
    while n:
        bin_form = str(n % 2) + bin_form
        n //= 2
    if std_len:
        bin_form = (std_len - len(bin_form)) * '0' + bin_form
    return bin_form


def encode(src):
    bin_str = ''
    for ch in src:
        if not (32 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122):
            print("Unsupported character: %s" % ch)
            return ''
        ch = ch.lower()
        is_letter = 'a' <= ch <= 'z'
        n = (ord(ch) - ord('a')) if is_letter else (ord(ch) - ord(' '))
        bin_str += '0' if is_letter else '1'
        bin_str += get_bin_form(n, 5)

    res = ''
    for i in range(0, len(bin_str), 8):
        dec = 0
        for ch in bin_str[i:i+8]:
            dec *= 2
            dec += int(ch)
        res += chr(dec)
    res += chr(len(bin_str) % 8 + 100)

    return res


def decode(code):
    n = ord(code[-1]) - 100
    if n == 0:
        n = 8
    code = code[:-1]
    bin_str = ''
    for i, ch in enumerate(list(code)):
        bin_str += get_bin_form(ord(ch), n if i == len(code) - 1 else 8)

    res = ''
    for i in range(0, len(bin_str), 6):
        dec = 0
        for ch in bin_str[i+1:i+6]:
            dec *= 2
            dec += int(ch)
        res += chr((ord('a') if bin_str[i] == '0' else ord(' ')) + dec)

    return res.rstrip('a')
