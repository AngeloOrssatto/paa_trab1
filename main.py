from cProfile import label
from MergeSort import mergeSort
from QuickSort import quickSort
from HeapSort import heapSort
from Graphs import creatGraphs
import time 
import copy
import pandas as pd
import sys
import glob

sys.setrecursionlimit(1500)

results = []

# Lista todos os arquivos .txt 
#files = glob.glob(r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\**\*.txt", recursive=True)

files = [
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Aleatórios\a1000.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Aleatórios\a100.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Aleatórios\a500.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Decrescentes\d1000.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Decrescentes\d100.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Decrescentes\d500.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Ordenados\o1000.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Ordenados\o100.txt",    
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\Ordenados\o500.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\ParcialmenteOrdenados\po1000.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\ParcialmenteOrdenados\po100.txt",
    r"D:\Documentos\CIENCIA DA COMPUTAÇAO\4º ANO\Projeto e Análise de Algoritmos\Trabalho 1\ParcialmenteOrdenados\po500.txt",
]

for file in files:
    print(file)

    if "Aleatórios" in file:
        mode = "Aleatorio"
    elif "Decrescentes" in file:
        mode = "Decrescente"
    elif "ParcialmenteOrdenados" in file:
        mode = "Parcialmente Ordenado"
    elif "Ordenados" in file:
        mode = "Ordenado"

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
    results.append(['Merge', mode, len(v_tosort), begin, end, exe_time])

    # Quick
    v_tosort = copy.deepcopy(v)
    begin = time.time_ns()
    quickSort(v_tosort, 0, len(v_tosort)-1)
    end = time.time_ns()
    exe_time = end-begin
    print("tempo execução quick (ns)", exe_time, begin, end)
    results.append(['Quick', mode, len(v_tosort), begin, end, exe_time])
    
    # Heap
    v_tosort = copy.deepcopy(v)
    begin = time.time_ns()
    heapSort(v_tosort)
    end = time.time_ns()
    exe_time = end-begin
    print("tempo execução heap (ns)", exe_time, begin, end) 
    results.append(['Heap', mode, len(v_tosort), begin, end, exe_time])

df = pd.DataFrame(data=results, columns=['Method', 'Mode', 'N_elements', 'Begin_exe', 'End_exe', 'Exec_time'])
df.to_excel("output.xlsx")

creatGraphs(df)
