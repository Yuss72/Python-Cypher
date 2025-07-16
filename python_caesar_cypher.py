hurufs = 'abcdefghijklmnopqrstuvwxyz'
jumlah_huruf = len(hurufs)

def enkripsi(plaintext, kunci):
    ciphertext = ''
    for huruf in plaintext:
        huruf = huruf.lower()
        if not huruf == ' ':
            indeks = hurufs.find(huruf)
            if indeks == -1:
                ciphertext += huruf
            else:
                indeks_baru = indeks + kunci
                if indeks_baru >= jumlah_huruf:
                    indeks_baru -= jumlah_huruf
                ciphertext += hurufs[indeks_baru]
    return ciphertext

def dekripsi(ciphertext, kunci):
    plaintext = ''
    for huruf in ciphertext:
        huruf = huruf.lower()
        if not huruf == ' ':
            indeks = hurufs.find(huruf)
            if indeks == -1:
                plaintext += huruf
            else:
                indeks_baru = indeks - kunci
                if indeks_baru < 0:
                    indeks_baru += jumlah_huruf
                plaintext += hurufs[indeks_baru]
    return plaintext

print( )
print('*** CAESAR CIPHER PROGRAM ***')
print( )

print('Apakah kamu mau enkripsi atau dekripsi?')
user_input = input('e/d: ').lower()
print( )

if user_input == 'e':
    print('ENKRIPSI MODE TERPILIH')
    print( )
    kunci = int(input('Masukan kunci (1 sampai 26): '))
    text = input('Masukan Text yang akan di enkripsi: ')
    ciphertext = enkripsi(text, kunci)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('DEKRIPSI MODE TERPILIH')
    print( )
    kunci = int(input('Masukan kunci (1 sampai 26): '))
    text = input('Masukan Text yang akan di dekripsi: ')
    plaintext = dekripsi(text, kunci)
    print(f'PLAINTEXT: {plaintext}')