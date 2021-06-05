import struct
import pprint

D_SIZE = 2+4*4
C_SIZE = 2 + 8 + 8 + 2 + 8 + 8*2 + 2*6
B_SIZE = 4 + 4 + 1 + 2
A_SIZE = 1 + 4 + B_SIZE + 1 + 4 + 8


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('<hIIII', d_bytes)

    return{'D1': d_parsed[0],
           'D2': list(d_parsed[1:])}


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('<hdqHqQQhhhhhh', c_bytes)

    return{'C1': c_parsed[0],
           'C2': c_parsed[1],
           'C3': c_parsed[2],
           'C4': c_parsed[3],
           'C5': c_parsed[4],
           'C6': list(c_parsed[5:7]),
           'C7': list(c_parsed[7:])
           }


def parse_b(offset, byte_string):

    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('<IIBH', b_bytes)

    b1_parsed = struct.unpack('<'+'H' * b_parsed[0],
                              byte_string[b_parsed[1]: b_parsed[1] + b_parsed[0]*2])

    b1_list = [parse_c(addr, byte_string) for addr in b1_parsed]

    return{'B1': b1_list,
           'B2': b_parsed[2],
           'B3': b_parsed[3]
           }


def parse_a(offset, byte_string):

    a12_bytes = byte_string[offset:offset + 5]
    a12_parsed = struct.unpack('<bf', a12_bytes)

    a3_parsed = parse_b(offset + 5, byte_string)

    a456_bytes = byte_string[offset + 5 + B_SIZE: offset + 5 + B_SIZE + 13]
    a456_parsed = struct.unpack('<BIQ', a456_bytes)

    return{'A1': a12_parsed[0],
           'A2': a12_parsed[1],
           'A3': a3_parsed,
           'A4': a456_parsed[0],
           'A5': parse_d(a456_parsed[1], byte_string),
           'A6': a456_parsed[2]
           }


def f31(byte_string):
    return parse_a(3, byte_string)





pprint.pprint(f31((b'OZM\x8d\xb5\xee\x01\xbf\x02\x00\x00\x00\x90\x00\x00\x00\xdc\x15\x14k'
                   b'\x94\x00\x00\x00\xe6.\x98 \xae\xaft\x81\x8cS\x80\x1e\xc5)\x160'
                   b"\xe7\xbf\xa2\xe4\xeb5\xd4\xe2Q\xe4'\x91\n\xbf\xf2\xfc\x8b\xf4\xcc\xf7"
                   b'H\xa2]\xe2\xa5\xc8z\xbb4\x08R\xcc\x18\x963a\x9b\xcev_\x02\xca\xd2\xc0'
                   b'\xa5\xe3\xe8\x05\xc5B@u\xe7\xeb\xdc\xb8\xe8?\x0c\xe8\xa6)\x15\x97H\x91\x80N'
                   b'\xb9\xc05\xc2\xea\x87\t\xc9\x0b\xa8\x0b\xbaq\xf7\xf1f{\xf5\xe6\xa1j/\xc4B'
                   b'\x86\xa2\x0e\x1d\xc0\xa5\x14\xd29\x8dDk \x00X\x00,U7\xcd\x89"\rc'
                   b'\x9c\x8b\xdc\xa9\xb8\xdfZ\x01\xbek')))


# int8 = b
# int16 = h
# int32 = i
# int64 = q

# float =
# uint8 = B
# uint16 = H
# uint32, размер 4 = I
# uint64, Размер 2 = Q
