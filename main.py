from MergeSort import mergeSort
from QuickSort import quickSort
from HeapSort import heapSort
import time, copy

import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)
# print(sys.getrecursionlimit())

# Lista todos os arquivos .txt 
# import glob
# files = glob.glob(r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\**\*.txt", recursive=True)
# print(len(files))

files = [
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Aleatórios\a10000.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Decrescentes\d10000.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Ordenados\o1000000.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\ParcialmenteOrdenados\po100000.txt"
]

for file in files:
    print(file)

    # lê os elementos de cada arquivo e coloca no vetor v
    f = open(file, "r")
    v = []
    for x in f:
        # print(x)
        v.append(int(x.replace('\n','')))
    # print('originial', v)

    # Merge
    v_tosort = copy.deepcopy(v)
    begin = time.time_ns()
    mergeSort(v_tosort, 0, len(v_tosort)-1)
    end = time.time_ns()
    exe_time = end-begin
    print("tempo execução merge (ns)", exe_time, begin, end)
    # print('merge', v_merge)

    # print('original', v)

    # Quick
    v_tosort = copy.deepcopy(v)
    begin = time.time_ns()
    quickSort(v_tosort)
    end = time.time_ns()
    exe_time = end-begin
    print("tempo execução quick (ns)", exe_time, begin, end)
    # print('quick', v_tosort)
    
    # Heap
    v_tosort = copy.deepcopy(v)
    begin = time.time_ns()
    heapSort(v_tosort)
    end = time.time_ns()
    exe_time = end-begin
    print("tempo execução heap (ns)", exe_time, begin, end) 



