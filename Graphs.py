from cProfile import label
from matplotlib.pyplot import plot


def creatGraphs(df):
    import matplotlib.pyplot as plt
    print(df)
    
    df_quick_ordenado = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Ordenado')].set_index('N_elements')
    df_quick_ordenado = df_quick_ordenado.loc[(df_quick_ordenado['Method'] == 'Quick')]
    print(df_quick_ordenado)

    df_heap_ordenado = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Ordenado')].set_index('N_elements')
    df_heap_ordenado = df_heap_ordenado.loc[(df_heap_ordenado['Method'] == 'Heap')]
    print(df_heap_ordenado)

    df_merge_ordenado = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Ordenado')].set_index('N_elements')
    df_merge_ordenado = df_merge_ordenado.loc[(df_merge_ordenado['Method'] == 'Merge')]
    print(df_merge_ordenado)

    df_quick_aleatorio = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Aleatorio')].set_index('N_elements')
    df_quick_aleatorio = df_quick_aleatorio.loc[(df_quick_aleatorio['Method'] == 'Quick')]
    print(df_quick_aleatorio)

    df_heap_aleatorio = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Aleatorio')].set_index('N_elements')
    df_heap_aleatorio = df_heap_aleatorio.loc[(df_heap_aleatorio['Method'] == 'Heap')]
    print(df_heap_aleatorio)

    df_merge_aleatorio = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Aleatorio')].set_index('N_elements')
    df_merge_aleatorio = df_merge_aleatorio.loc[(df_merge_aleatorio['Method'] == 'Merge')]
    print(df_merge_aleatorio)

    df_quick_decrescente = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Decrescente')].set_index('N_elements')
    df_quick_decrescente = df_quick_decrescente.loc[(df_quick_decrescente['Method'] == 'Quick')]
    print(df_quick_decrescente)

    df_heap_decrescente = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Decrescente')].set_index('N_elements')
    df_heap_decrescente = df_heap_decrescente.loc[(df_heap_decrescente['Method'] == 'Heap')]
    print(df_heap_decrescente)

    df_merge_decrescente = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Decrescente')].set_index('N_elements')
    df_merge_decrescente = df_merge_decrescente.loc[(df_merge_decrescente['Method'] == 'Merge')]
    print(df_merge_decrescente)

    df_quick_parcialmenteordenado = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Parcialmente Ordenado')].set_index('N_elements')
    df_quick_parcialmenteordenado = df_quick_parcialmenteordenado.loc[(df_quick_parcialmenteordenado['Method'] == 'Quick')]
    print(df_quick_parcialmenteordenado)

    df_heap_parcialmenteordenado = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Parcialmente Ordenado')].set_index('N_elements')
    df_heap_parcialmenteordenado = df_heap_parcialmenteordenado.loc[(df_heap_parcialmenteordenado['Method'] == 'Heap')]
    print(df_heap_parcialmenteordenado)

    df_merge_parcialmenteordenado = df.sort_values(by=['N_elements']).loc[(df['Mode'] == 'Parcialmente Ordenado')].set_index('N_elements')
    df_merge_parcialmenteordenado = df_merge_parcialmenteordenado.loc[(df_merge_parcialmenteordenado['Method'] == 'Merge')]
    print(df_merge_parcialmenteordenado)

    figure, axis = plt.subplots(2, 2)

    axis[0, 0].set_title('Conjunto de dados ordenado')
    axis[0, 0].set_xlabel('Número de elementos')
    axis[0, 0].set_ylabel('Tempo de execução (ns)')
    axis[0, 0].plot(df_quick_ordenado['Exec_time'], label='QuickSort')
    axis[0, 0].plot(df_heap_ordenado['Exec_time'], label='HeapSort')
    axis[0, 0].plot(df_merge_ordenado['Exec_time'], label='MergeSort')
    axis[0, 0].legend()

    axis[0, 1].set_title('Conjunto de dados aleatório')
    axis[0, 1].set_xlabel('Número de elementos')
    axis[0, 1].set_ylabel('Tempo de execução (ns)')
    axis[0, 1].plot(df_quick_aleatorio['Exec_time'], label='QuickSort')
    axis[0, 1].plot(df_heap_aleatorio['Exec_time'], label='HeapSort')
    axis[0, 1].plot(df_merge_aleatorio['Exec_time'], label='MergeSort')
    axis[0, 1].legend()

    axis[1, 0].set_title('Conjunto de dados parcialmente ordenado')
    axis[1, 0].set_xlabel('Número de elementos')
    axis[1, 0].set_ylabel('Tempo de execução (ns)')
    axis[1, 0].plot(df_quick_parcialmenteordenado['Exec_time'], label='QuickSort')
    axis[1, 0].plot(df_heap_parcialmenteordenado['Exec_time'], label='HeapSort')
    axis[1, 0].plot(df_merge_parcialmenteordenado['Exec_time'], label='MergeSort')
    axis[1, 0].legend()

    axis[1, 1].set_title('Conjunto de dados decrescente')
    axis[1, 1].set_xlabel('Número de elementos')
    axis[1, 1].set_ylabel('Tempo de execução (ns)')
    axis[1, 1].plot(df_quick_decrescente['Exec_time'], label='QuickSort')
    axis[1, 1].plot(df_heap_decrescente['Exec_time'], label='HeapSort')
    axis[1, 1].plot(df_merge_decrescente['Exec_time'], label='MergeSort')
    axis[1, 1].legend()

    plt.show()

    fig, axis = plt.subplots(3, sharex=True)
    axis[0].set_title('QuickSort')
    # axis[0].set_xlabel('Número de elementos')
    axis[0].set_ylabel('Tempo de execução (ns)')
    axis[0].plot(df_quick_ordenado['Exec_time'], label='Ordenados')
    axis[0].plot(df_quick_aleatorio['Exec_time'], label='Aleatórios')
    axis[0].plot(df_quick_decrescente['Exec_time'], label='Decrescentes')
    axis[0].plot(df_quick_parcialmenteordenado['Exec_time'], label='Parcialmente Ordenados')
    axis[0].legend()

    axis[1].set_title('MergeSort')
    # axis[1].set_xlabel('Número de elementos')
    axis[1].set_ylabel('Tempo de execução (ns)')
    axis[1].plot(df_merge_ordenado['Exec_time'], label='Ordenados')
    axis[1].plot(df_merge_aleatorio['Exec_time'], label='Aleatórios')
    axis[1].plot(df_merge_decrescente['Exec_time'], label='Decrescentes')
    axis[1].plot(df_merge_parcialmenteordenado['Exec_time'], label='Parcialmente Ordenados')
    axis[1].legend()

    axis[2].set_title('HeapSort')
    axis[2].set_xlabel('Número de elementos')
    axis[2].set_ylabel('Tempo de execução (ns)')
    axis[2].plot(df_heap_ordenado['Exec_time'], label='Ordenados')
    axis[2].plot(df_heap_aleatorio['Exec_time'], label='Aleatórios')
    axis[2].plot(df_heap_decrescente['Exec_time'], label='Decrescentes')
    axis[2].plot(df_heap_parcialmenteordenado['Exec_time'], label='Parcialmente Ordenados')
    axis[2].legend()

    plt.show()
    