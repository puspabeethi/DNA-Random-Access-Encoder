import math
import pandas as pd
import os

def encoder(oligo_length, folder_path):
    os.chdir(folder_path)
    data = []
    data_size = []
    m_p = math.ceil((oligo_length - 40) / 10) - 1
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{folder_path}\{file}"
            with open(file_path, 'r') as f:
                file_data = str(f.read())
                data.append(file_data)
                #file = open(file_name, "r")
                #data = str(file.read())
                file_data_size = len(file_data)
                data_size.append(file_data_size)
    file_count = len(data)
    os.chdir("..")
    M = 0
    total_data_size = 0
    for i in range(file_count):
        M = M + math.ceil(data_size[i] / (16 * m_p))
        total_data_size = total_data_size + data_size[i]
    if (M > 93756) and (m_p < 19):
        m_p = 19
    print('total data size = ' + str(total_data_size) + ' bits, number of oligos = ' + str(M))

    df = pd.read_excel('puspabeethis_files\PrimerList_400_with_RC.xlsx', sheet_name='200_primer_pairs', header=0)
    primers = df['Primers'].tolist()
    forward_primers = []
    reverse_primers_RC = []
    reverse_primers = []
    for i in range(file_count):
        forward_primers.append(primers[2*i])
        reverse_primers_RC.append(primers[2*i + 1])
        primer = primers[2*i + 1].replace("A", "1").replace("T", "0").replace("G", "3").replace("C", "2")
        primer = primer[::-1]
        primer = primer.replace("0", "A").replace("1", "T").replace("2", "G").replace("3", "C")
        reverse_primers.append(primer)
    writer = pd.ExcelWriter('Output_files\ForwardPrimers.xlsx', engine='xlsxwriter')
    writer.save()
    df = pd.DataFrame({'Primers': forward_primers})
    writer = pd.ExcelWriter('Output_files\ForwardPrimers.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name=str(file_count) +' forward primers', index=False)
    writer.save()
    writer = pd.ExcelWriter('Output_files\ReversePrimers.xlsx', engine='xlsxwriter')
    writer.save()
    df = pd.DataFrame({'Primers': reverse_primers})
    writer = pd.ExcelWriter('Output_files\ReversePrimers.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name=str(file_count) + ' reverse primers', index=False)
    writer.save()

    address = addressBook(M)
    codebook = subCode(M)

    oligo_num = 0
    for k in range(file_count):
        oligos = []
        file_M = math.ceil(data_size[k]/(16 * m_p))
        file_data = data[k]
        if data_size[k] % (16 * m_p) == 0:
            for i in range(file_M):
                payload = ''
                for j in range(m_p):
                    message = 256 * (128 * int(file_data[0]) + 64 * int(file_data[1]) + 32 * int(file_data[2]) + 16 * int(file_data[3]) + 8 * int(file_data[4]) + 4 * int(file_data[5]) + 2 * int(file_data[6]) + int(file_data[7])) + (128 * int(file_data[8]) + 64 * int(file_data[9]) + 32 * int(file_data[10]) + 16 * int(file_data[11]) + 8 * int(file_data[12]) + 4 * int(file_data[13]) + 2 * int(file_data[14]) + int(file_data[15]))
                    file_data = file_data[16:]
                    print(message, len(file_data))
                    payload = payload + codebook[message]
                print(len(payload), payload)
                primerF = forward_primers[k]
                primerRC = reverse_primers_RC[k]
                sequence = primerF + address[oligo_num] + payload + primerRC
                oligo_num += 1
                oligos.append(sequence)
            print(len(oligos), oligos)
        else:
            for i in range(file_M - 1):
                payload = ''
                for j in range(m_p):
                    message = 256 * (128 * int(file_data[0]) + 64 * int(file_data[1]) + 32 * int(file_data[2]) + 16 * int(file_data[3]) + 8 * int(file_data[4]) + 4 * int(file_data[5]) + 2 * int(file_data[6]) + int(file_data[7])) + (128 * int(file_data[8]) + 64 * int(file_data[9]) + 32 * int(file_data[10]) + 16 * int(file_data[11]) + 8 * int(file_data[12]) + 4 * int(file_data[13]) + 2 * int(file_data[14]) + int(file_data[15]))
                    file_data = file_data[16:]
                    print(message, len(file_data))
                    payload = payload + codebook[message]
                print(len(payload), payload)
                primerF = forward_primers[k]
                primerRC = reverse_primers_RC[k]
                sequence = primerF + address[oligo_num] + payload + primerRC
                oligo_num += 1
                oligos.append(sequence)
            print(len(oligos), oligos)
            rem = int(len(file_data)/16)
            junk_num = m_p - rem
            payload = ''
            for j in range(rem):
                message = 256 * (128 * int(file_data[0]) + 64 * int(file_data[1]) + 32 * int(file_data[2]) + 16 * int(
                    file_data[3]) + 8 * int(file_data[4]) + 4 * int(file_data[5]) + 2 * int(file_data[6]) + int(
                    file_data[7])) + (128 * int(file_data[8]) + 64 * int(file_data[9]) + 32 * int(
                    file_data[10]) + 16 * int(file_data[11]) + 8 * int(file_data[12]) + 4 * int(
                    file_data[13]) + 2 * int(file_data[14]) + int(file_data[15]))
                file_data = file_data[16:]
                print(message, len(file_data))
                payload = payload + codebook[message]
            payload = payload + Junk(junk_num)
            print(len(payload), payload)
            primerF = forward_primers[k]
            primerRC = reverse_primers_RC[k]
            sequence = primerF + address[oligo_num] + payload + primerRC
            oligo_num += 1
            oligos.append(sequence)
            print(len(oligos), oligos)
        index = []
        for i in range(file_M):
            index.append('>oligo_' + str(i + 1))
        print(index)
        file_text = []
        for j in range(file_M):
            file_text.append(index[j])
            file_text.append(oligos[j])
        print(file_text)
        print(len(file_text))
        fasta_file = open('Output_files\DNA_encoded_file'+str(k+1)+'_data.fasta', "w")
        for l in range(len(file_text)):
            fasta_file.write(file_text[l] + "\n")
        fasta_file.close()

def numberToBase(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    intTemp = digits[::-1]
    s = ""
    s = [s.join(str(j)) for j in intTemp]
    y = ""
    y = y.join(s)
    return y

def CountStringStreakBeginning(charVar):
    if len(charVar) == 1:
        return 1
    for i in range(1, len(charVar)):
        if charVar[i] != charVar[0]:
            return i
    return i + 1

def CountStringStreakEnding(charVar):
    if len(charVar) == 1:
        return 1
    for i in range(len(charVar) - 2, -1, -1):
        if charVar[i] != charVar[len(charVar) - 1]:
            return len(charVar) - (i + 1)
    return len(charVar) - i

def addressBook(M):
    if 1 <= M <= 8:
        n_a = 2
    elif 9 <= M <= 80:
        n_a = 4
    elif 81 <= M <= 504:
        n_a = 5
    elif 505 <= M <= 1008:
        n_a = 6
    elif 1009 <= M <= 6768:
        n_a = 7
    elif 6769 <= M <= 13278:
        n_a = 8
    elif 13279 <= M <= 93756:
        n_a = 9
    GC_LowerBound = math.ceil(.4 * n_a)
    GC_UpperBound = math.floor(.6 * n_a)
    l = math.floor(3 / 2)
    r = 3 - l
    ForbiddenString0 = '0'.rjust(3 + 1, '0')
    ForbiddenString1 = '1'.rjust(3 + 1, '1')
    ForbiddenString2 = '2'.rjust(3 + 1, '2')
    ForbiddenString3 = '3'.rjust(3 + 1, '3')
    TableData = []
    i = 0
    count = 0
    while i < 4 ** n_a:
        charVar = str(numberToBase(i, 4)).rjust(n_a, '0')
        if ((l != 0 and CountStringStreakBeginning(charVar) > l) or (r != 0 and CountStringStreakEnding(charVar) > r)) == False:
            if ForbiddenString0 not in charVar and ForbiddenString1 not in charVar and ForbiddenString2 not in charVar and ForbiddenString3 not in charVar:
                if (charVar.count('2') + charVar.count('3') >= GC_LowerBound) and (charVar.count('2') + charVar.count('3') <= GC_UpperBound):
                    charVar = charVar.replace("0", "A").replace("1", "T").replace("2", "G").replace("3", "C")
                    TableData.insert(count, charVar)
                    count += 1
        i += 1
    if n_a == 8:
        df = pd.read_excel('puspabeethis_files\common_address_len8.xlsx', sheet_name='common_address', header=0)
        common_address = df['common_address'].tolist()
    elif n_a == 9:
        df = pd.read_excel('puspabeethis_files\common_address_len9.xlsx', sheet_name='common_address', header=0)
        common_address = df['common_address'].tolist()
    else:
        common_address = []
    for j in range(len(common_address)):
        TableData.remove(common_address[j])
    TableData = TableData[0:M]
    writer = pd.ExcelWriter('Output_files\AddressBook.xlsx', engine='xlsxwriter')
    writer.save()
    df = pd.DataFrame({'Address': TableData})
    writer = pd.ExcelWriter('Output_files\AddressBook.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='BlockLength ' + str(n_a), index=False)
    writer.save()
    return TableData

def subCode(M):
    df = pd.read_excel('puspabeethis_files\CodeBook_large.xlsx', sheet_name='Min_HammingDistance_2', header=0)
    codebook_large = df['CodeBook_large'].tolist()
    TableData = codebook_large
    if 9 <= M <= 80:
        df = pd.read_excel('puspabeethis_files\common_codeword_len4.xlsx', sheet_name='common_codeword', header=0)
        common_codeword = df['common_codeword'].tolist()
    elif 81 <= M <= 504:
        df = pd.read_excel('puspabeethis_files\common_codeword_len5.xlsx', sheet_name='common_codeword', header=0)
        common_codeword = df['common_codeword'].tolist()
    elif 505 <= M <= 1008:
        df = pd.read_excel('puspabeethis_files\common_codeword_len6.xlsx', sheet_name='common_codeword', header=0)
        common_codeword = df['common_codeword'].tolist()
    elif 1009 <= M <= 6768:
        df = pd.read_excel('puspabeethis_files\common_codeword_len7.xlsx', sheet_name='common_codeword', header=0)
        common_codeword = df['common_codeword'].tolist()
    else:
        common_codeword = []
    for j in range(len(common_codeword)):
        TableData.remove(common_codeword[j])
    writer = pd.ExcelWriter('Output_files\CodeBook.xlsx', engine='xlsxwriter')
    writer.save()
    df = pd.DataFrame({'CodeBook': TableData})
    writer = pd.ExcelWriter('Output_files\CodeBook.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Min_HammingDistance_2', index=False)
    writer.save()
    return TableData

def Junk(junk_num):
    df = pd.read_excel('puspabeethis_files\CodeBook_large.xlsx', sheet_name='Min_HammingDistance_2', header=0)
    codebook_large = df['CodeBook_large'].tolist()
    payload = ''
    for i in range(junk_num):
        payload = payload +codebook_large[65536+i]
    print(payload)
    return payload

