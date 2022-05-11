class Plugboard(object):
    def __init__(self, wires=""):
        """
        wires: This is the mapping of pairs of characters
        """
        if wires is None:
            raise Exception("Should not have accepted too many wires defined")
        length = len(str(wires))
        self.length_Str = str(wires)
        for s in self.length_Str:
            if self.length_Str.count(s) > 1:
                raise Exception("Should not have accepted a sencod definition for a wireend")
        print(f"length is {length}")
        if length > 20:
            raise Exception("Should not have accepted too many wires defined")
        if length % 2 == 1:
            raise Exception("Should not have accepted a partial wire definition")

    def process(self, c):
        """
        c: The single character to process
        """
        pos = self.length_Str.find(c)
        if pos >= 0:
            if pos % 2 == 0:
                return self.length_Str[pos + 1]
            else:
                return self.length_Str[pos - 1]
        else:
            return c

    def check_duplicate(self, test_char):
        if self.length_Str.count(test_char)

