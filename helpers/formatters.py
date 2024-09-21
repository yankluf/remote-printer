from email.header import decode_header

def safe_attachment_filename(raw_filename):
    decoded_filename = decode_header(raw_filename)
    filename = []
    for decoded_part in decoded_filename:
        if decoded_part[1] == None and type(decoded_part[0]) is str:
            filename.append(decoded_part[0])
        elif decoded_part[1] == None and type(decoded_part[0]) is not str:
            filename.append(decoded_part[0].decode('utf-8'))
        else:
            filename.append(decoded_part[0].decode(decoded_part[1]))
    return ''.join(filename)