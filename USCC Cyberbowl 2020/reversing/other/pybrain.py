import random
import itertools
'''
BF_OP_GT = '>'
BF_OP_ADD = '+'
BF_OP_LBR = '['
BF_OP_LT = '<'
BF_OP_SUB = '-'
BF_OP_RBR = ']'
BF_OP_DOT = '.'
'''
BF_OP_GT = 'S'
BF_OP_ADD = 'N'
BF_OP_LBR = '!'
BF_OP_LT = 'B'
BF_OP_SUB = 'I'
BF_OP_RBR = 'O'
BF_OP_DOT = '.'

def bf_buildbracemap(code):
    temp_bracestack, bracemap = [], dict()
    for position, command in enumerate(code):
        if command == BF_OP_LBR:
            temp_bracestack.append(position)
        if command == BF_OP_RBR:
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start

    return bracemap


def bf_evaluate(code):
    code = ''.join(filter(lambda x: x in [BF_OP_GT, BF_OP_LT, BF_OP_ADD, BF_OP_SUB, BF_OP_LBR, BF_OP_RBR, BF_OP_DOT], code))
    bracemap = bf_buildbracemap(code)
    cells, codeptr, cellptr = [0], 0, 0
    std_out = ''
    num_iters = 0
    while codeptr < len(code) and num_iters < 1000000:
        command = code[codeptr]
        if command == BF_OP_GT:
            cellptr += 1
            if cellptr == len(cells):
                cells.append(0)
        if command == BF_OP_LT:
            cellptr = 0 if cellptr <= 0 else cellptr - 1
        if command == BF_OP_ADD:
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0
        if command == BF_OP_SUB:
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255
        if command == BF_OP_LBR:
            if cells[cellptr] == 0:
                codeptr = bracemap[codeptr]
        if command == BF_OP_RBR:
            if cells[cellptr] != 0:
                codeptr = bracemap[codeptr]
        if command == BF_OP_DOT:
            std_out += chr(cells[cellptr])
        codeptr += 1
        num_iters += 1
    
    if num_iters >= 1000000:
        return "TLE"
    return std_out


if __name__ == '__main__':
    print('Evaluating BF code...')
    bf_flag_code = 'SN!BIIIIIIIIISOIIIIIIIIIBN!OIII.BIIIISOIIIIBN!OIIII.NNN.BIIIIIIIISONNNNNNNNBN!ONNNNN.BIIIIIIIISOIIIIIIIIBN!OIIIIII.BIISOIIBN!OII.BIIISONNNBN!ONN.BIISOIIBN!OII.BIIIIIIIISONNNNNNNNBN!ONNNNNNN.BIIIIIIIISOIIIIIIIIBN!OIIIIIIIII.BIIISOIIIBN!OI.BIIIIIIISONNNNNNNBN!ONNNNNNNN.BIIIIISONNNNNBN!ON.BIIIIIIISOIIIIIIIBN!OIIII.NN.BIIIISONNNNBN!O..BIIIIIIISOIIIIIIIBN!OIIIIIII.BIIIIIISONNNNNNBN!ONNN.BIIIISOIIIIBN!OIIII.NNN.BIISONNBN!ONN.BIIISOIIIBN!OIIIII.II.IIII.I.BIIIISONNNNBN!ONNNNN.BIISOIIBN!OIII.NNNNN.BIIISOIIIBN!OIII.II.BIISOIIBN!OII.NN.BIIIISONNNNBN!ONNNN.BIISOIIBN!OII.BIIISOIIIBN!OIIIII.NNNN.NNN.BIIISONNNBN!ONN.BIIISOIIIBN!OIIII.BIISONNBN!ONNN.BIISONNBN!ONNNN.BIIISOIIIBN!OI.IIIII.BIIISONNNBN!ONNNNNN.BIIIISOIIIIBN!OIIIII.BIIISONNNBN!ONNN.NNN.BIISONNBN!ONN.BIIIISOIIIIBN!OIIIIIIII.BIISONNBN!ONNNN............III.BIISONNBN!ONN.BIISONNBN!ONNNN.BIIIIISOIIIIIBN!O.SN!'
    opcodes_raw = 'SN!BIO.'
    for opcodes in itertools.permutations(opcodes_raw):
        # print(opcodes)
        BF_OP_GT = opcodes[0]
        BF_OP_ADD = opcodes[1]
        BF_OP_LBR = opcodes[2]
        BF_OP_LT = opcodes[3]
        BF_OP_SUB = opcodes[4]
        BF_OP_RBR = opcodes[5]
        BF_OP_DOT = opcodes[6]
        try:
            result = bf_evaluate(bf_flag_code)
            if 'USCC' in result:
                print(opcodes)
                print(result)
                input()
        except Exception as e:
            print(e)
