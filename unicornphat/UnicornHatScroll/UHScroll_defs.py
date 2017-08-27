'''This file contains all the letter designs as an 8x8 bitarray. 
You can add your won by just folowing the same format. Don't forget to specify the character 
to which it relates to in the mapping dictionary. 

Currently only uppercase letter are defined. Any message enetered with lowercase chars will
automatically be rendered in uppercase

If you try to create a scrolling message using another undefined character it will be displayed as an
underscore (_)

'''

from bitarray import bitarray


# Letter space
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('00000000')
x3= bitarray('00000000')
x4= bitarray('00000000')
x5= bitarray('00000000')
x6= bitarray('00000000')
x7= bitarray('00000000')
letter_space=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter A
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100100')
x3= bitarray('00111100')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00100100')
x7= bitarray('00000000')
letter_A=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter B
x0= bitarray('00000000')
x1= bitarray('00111000')
x2= bitarray('00100100')
x3= bitarray('00111000')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00111000')
x7= bitarray('00000000')
letter_B=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter C
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100000')
x3= bitarray('00100000')
x4= bitarray('00100000')
x5= bitarray('00100000')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_C=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter D
x0= bitarray('00000000')
x1= bitarray('00111000')
x2= bitarray('00100100')
x3= bitarray('00100100')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00111000')
x7= bitarray('00000000')
letter_D=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter E
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100000')
x3= bitarray('00111100')
x4= bitarray('00100000')
x5= bitarray('00100000')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_E=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter F
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100000')
x3= bitarray('00111100')
x4= bitarray('00100000')
x5= bitarray('00100000')
x6= bitarray('00100000')
x7= bitarray('00000000')
letter_F=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter G
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100000')
x3= bitarray('00100000')
x4= bitarray('00101100')
x5= bitarray('00100100')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_G=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter H
x0= bitarray('00000000')
x1= bitarray('00100100')
x2= bitarray('00100100')
x3= bitarray('00111100')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00100100')
x7= bitarray('00000000')
letter_H=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter I
x0= bitarray('00000000')
x1= bitarray('00011100')
x2= bitarray('00001000')
x3= bitarray('00001000')
x4= bitarray('00001000')
x5= bitarray('00001000')
x6= bitarray('00011100')
x7= bitarray('00000000')
letter_I=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter J
x0= bitarray('00000000')
x1= bitarray('00011100')
x2= bitarray('00001000')
x3= bitarray('00001000')
x4= bitarray('00001000')
x5= bitarray('00001000')
x6= bitarray('00011000')
x7= bitarray('00000000')
letter_J=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter K
x0= bitarray('00000000')
x1= bitarray('00100100')
x2= bitarray('00100100')
x3= bitarray('00101000')
x4= bitarray('00110000')
x5= bitarray('00101000')
x6= bitarray('00100100')
x7= bitarray('00000000')
letter_K=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter L
x0= bitarray('00000000')
x1= bitarray('00100000')
x2= bitarray('00100000')
x3= bitarray('00100000')
x4= bitarray('00100000')
x5= bitarray('00100000')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_L=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter M
x0= bitarray('00000000')
x1= bitarray('01111100')
x2= bitarray('01010100')
x3= bitarray('01010100')
x4= bitarray('01010100')
x5= bitarray('01010100')
x6= bitarray('01010100')
x7= bitarray('00000000')
letter_M=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter N
x0= bitarray('00000000')
x1= bitarray('00100100')
x2= bitarray('00100100')
x3= bitarray('00110100')
x4= bitarray('00101100')
x5= bitarray('00100100')
x6= bitarray('00100100')
x7= bitarray('00000000')
letter_N=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter O
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100100')
x3= bitarray('00100100')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_O=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter P
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100100')
x3= bitarray('00111100')
x4= bitarray('00100000')
x5= bitarray('00100000')
x6= bitarray('00100000')
x7= bitarray('00000000')
letter_P=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter Q
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100100')
x3= bitarray('00100100')
x4= bitarray('00100100')
x5= bitarray('00101100')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_Q=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter R
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100100')
x3= bitarray('00111100')
x4= bitarray('00110000')
x5= bitarray('00101000')
x6= bitarray('00100100')
x7= bitarray('00000000')
letter_R=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter S
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100000')
x3= bitarray('00111100')
x4= bitarray('00000100')
x5= bitarray('00000100')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_S=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter T
x0= bitarray('00000000')
x1= bitarray('00011100')
x2= bitarray('00001000')
x3= bitarray('00001000')
x4= bitarray('00001000')
x5= bitarray('00001000')
x6= bitarray('00001000')
x7= bitarray('00000000')
letter_T=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter U
x0= bitarray('00000000')
x1= bitarray('00100100')
x2= bitarray('00100100')
x3= bitarray('00100100')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_U=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter V
x0= bitarray('00000000')
x1= bitarray('00100100')
x2= bitarray('00100100')
x3= bitarray('00100100')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00011000')
x7= bitarray('00000000')
letter_V=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter W
x0= bitarray('00000000')
x1= bitarray('01010100')
x2= bitarray('01010100')
x3= bitarray('01010100')
x4= bitarray('01010100')
x5= bitarray('01010100')
x6= bitarray('01111100')
x7= bitarray('00000000')
letter_W=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter X
x0= bitarray('00000000')
x1= bitarray('00100100')
x2= bitarray('00100100')
x3= bitarray('00011000')
x4= bitarray('00011000')
x5= bitarray('00100100')
x6= bitarray('00100100')
x7= bitarray('00000000')
letter_X=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter Y
x0= bitarray('00000000')
x1= bitarray('00100100')
x2= bitarray('00100100')
x3= bitarray('00111100')
x4= bitarray('00000100')
x5= bitarray('00000100')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_Y=[x0,x1,x2,x3,x4,x5,x6,x7]

