import zlib, sys, lzma, json, bz2, time


class Compress:

    def zlib_compress(self, data):
        """
        Build zlib compression

        :param data: json file to be compressed
        :rtype: object
        """

        return zlib.compress(data)

    def lzma_compress(self, data):
        """
        Build lzma compression

        :param data: json file to be compressed
        :rtype: object
        """

        lzc = lzma.LZMACompressor(check=lzma.CHECK_CRC32)
        return lzc.compress(data) + lzc.flush()

    def bz2_compress(self, data):
        """
        Build bz2 compression

        :param data: json file to be compressed
        :rtype: object
        """

        return bz2.compress(data)


class Decompress:

    def zlib_decompress(self, data):
        """
        Build zlib decompression

        :param data: json file to be compressed
        :rtype: object
        """

        return zlib.decompress(data)

    def lzma_decompress(self, data):
        """
        Build lzma decompression

        :param data: json file to be compressed
        :rtype: object
        """

        lzcd = lzma.LZMADecompressor()
        return lzcd.decompress(data)

    def bz2_decompress(self, data):
        """
        Build bz2 decompression

        :param data: json file to be compressed
        :rtype: object
        """

        return bz2.decompress(data)


class Main:

    """
    Main class to run the program
    """

    c = Compress()
    d = Decompress()
    print("Opening Json file to compress and decompress!!")
    time.sleep(2)
    payload = open('jsonWebsite.json', 'rb')
    data = payload.read()
    print("Json file opened and read!")
    time.sleep(1)
    print("Getting data")
    time.sleep(2)
#    print(data)

    def zlib_compress_decompress(self):

        """
        Perform zlib compression/decompression

        :rtype: none
        """


        print("Time to compress your feelings!")
        print("Compressing :(")
        zlibcompressed = c.zlib_compress(self.data)
        print("The size of compressed object is:", sys.getsizeof(zlibcompressed))
        time.sleep(1)
        print("Compressed :'(")
        print(zlibcompressed)
        checksum = zlib.crc32(self.data)
        time.sleep(1)
        print("Time to decompress those bad feelings!")
        time.sleep(1)
        print(":)")
        print("Decompressing")
        zlibdecompressed = d.zlib_decompress(zlibcompressed)
        print("The size of decompressed object is", sys.getsizeof(zlibdecompressed))
        checksumGen = zlib.crc32(zlibdecompressed)
        print("You have been decompressed!")
        print(zlibdecompressed)
        if checksum == checksumGen:
            print("Checksum matches")

        else:
            print("Checksum mismatch")

    def lzma_compress_decompress(self):
        """
        Perform lzma compression/decompression

        :rtype: none
        """
        try:
             print("Oh no! Here comes lady lzma to ruin your life!!!!")
             print("Compressing :(")
             time.sleep(1)
             lzmacompressed = c.lzma_compress(self.data)
             print("She has compressed your feelings and here they are!")
             time.sleep(1)
             print(lzmacompressed)
             print("The size of compressed object is:", sys.getsizeof(lzmacompressed))
             time.sleep(1)
             print("After life hits you, you finally find a way to decompress those feelings! LET THEM OUT")
        time.sleep(1)
        lzmadecompressed = d.lzma_decompress(lzmacompressed)
        print("The size of decompressed object is:", sys.getsizeof(lzmadecompressed))
        time.sleep(2)
        if self.data == d.lzma_decompress(lzmacompressed):
            print("Checksum matches")

        else:
            print("Checksum mismatch")

    def bz2_compress_decompress(self):
        """
        Perform bz2 compression/decompression

        :rtype: none
        """
        try:
            print("Compressing")
            time.sleep(1)
            bz2compressed = c.bz2_compress(self.data)
            print("Data is compressed here is the data!")
            print(bz2compressed)
            print("The size of compressed object is:", sys.getsizeof(bz2compressed))
            time.sleep(1)
            print("Time to decompress the data since we need to")
            print("Decompressing...")
            time.sleep(1)
            bz2decompressed = d.bz2_decompress(bz2compressed)
            print("The size of compressed object is:", sys.getsizeof(bz2decompressed))
            print("The 'data' is decompressed")
            print(bz2decompressed)
            if self.data == bz2decompressed:
                print("Checksum matches")

            else:
                print("Checksum mismatch")
        except Exception as e:
            print ("Error %s" % e.args[0])


if __name__ == '__main__':
    c = Compress()
    d = Decompress()
    m = Main()
    m.zlib_compress_decompress()
    m.lzma_compress_decompress()
    m.bz2_compress_decompress()
