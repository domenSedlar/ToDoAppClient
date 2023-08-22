from num_base_conv import Convert_Base
import copy

cb = Convert_Base()

class AES:
    def __init__(self, key=[[int('2b', 16), int('28', 16), int('ab', 16), 9],
                 [int('7e', 16), int('ae', 16), int('f7', 16), int('cf', 16)],
                 [int('15', 16), int('d2', 16), int('15', 16), int('4f', 16)],
                [int('16', 16), int('a6', 16), int('88', 16), int('3c', 16)]]):
        self.matrix = [[2, 3, 1, 1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
        self.r_matrix = [[14, 11, 13, 9],[9, 14 , 11, 13],[13, 9, 14, 11],[11, 13, 9, 14]]

        self.key = key
        self.aes_sbox = [
            [int('63', 16), int('7c', 16), int('77', 16), int('7b', 16), int('f2', 16), int('6b', 16), int('6f', 16),
             int('c5', 16), int(
                '30', 16), int('01', 16), int('67', 16), int('2b', 16), int('fe', 16), int('d7', 16), int('ab', 16),
             int('76', 16)],
            [int('ca', 16), int('82', 16), int('c9', 16), int('7d', 16), int('fa', 16), int('59', 16), int('47', 16),
             int('f0', 16), int(
                'ad', 16), int('d4', 16), int('a2', 16), int('af', 16), int('9c', 16), int('a4', 16), int('72', 16),
             int('c0', 16)],
            [int('b7', 16), int('fd', 16), int('93', 16), int('26', 16), int('36', 16), int('3f', 16), int('f7', 16),
             int('cc', 16), int(
                '34', 16), int('a5', 16), int('e5', 16), int('f1', 16), int('71', 16), int('d8', 16), int('31', 16),
             int('15', 16)],
            [int('04', 16), int('c7', 16), int('23', 16), int('c3', 16), int('18', 16), int('96', 16), int('05', 16),
             int('9a', 16), int(
                '07', 16), int('12', 16), int('80', 16), int('e2', 16), int('eb', 16), int('27', 16), int('b2', 16),
             int('75', 16)],
            [int('09', 16), int('83', 16), int('2c', 16), int('1a', 16), int('1b', 16), int('6e', 16), int('5a', 16),
             int('a0', 16), int(
                '52', 16), int('3b', 16), int('d6', 16), int('b3', 16), int('29', 16), int('e3', 16), int('2f', 16),
             int('84', 16)],
            [int('53', 16), int('d1', 16), int('00', 16), int('ed', 16), int('20', 16), int('fc', 16), int('b1', 16),
             int('5b', 16), int(
                '6a', 16), int('cb', 16), int('be', 16), int('39', 16), int('4a', 16), int('4c', 16), int('58', 16),
             int('cf', 16)],
            [int('d0', 16), int('ef', 16), int('aa', 16), int('fb', 16), int('43', 16), int('4d', 16), int('33', 16),
             int('85', 16), int(
                '45', 16), int('f9', 16), int('02', 16), int('7f', 16), int('50', 16), int('3c', 16), int('9f', 16),
             int('a8', 16)],
            [int('51', 16), int('a3', 16), int('40', 16), int('8f', 16), int('92', 16), int('9d', 16), int('38', 16),
             int('f5', 16), int(
                'bc', 16), int('b6', 16), int('da', 16), int('21', 16), int('10', 16), int('ff', 16), int('f3', 16),
             int('d2', 16)],
            [int('cd', 16), int('0c', 16), int('13', 16), int('ec', 16), int('5f', 16), int('97', 16), int('44', 16),
             int('17', 16), int(
                'c4', 16), int('a7', 16), int('7e', 16), int('3d', 16), int('64', 16), int('5d', 16), int('19', 16),
             int('73', 16)],
            [int('60', 16), int('81', 16), int('4f', 16), int('dc', 16), int('22', 16), int('2a', 16), int('90', 16),
             int('88', 16), int(
                '46', 16), int('ee', 16), int('b8', 16), int('14', 16), int('de', 16), int('5e', 16), int('0b', 16),
             int('db', 16)],
            [int('e0', 16), int('32', 16), int('3a', 16), int('0a', 16), int('49', 16), int('06', 16), int('24', 16),
             int('5c', 16), int(
                'c2', 16), int('d3', 16), int('ac', 16), int('62', 16), int('91', 16), int('95', 16), int('e4', 16),
             int('79', 16)],
            [int('e7', 16), int('c8', 16), int('37', 16), int('6d', 16), int('8d', 16), int('d5', 16), int('4e', 16),
             int('a9', 16), int(
                '6c', 16), int('56', 16), int('f4', 16), int('ea', 16), int('65', 16), int('7a', 16), int('ae', 16),
             int('08', 16)],
            [int('ba', 16), int('78', 16), int('25', 16), int('2e', 16), int('1c', 16), int('a6', 16), int('b4', 16),
             int('c6', 16), int(
                'e8', 16), int('dd', 16), int('74', 16), int('1f', 16), int('4b', 16), int('bd', 16), int('8b', 16),
             int('8a', 16)],
            [int('70', 16), int('3e', 16), int('b5', 16), int('66', 16), int('48', 16), int('03', 16), int('f6', 16),
             int('0e', 16), int(
                '61', 16), int('35', 16), int('57', 16), int('b9', 16), int('86', 16), int('c1', 16), int('1d', 16),
             int('9e', 16)],
            [int('e1', 16), int('f8', 16), int('98', 16), int('11', 16), int('69', 16), int('d9', 16), int('8e', 16),
             int('94', 16), int(
                '9b', 16), int('1e', 16), int('87', 16), int('e9', 16), int('ce', 16), int('55', 16), int('28', 16),
             int('df', 16)],
            [int('8c', 16), int('a1', 16), int('89', 16), int('0d', 16), int('bf', 16), int('e6', 16), int('42', 16),
             int('68', 16), int(
                '41', 16), int('99', 16), int('2d', 16), int('0f', 16), int('b0', 16), int('54', 16), int('bb', 16),
             int('16', 16)]
        ]
        self.aes_rsbox = [
            [int('52', 16), int('09', 16), int('6a', 16), int('d5', 16), int('30', 16), int('36', 16), int('a5', 16),
             int('38', 16), int(
                'bf', 16), int('40', 16), int('a3', 16), int('9e', 16), int('81', 16), int('f3', 16), int('d7', 16),
             int('fb', 16)],
            [int('7c', 16), int('e3', 16), int('39', 16), int('82', 16), int('9b', 16), int('2f', 16), int('ff', 16),
             int('87', 16), int(
                '34', 16), int('8e', 16), int('43', 16), int('44', 16), int('c4', 16), int('de', 16), int('e9', 16),
             int('cb', 16)],
            [int('54', 16), int('7b', 16), int('94', 16), int('32', 16), int('a6', 16), int('c2', 16), int('23', 16),
             int('3d', 16), int(
                'ee', 16), int('4c', 16), int('95', 16), int('0b', 16), int('42', 16), int('fa', 16), int('c3', 16),
             int('4e', 16)],
            [int('08', 16), int('2e', 16), int('a1', 16), int('66', 16), int('28', 16), int('d9', 16), int('24', 16),
             int('b2', 16), int(
                '76', 16), int('5b', 16), int('a2', 16), int('49', 16), int('6d', 16), int('8b', 16), int('d1', 16),
             int('25', 16)],
            [int('72', 16), int('f8', 16), int('f6', 16), int('64', 16), int('86', 16), int('68', 16), int('98', 16),
             int('16', 16), int(
                'd4', 16), int('a4', 16), int('5c', 16), int('cc', 16), int('5d', 16), int('65', 16), int('b6', 16),
             int('92', 16)],
            [int('6c', 16), int('70', 16), int('48', 16), int('50', 16), int('fd', 16), int('ed', 16), int('b9', 16),
             int('da', 16), int(
                '5e', 16), int('15', 16), int('46', 16), int('57', 16), int('a7', 16), int('8d', 16), int('9d', 16),
             int('84', 16)],
            [int('90', 16), int('d8', 16), int('ab', 16), int('00', 16), int('8c', 16), int('bc', 16), int('d3', 16),
             int('0a', 16), int(
                'f7', 16), int('e4', 16), int('58', 16), int('05', 16), int('b8', 16), int('b3', 16), int('45', 16),
             int('06', 16)],
            [int('d0', 16), int('2c', 16), int('1e', 16), int('8f', 16), int('ca', 16), int('3f', 16), int('0f', 16),
             int('02', 16), int(
                'c1', 16), int('af', 16), int('bd', 16), int('03', 16), int('01', 16), int('13', 16), int('8a', 16),
             int('6b', 16)],
            [int('3a', 16), int('91', 16), int('11', 16), int('41', 16), int('4f', 16), int('67', 16), int('dc', 16),
             int('ea', 16), int(
                '97', 16), int('f2', 16), int('cf', 16), int('ce', 16), int('f0', 16), int('b4', 16), int('e6', 16),
             int('73', 16)],
            [int('96', 16), int('ac', 16), int('74', 16), int('22', 16), int('e7', 16), int('ad', 16), int('35', 16),
             int('85', 16), int(
                'e2', 16), int('f9', 16), int('37', 16), int('e8', 16), int('1c', 16), int('75', 16), int('df', 16),
             int('6e', 16)],
            [int('47', 16), int('f1', 16), int('1a', 16), int('71', 16), int('1d', 16), int('29', 16), int('c5', 16),
             int('89', 16), int(
                '6f', 16), int('b7', 16), int('62', 16), int('0e', 16), int('aa', 16), int('18', 16), int('be', 16),
             int('1b', 16)],
            [int('fc', 16), int('56', 16), int('3e', 16), int('4b', 16), int('c6', 16), int('d2', 16), int('79', 16),
             int('20', 16), int(
                '9a', 16), int('db', 16), int('c0', 16), int('fe', 16), int('78', 16), int('cd', 16), int('5a', 16),
             int('f4', 16)],
            [int('1f', 16), int('dd', 16), int('a8', 16), int('33', 16), int('88', 16), int('07', 16), int('c7', 16),
             int('31', 16), int(
                'b1', 16), int('12', 16), int('10', 16), int('59', 16), int('27', 16), int('80', 16), int('ec', 16),
             int('5f', 16)],
            [int('60', 16), int('51', 16), int('7f', 16), int('a9', 16), int('19', 16), int('b5', 16), int('4a', 16),
             int('0d', 16), int(
                '2d', 16), int('e5', 16), int('7a', 16), int('9f', 16), int('93', 16), int('c9', 16), int('9c', 16),
             int('ef', 16)],
            [int('a0', 16), int('e0', 16), int('3b', 16), int('4d', 16), int('ae', 16), int('2a', 16), int('f5', 16),
             int('b0', 16), int(
                'c8', 16), int('eb', 16), int('bb', 16), int('3c', 16), int('83', 16), int('53', 16), int('99', 16),
             int('61', 16)],
            [int('17', 16), int('2b', 16), int('04', 16), int('7e', 16), int('ba', 16), int('77', 16), int('d6', 16),
             int('26', 16), int(
                'e1', 16), int('69', 16), int('14', 16), int('63', 16), int('55', 16), int('21', 16), int('0c', 16),
             int('7d', 16)]
        ]
        self.key_schedule = [
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        ]

        rcon = [[1,2,4,8,16,32,64,128,int('1b', 16),int('36', 16)],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
        rot_word = [self.key[1][3], self.key[2][3], self.key[3][3],self.key[0][3]]

        for b in range(len(rot_word)):
            byte = cb.to(rot_word[b], 16)
            if len(byte) > 1:
                rot_word[b] = self.aes_sbox[cb.back(byte[0], 16)][cb.back(byte[1], 16)]
            else:
                rot_word[b] = self.aes_sbox[0][cb.back(byte[0], 16)]

        for i in range(4):
            self.key_schedule[0][i][0] = self.key[i][0] ^ rot_word[i] ^ rcon[i][0]

        for c in range(1, 4):
            for r in range(4):
                self.key_schedule[0][r][c] = self.key[r][c] ^ self.key_schedule[0][r][c - 1]

        for ro in range(1, 10):
            rot_word = [self.key_schedule[ro - 1][1][3], self.key_schedule[ro - 1][2][3], self.key_schedule[ro - 1][3][3], self.key_schedule[ro - 1][0][3]]

            for b in range(len(rot_word)):
                byte = cb.to(rot_word[b], 16)
                if len(byte) > 1:
                    rot_word[b] = self.aes_sbox[cb.back(byte[0], 16)][cb.back(byte[1], 16)]
                else:
                    rot_word[b] = self.aes_sbox[0][cb.back(byte[0], 16)]

            for i in range(4):
                self.key_schedule[ro][i][0] = self.key_schedule[ro - 1][i][0] ^ rot_word[i] ^ rcon[i][ro]

            for c in range(1, 4):
                for r in range(4):
                    self.key_schedule[ro][r][c] = self.key_schedule[ro - 1][r][c] ^ self.key_schedule[ro][r][c - 1]

    def sub_bytes(self, block):
        for i in range(len(block)):
            for b in range(len(block[i])):
                byte = cb.to(block[i][b], 16)
                if len(byte) > 1:
                    block[i][b] = self.aes_sbox[cb.back(byte[0], 16)][cb.back(byte[1], 16)]
                else:
                    block[i][b] = self.aes_sbox[0][cb.back(byte[0], 16)]

        return block

    def unsub_bytes(self, block):
        for i in range(len(block)):
            for b in range(len(block[i])):
                byte = cb.to(block[i][b], 16)
                if len(byte) > 1:
                    block[i][b] = self.aes_rsbox[cb.back(byte[0], 16)][cb.back(byte[1], 16)]
                else:
                    block[i][b] = self.aes_rsbox[0][cb.back(byte[0], 16)]


        return block

    def shift_rows(self, array):
        state = array
        for ii in range(4):
            row = state[ii][:]
            for i in range(4):
                j = i - ii
                state[ii][j] = row[i]

        return state

    def unshift_rows(self, state):
        for i in range(4):
            row = state[i][:]
            new_row1 = []
            new_row1 = new_row1 + row[0:4-i]
            new_row2 = []

            j = i
            k = 0
            while j + k != 0:
                k = k - 1
                new_row2.insert(0, row[k])
            new_row = new_row2 + new_row1
            state[i] = new_row

        return state

    def times_two(self, number):
        number = number * 2
        if number > 255:
            number = number - 256
            number = number ^ 27

        return number

    def mix_collums(self, block):

        state = copy.deepcopy(block)

        for collum in range(4):

            for row in range(4):
                to_add = []
                for step in range(4):
                    if self.matrix[row][step] == 1:
                        to_add.append(copy.deepcopy(block[step][collum]))
                    elif self.matrix[row][step] == 2:
                        to_add.append(self.times_two(copy.deepcopy(block[step][collum])))
                    else:
                        a = self.times_two(copy.deepcopy(block[step][collum]))
                        a = a ^ block[step][collum]
                        to_add.append(a)

                added = 0
                for i in to_add:
                    added = i ^ added

                state[row][collum] = added

        return state

    def unmix_collums(self, block):

        state = copy.deepcopy(block)

        for collum in range(4):

            for row in range(4):
                to_add = []
                for step in range(4):
                    if self.r_matrix[row][step] == 9:
                        #x×9 = (((x×2)×2)×2) + x
                        x = copy.deepcopy(block[step][collum])
                        x = self.times_two(x)
                        x = self.times_two(x)
                        x = self.times_two(x)
                        x = x ^ block[step][collum]

                        to_add.append(x)

                    elif self.r_matrix[row][step] == 11:
                        # x×11 = ((((x×2)×2) + x)×2) + x
                        x = copy.deepcopy(block[step][collum])
                        x = self.times_two(x)
                        x = self.times_two(x)
                        x = x ^ block[step][collum]
                        x = self.times_two(x)
                        x = x ^ block[step][collum]

                        to_add.append(x)

                    elif self.r_matrix[row][step] == 13:
                        # x×13 = ((((x×2) + x)×2)×2) + x
                        x = copy.deepcopy(block[step][collum])
                        x = self.times_two(x)
                        x = x ^ block[step][collum]
                        x = self.times_two(x)
                        x = self.times_two(x)
                        x = x ^ block[step][collum]

                        to_add.append(x)

                    else:
                    #x×14 = ((((x×2) + x)×2) + x)×2
                        x = copy.deepcopy(block[step][collum])
                        x = self.times_two(x)
                        x = x ^ block[step][collum]
                        x = self.times_two(x)
                        x = x ^ block[step][collum]
                        x = self.times_two(x)

                        to_add.append(x)

                added = 0
                for i in to_add:
                    added = i ^ added

                state[row][collum] = added

        return state

    def add_key(self, block, round):
        for i in range(4):
            for ii in range(4):
                block[i][ii] = block[i][ii]
                block[i][ii] = block[i][ii] ^ self.key_schedule[round][i][ii]

        for i in range(4):
            for ii in range(4):
                block[i][ii] = block[i][ii]

        return block

    def enyc_block(self, block):
        for i in range(9):
            block = self.sub_bytes(block)
            block = self.shift_rows(block)
            block = self.mix_collums(block)
            block = self.add_key(block, i)

        block = self.sub_bytes(block)
        block = self.shift_rows(block)
        block = self.add_key(block, 9)

        return block

    def deycp_block(self, block):
        block = self.add_key(block, 9)
        block = self.unshift_rows(block)
        block = self.unsub_bytes(block)

        for i in range(9):
            block = self.add_key(block, 8-i)
            block = self.unmix_collums(block)
            block = self.unshift_rows(block)
            block = self.unsub_bytes(block)

        return block

    def mk_block(self, s):
        s = s.encode()
        j = 0
        template = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for c in range(4):
            for r in range(4):
                template[r][c] = s[j]
                j += 1
        return template

    def enyc_string(self, plain_text):
        #b = plain_text.encode('UTF-8')
        while len(plain_text) % 16 != 0:
            plain_text += chr(0)
        b = bytearray(plain_text, "UTF-8")
        j = 0
        chipher = []
        for i in range(len(plain_text) // 16):
            template = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            for c in range(4):
                for r in range(4):
                    template[r][c] = b[j]
                    j += 1

            chipher.append(self.enyc_block(template))

        chipher_text = ""

        for i in chipher:
            for r in i:
                for c in r:
                    chipher_text += str(c) + ";"

        return chipher_text

    def find_index(self, string, char, place):
        times = 0
        i = 0
        while times != place:
            if string[i] == char:
                times += 1
            i += 1
        return i - 1

    def deyc_string(self, chipher_text):
        deyc = []
        chipher = []
        j = 0
        p = 0

        for i in range(chipher_text.count(";") // 16):
            chipher.append([])
            for r in range(4):
                chipher[i].append([])
                for c in range(4):
                    p += 1
                    chipher[i][r].append(int(chipher_text[j:self.find_index(chipher_text, ";", p)]))
                    j += len(str(chipher[i][r][c])) + 1

        for i in chipher:
            deyc.append(self.deycp_block(i))

        plain_text = ""
        for b in deyc:
            for c in range(4):
                for r in range(4):
                    plain_text = plain_text + chr(b[r][c])

        return plain_text
