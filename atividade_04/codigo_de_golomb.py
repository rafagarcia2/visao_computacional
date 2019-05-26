import math

def passo2 (ans, n, m):
    k = int (math.log(m, 2))
    c = int (math.pow (2, k) - m)

    r = int (math.fmod(n, m))

    if (r >= 0 and r < c):
        st = "0" + str(k-1) + "b"
        rb = str(format(r, st))  
    else:
        st = "0" + str(k) + "b"
        rb = str(format(r+c, st))

    return rb


def codigo_de_golomb(posicao, deslocamento):
    '''

    '''
    q = posicao / deslocamento
    
    ans = "1" * int(q)
    ans += "0" + passo2(ans, posicao, deslocamento)
    
    return ans


def golomb_encode(number, bits):
    "Yields a sequence of bits Golomb-coding the number with divisor 2**bits."
    qq, rr = divmod(number, 2**bits)

    for ii in range(qq):
        yield 1
    yield 0

    for ii in range(bits-1, -1, -1):    # most significant bit first
        yield 1 if rr & (1 << ii) else 0


def pack_bits(bits):
    """Yields a sequence of bytes containing the specified sequence of bits.

    Big-endian, and packs stray bits into the last byte left-justified
    with zeroes.

    """
    buf, bufptr = 0, 0

    for bit in bits:
        buf = buf << 1 | bit
        bufptr += 1

        if bufptr == 8:
            yield chr(buf)
            buf, bufptr = 0, 0

    if bufptr:
        yield chr(buf << (8 - bufptr))


def golomb_decode(bytes, bits):
    """Yields each of the numbers Golomb-encoded in bytes with divisor 2**bits.

    Not quite the inverse of golomb_encode; that encodes only a single
    number, and encodes it as a sequence of bits.  Otherwise, though,
    the two are inverses.

    """
    bit_seq = unpack_bits(bytes)

    while True:              # or until bit_seq throws a StopIteration
        qq = 0
        while bit_seq.next() == 1:
            qq += 1

        rr = 0
        for ii in range(bits):
            rr = rr << 1 | bit_seq.next()

        yield qq << bits | rr

def unpack_bits(bytes):
    """Yields the bits in a sequence of bytes."""
    for byte in bytes:
        byte = ord(byte)
        for ii in range(7, -1, -1):     # 8 bits per byte
            yield 1 if byte & (1 << ii) else 0