# Letter Z
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00000100')
x3= bitarray('00001000')
x4= bitarray('00010000')
x5= bitarray('00100000')
x6= bitarray('00111100')
x7= bitarray('00000000')
letter_Z=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 0
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00110100')
x3= bitarray('00100100')
x4= bitarray('00100100')
x5= bitarray('00101100')
x6= bitarray('00111100')
x7= bitarray('00000000')
number_0=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 1
x0= bitarray('00000000')
x1= bitarray('00011000')
x2= bitarray('00001000')
x3= bitarray('00001000')
x4= bitarray('00001000')
x5= bitarray('00001000')
x6= bitarray('00011100')
x7= bitarray('00000000')
number_1=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 2
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00000100')
x3= bitarray('00000100')
x4= bitarray('00111000')
x5= bitarray('00100000')
x6= bitarray('00111100')
x7= bitarray('00000000')
number_2=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 3
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00000100')
x3= bitarray('00000100')
x4= bitarray('00111100')
x5= bitarray('00000100')
x6= bitarray('00111100')
x7= bitarray('00000000')
number_3=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 4
x0= bitarray('00000000')
x1= bitarray('00100100')
x2= bitarray('00100100')
x3= bitarray('00111100')
x4= bitarray('00000100')
x5= bitarray('00000100')
x6= bitarray('00000100')
x7= bitarray('00000000')
number_4=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number S
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100000')
x3= bitarray('00011100')
x4= bitarray('00000100')
x5= bitarray('00000100')
x6= bitarray('00111100')
x7= bitarray('00000000')
number_5=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 6
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100000')
x3= bitarray('00111100')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00111100')
x7= bitarray('00000000')
number_6=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 7
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00000100')
x3= bitarray('00000100')
x4= bitarray('00000100')
x5= bitarray('00000100')
x6= bitarray('00000100')
x7= bitarray('00000000')
number_7=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 8
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100100')
x3= bitarray('00111100')
x4= bitarray('00100100')
x5= bitarray('00100100')
x6= bitarray('00111100')
x7= bitarray('00000000')
number_8=[x0,x1,x2,x3,x4,x5,x6,x7]

