#Coerção de tipos (covnertendo um tipo para outro)

#Conversao de tipos, coerção
#Type convertion, typecasting, coercion
#é o ato de converter um tipo em outro
#tipos imutaveis e primitivos:
#str, int, float, bool

print('1', type('1'), sep=', ')  # '1' é uma string

print(int('1'), type(int('1')), sep=', ')  # '1' convertido para int
print(type(float('1')+1), sep=', ')  # '1' convertido para float e somado com 1
print(bool(' '))  # ' ' (string com espaço) é True, pois não é vazia
print(bool(''))  # '' (string vazia) é False
print(str(11) + 'b')  # 11 convertido para string e concatenado com 'b'