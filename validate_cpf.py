def generatorCPF() -> str:
    from random import randint

    cpf = ''
    for _ in range(0, 9):
        cpf += str(randint(0, 9))
    cpf = validateCPF(cpf, generator=True)
    return cpf


def validateCPF(cpf: str, generator=False) -> bool | str:
    try:
        if cpf.count('.') > 0 or cpf.count('-') > 0:
            cpf = formatCPF(cpf)
        oldCpf = cpf
        if len(cpf) > 9 or not generator:
            cpf = cpf[:-2]

        cpf += digit_number(cpf, 10)
        cpf += digit_number(cpf, 11)

        if not generator:
            if cpf == oldCpf and not sequence_cpf(cpf):
                return True
            else:
                return False
        else:
            cpf = [cpf[:3] + '.', cpf[3:6] + '.', cpf[6:9] + '-', cpf[9:]]

            cpf = ''.join(cpf)
            return cpf
    except:
        return False


def digit_number(cpf, num_max):
    lista = []
    for ind, num in enumerate(range(num_max, 1, -1)):
        lista.append(int(cpf[ind]) * num)
    
    varTotal = 11 - (sum(lista) % 11)
    if varTotal > 9:
        varTotal = 0
    cpf_digit = str(varTotal)
    return cpf_digit


def sequence_cpf(cpf):
    return cpf == str(cpf[0]) * len(cpf)


def formatCPF(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    return cpf