# Number 9
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100100')
x3= bitarray('00111100')
x4= bitarray('00000100')
x5= bitarray('00000100')
x6= bitarray('00111100')
x7= bitarray('00000000')
number_9=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol -
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('00000000')
x3= bitarray('00111100')
x4= bitarray('00000000')
x5= bitarray('00000000')
x6= bitarray('00000000')
x7= bitarray('00000000')
symbol_hyph=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol dot
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('00000000')
x3= bitarray('00000000')
x4= bitarray('00000000')
x5= bitarray('00001100')
x6= bitarray('00001100')
x7= bitarray('00000000')
symbol_dot=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol at
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00101100')
x3= bitarray('00101100')
x4= bitarray('00111100')
x5= bitarray('00100100')
x6= bitarray('00111000')
x7= bitarray('00000000')
symbol_at=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol ?
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00000100')
x3= bitarray('00111100')
x4= bitarray('00100000')
x5= bitarray('00100000')
x6= bitarray('00100000')
x7= bitarray('00000000')
symbol_qm=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol !
x0= bitarray('00000000')
x1= bitarray('00001000')
x2= bitarray('00001000')
x3= bitarray('00001000')
x4= bitarray('00001000')
x5= bitarray('00000000')
x6= bitarray('00001000')
x7= bitarray('00000000')
symbol_em=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol _
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('00000000')
x3= bitarray('00000000')
x4= bitarray('00000000')
x5= bitarray('00000000')
x6= bitarray('00111100')
x7= bitarray('00000000')
symbol_under=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol hash
x0= bitarray('00000000')
x1= bitarray('00101000')
x2= bitarray('01111100')
x3= bitarray('00101000')
x4= bitarray('00101000')
x5= bitarray('01111100')
x6= bitarray('00101000')
x7= bitarray('00000000')
symbol_hash=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol plus
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('00000000')
x3= bitarray('00001000')
x4= bitarray('00011100')
x5= bitarray('00001000')
x6= bitarray('00000000')
x7= bitarray('00000000')
symbol_plus=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol equals
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('00000000')
x3= bitarray('00111100')
x4= bitarray('00000000')
x5= bitarray('00111100')
x6= bitarray('00000000')
x7= bitarray('00000000')
symbol_equals=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol dollar
x0= bitarray('00000000')
x1= bitarray('00111100')
x2= bitarray('00100000')
x3= bitarray('00111100')
x4= bitarray('00010100')
x5= bitarray('00111100')
x6= bitarray('00010000')
x7= bitarray('00000000')
symbol_dollar=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol ast
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('01010100')
x3= bitarray('00111000')
x4= bitarray('01111100')
x5= bitarray('00111000')
x6= bitarray('01010100')
x7= bitarray('00000000')
symbol_ast=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol cb
x0= bitarray('00000000')
x1= bitarray('00010000')
x2= bitarray('00001000')
x3= bitarray('00000100')
x4= bitarray('00000100')
x5= bitarray('00001000')
x6= bitarray('00010000')
x7= bitarray('00000000')
symbol_cb=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol ob
x0= bitarray('00000000')
x1= bitarray('00000100')
x2= bitarray('00001000')
x3= bitarray('00010000')
x4= bitarray('00010000')
x5= bitarray('00001000')
x6= bitarray('00000100')
x7= bitarray('00000000')
symbol_ob=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol dbq
x0= bitarray('00000000')
x1= bitarray('00101000')
x2= bitarray('00101000')
x3= bitarray('00000000')
x4= bitarray('00000000')
x5= bitarray('00000000')
x6= bitarray('00000000')
x7= bitarray('00000000')
symbol_dbq=[x0,x1,x2,x3,x4,x5,x6,x7]


# Symbol gt
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('00110000')
x3= bitarray('00011000')
x4= bitarray('00000100')
x5= bitarray('00011000')
x6= bitarray('00110000')
x7= bitarray('00000000')
symbol_gt=[x0,x1,x2,x3,x4,x5,x6,x7]

