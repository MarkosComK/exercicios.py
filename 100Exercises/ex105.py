def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: um ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dic = {}
    total = []
    total = notas
    maior = menor = c = 0
    for nota in notas:
        if c == 0:
            maior = nota
            menor = nota
            c +=1
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    dic['maior'] = maior
    dic['menor'] = menor
    dic['total'] = len(total)
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(total)
    dic['média'] = media
    if sit:
        if media >= 7:
            dic['situação'] = 'OK'
        if media < 5:
            dic['situação'] = 'RUIM'
        if 5 <= media < 7:
            dic['situação'] = 'RECUPERAÇÃO'
        if media == 10:
            dic['situação'] = 'EXCELENTE!'
    return dic

resp = notas(2, 10, 7, 10)
print(resp)