import unittest


class TestTextAlignJustify(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(justify('123 45 6', 7),  '123  45\n6')
        # self.assertEqual(justify('123 45 6 abc defgh i jk lmn opq rstu', 7),  '123  45\n6   abc\ndefgh i\njk  lmn\nopq\nrstu')
        self.assertEqual(justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.', 20),  '123  45\n6')

def one_line_justify(item_list, width):
    item_count = len(item_list)
    gap_count = item_count - 1
    if gap_count == 0: #Only has one item
        return item_list[0]
    items_len_sum = sum([len(item) for item in item_list])
    spcs = width - items_len_sum
    gap = spcs // gap_count
    add_one_idx = spcs % gap_count
    result = ''
    for idx, item in enumerate(item_list):
        if idx < gap_count:
            if add_one_idx > 0 and idx < add_one_idx:
                result += (item + (' ' * (gap+1)))
            else:
                result += (item + (' ' * gap))
        else:
            result += item
    
    return result



def justify(text, width):
    txt_list = text.split()
    
    #print quiz data
    # print(f"text={text}")
    # print(f"width={width}")

    #init 
    result = ''
    line_list = []
    w_left = width

    #Get each item one by one
    for item in txt_list:
        if w_left == len(item): #Just match the final space
            line_list.append(item)
            result += (one_line_justify(line_list, width) + '\n')
            line_list = []
            w_left = width
        elif w_left - len(item) > 0:  # Can add this item in current line
            w_left -= (len(item) + 1)  # 1 is for the gap of one space
            line_list.append(item)
        else: # Can't add this item in current line
            result += (one_line_justify(line_list, width) + '\n')
            line_list = [item]
            w_left = width - (len(item) + 1)

    if line_list: #The last line not process yet.
        last_line = " ".join(line_list)
        result += last_line
        # result += (one_line_justify(line_list, width) + '\n')

    return result.rstrip('\n')


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    print(justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.', 20))