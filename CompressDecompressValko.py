import zlib, sys, lzma, json

class CompressDecompress:

    def zlib(self):

        try:
            print("Reading the file Payload to compress")
            payload = open('payloadValko.json', 'rb')
            data = payload.read()
            print("Compressing")
            payloadComp = zlib.compress(data)
            print(payloadComp)
            checksum = zlib.crc32(data)
            print(checksum)
            payloadComp = zlib.decompress(payloadComp)
            print(payloadComp)
            checksumGen = zlib.crc32(payloadComp)
            print(checksumGen)
            if checksum == checksumGen:
                print("Checksum matches")

            else:
                 print("Checksum mismatch")
        except Exception as e:
            print(e)

    def lzma(self):

        try:
            print("Reading the file Payload to compress")
            payload = open('payloadValko.json', 'rb')
            data = payload.read()
            print("Compressing")
            payloadComplzma = lzma.compress(data)
            print(payloadComplzma)
            checksum = lzma.CHECK_CRC32(data)
            print(checksum)
            payloadComplzma = lzma.decompress(payloadComplzma)
            print(payloadComplzma)
            checksumGen = lzma.CHECK_CRC32(payloadComplzma)
            print(checksumGen)
            if checksum == checksumGen:
                print("Checksum match")

            else:
                print("Checksum mismatch")
        except Exception as e:
            print(e)
        

    def bz2(self):
        print()





if __name__ == '__main__':
    c = CompressDecompress()
    c.zlib()
    c.lzma()