# Symbol lt
x0= bitarray('00000000')
x1= bitarray('00000000')
x2= bitarray('00001100')
x3= bitarray('00011000')
x4= bitarray('00100000')
x5= bitarray('00011000')
x6= bitarray('00001100')
x7= bitarray('00000000')
symbol_lt=[x0,x1,x2,x3,x4,x5,x6,x7]

# Special hart
x0= bitarray('00000000')
x1= bitarray('01100110')
x2= bitarray('11111111')
x3= bitarray('11111111')
x4= bitarray('11111111')
x5= bitarray('01111110')
x6= bitarray('00111100')
x7= bitarray('00011000')
special_hart=[x0,x1,x2,x3,x4,x5,x6,x7]

# Special smilie
x0= bitarray('00111100')
x1= bitarray('01000010')
x2= bitarray('10100101')
x3= bitarray('10000001')
x4= bitarray('10100101')
x5= bitarray('10011001')
x6= bitarray('01000010')
x7= bitarray('00111100')
special_smilie=[x0,x1,x2,x3,x4,x5,x6,x7]

# Special degrees
x0= bitarray('00000000')
x1= bitarray('00011100')
x2= bitarray('00010100')
x3= bitarray('00011100')
x4= bitarray('00000000')
x5= bitarray('00000000')
x6= bitarray('00000000')
x7= bitarray('00000000')
special_degrees=[x0,x1,x2,x3,x4,x5,x6,x7]

'''The mapping dictionary is called to translate a character from the message to be displayed
into the relevant bitarray'''

mapping = {}
mapping['A'] = letter_A
mapping['B'] = letter_B
mapping['C'] = letter_C
mapping['D'] = letter_D
mapping['E'] = letter_E
mapping['F'] = letter_F
mapping['G'] = letter_G
mapping['H'] = letter_H
mapping['I'] = letter_I
mapping['J'] = letter_J
mapping['K'] = letter_K
mapping['L'] = letter_L
mapping['M'] = letter_M
mapping['N'] = letter_N
mapping['O'] = letter_O
mapping['P'] = letter_P
mapping['Q'] = letter_Q
mapping['R'] = letter_R
mapping['S'] = letter_S
mapping['T'] = letter_T
mapping['U'] = letter_U
mapping['V'] = letter_V
mapping['W'] = letter_W
mapping['X'] = letter_X
mapping['Y'] = letter_Y
mapping['Z'] = letter_Z
mapping['0'] = number_0
mapping['1'] = number_1
mapping['2'] = number_2
mapping['3'] = number_3
mapping['4'] = number_4
mapping['5'] = number_5
mapping['6'] = number_6
mapping['7'] = number_7
mapping['8'] = number_8
mapping['9'] = number_9
mapping['@'] = symbol_at
mapping['.'] = symbol_dot
mapping['-'] = symbol_hyph
mapping['?'] = symbol_qm
mapping['!'] = symbol_em
mapping[' '] = letter_space
mapping['_'] = symbol_under
mapping['#'] = symbol_hash
mapping['+'] = symbol_plus
mapping['='] = symbol_equals

mapping['$'] = symbol_dollar
mapping['"'] = symbol_dbq
mapping[')'] = symbol_cb
mapping['('] = symbol_ob
mapping['*'] = symbol_ast
mapping['>'] = symbol_gt
mapping['<'] = symbol_lt
mapping['heart'] = special_hart
mapping['smile'] = special_smilie
mapping['degrs'] = special_degrees


'''Characters are normally 4x6 high although some (e.g m, w) are wider and others are narrower 
(e.g. !, I, J). In order for these to be proiperly spaced in a word (i.e seperated by 2 blank columns,
any additional wide or narrow letters must be added to the appropriate list)'''

narrows = [symbol_plus,letter_I,letter_J,letter_T,symbol_em, symbol_ob, symbol_cb,symbol_plus]
super_narrow = [letter_space,special_degrees]
wides = [letter_M,letter_W,symbol_ast,symbol_hash,special_smilie, special_hart]
super_wides = [special_smilie, special_hart]
specials = ['~heart','~smile','~degrs']