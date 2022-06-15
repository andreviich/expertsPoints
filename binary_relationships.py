# установить:
# pip install openpyxl
# pip install ranky
import numpy as np
import pandas as pd

fridges = pd.read_excel('Выбор_Холодильников.xlsx', sheet_name='Выбор холодильников', engine='openpyxl')


def binary_rel() :
    # Выборка из экселя информации по нужным вопросам
    names = [fridges['Ваше имя'].tolist()][0]
    names_ch = [fridges['Ваш пол'].tolist()][0]
    first_second_question = [fridges['Samsung (1) или LG (2) ?'].tolist()][0]
    first_third_question = [fridges['Samsung (1) или Indesit (3) ?'].tolist()][0]
    first_fourth_question = [fridges['Samsung (1) или HotPoint (4) ?'].tolist()][0]
    second_third_question = [fridges['LG (2) или Indesit (3) ?'].tolist()][0]
    second_fourth_question = [fridges['LG (2) или HotPoint (4) ?'].tolist()][0]
    third_fourth_question = [fridges['Indesit (3) или HotPoint (4) ?'].tolist()][0]
    # print(names)
    k = len(names)  # число экспертов
    n = 4  # число ранжируемых вариантов
    print('Кол-во экспертов: ', len(names))
    final_matr = []
    list1 = 0
    list2 = 0
    list3 = 0
    list4 = 0
    list5 = 0
    list6 = 0
    list11 = 0
    list22 = 0
    list33 = 0
    list44 = 0
    list55 = 0
    list66 = 0
    # Генерация матриц бинарных отношений для всех рассматриваемых экспертов
    for i in range(k) :
        matr_first = np.ones((n, n))
        if first_second_question[i - 1] == 1 :
            matr_first[1] = [0, 1, 0, 0]
            if first_third_question[i - 1] == 1 :
                matr_first[2] = [0, 0, 1, 0]
                if first_fourth_question[i - 1] == 1 :
                    matr_first[0] = [1, 1, 1, 1]
                    matr_first[3] = [0, 0, 0, 1]
                else :
                    matr_first[0] = [1, 1, 1, 0]
                    matr_first[3] = [1, 0, 0, 1]
            else :
                matr_first[2] = [1, 0, 1, 0]
                if first_fourth_question[i - 1] == 1 :
                    matr_first[0] = [1, 1, 0, 1]
                    matr_first[3] = [0, 0, 0, 1]
                else :
                    matr_first[0] = [1, 1, 0, 0]
                    matr_first[3] = [1, 0, 0, 1]
        else :
            matr_first[1] = [1, 1, 0, 0]
            if first_third_question[i - 1] == 1 :
                matr_first[2] = [0, 0, 1, 0]
                if first_fourth_question[i - 1] == 1 :
                    matr_first[0] = [1, 0, 1, 1]
                    matr_first[3] = [0, 0, 0, 1]
                else :
                    matr_first[0] = [1, 0, 1, 0]
                    matr_first[3] = [1, 0, 0, 1]
            else :
                matr_first[2] = [1, 0, 1, 0]
                if first_fourth_question[i - 1] == 1 :
                    matr_first[0] = [1, 0, 0, 1]
                    matr_first[3] = [0, 0, 0, 1]
                else :
                    matr_first[0] = [1, 0, 0, 0]
                    matr_first[3] = [1, 0, 0, 1]
        if second_third_question[i - 1] == 2 :
            matr_first[1][2] = 1
            matr_first[2][1] = 0
        else :
            matr_first[1][2] = 0
            matr_first[2][1] = 1
        if second_fourth_question[i - 1] == 2 :
            matr_first[1][3] = 1
            matr_first[3][1] = 0
        else :
            matr_first[1][3] = 0
            matr_first[3][1] = 1
        if third_fourth_question[i - 1] == 3 :
            matr_first[2][3] = 1
            matr_first[3][2] = 0
        else :
            matr_first[2][3] = 0
            matr_first[3][2] = 1

        columns = ['Samsung', 'LG', 'Indesit', 'HotPoint']
        index = ['Samsung', 'LG', 'Indesit', 'HotPoint']
        first_df = pd.DataFrame(matr_first, index, columns)
        print('Массив ранговых оценок эксперта', names[i], ':')
        print(first_df)
        final_matr.append(matr_first)  # финальная матрица со всеми бинарными отношениями экспертов

        names_ch[i - 1] = pd.DataFrame(0, index, columns)
        np.fill_diagonal(names_ch[i - 1].values, 1)
        if fridges.iloc[i - 1].iloc[1] == 1 :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        else :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        if fridges.iloc[i - 1].iloc[2] == 1 :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        else :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]])
        if fridges.iloc[i - 1].iloc[3] == 1 :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        else :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
        if fridges.iloc[i - 1].iloc[4] == 2 :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        else :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
        if fridges.iloc[i - 1].iloc[5] == 2 :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
        else :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
        if fridges.iloc[i - 1].iloc[6] == 3 :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
        else :
            names_ch[i - 1] = names_ch[i - 1] + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]])
        # Кол-во выборов варианта для медианы кемени
        # Первый вариант
        if (names_ch[i - 1].iloc[0]).tolist() == [1, 1, 1, 1] :
            list1 = list1 + 1
            list2 = list2 + 1
            list3 = list3 + 1
        if (names_ch[i - 1].iloc[0]).tolist() == [1, 0, 1, 1] :
            list2 = list2 + 1
            list3 = list3 + 1
        if (names_ch[i - 1].iloc[0]).tolist() == [1, 0, 0, 1] :
            list3 = list3 + 1
        if (names_ch[i - 1].iloc[0]).tolist() == [1, 1, 0, 0] :
            list1 = list1 + 1
        if (names_ch[i - 1].iloc[0]).tolist() == [1, 0, 1, 0] :
            list2 = list2 + 1
        if (names_ch[i - 1].iloc[0]).tolist() == [1, 1, 1, 0] :
            list1 = list1 + 1
            list2 = list2 + 1
        if (names_ch[i - 1].iloc[0]).tolist() == [1, 1, 0, 1] :
            list1 = list1 + 1
            list3 = list3 + 1
        # Второй вариант
        if (names_ch[i - 1].iloc[1]).tolist() == [1, 1, 1, 1] :
            list4 = list4 + 1
            list5 = list5 + 1
            list11 = list11 + 1
        if (names_ch[i - 1].iloc[1]).tolist() == [1, 1, 1, 0] :
            list4 = list4 + 1
            list11 = list11 + 1
        if (names_ch[i - 1].iloc[1]).tolist() == [1, 1, 0, 1] :
            list5 = list5 + 1
            list11 = list11 + 1
        if (names_ch[i - 1].iloc[1]).tolist() == [0, 1, 1, 1] :
            list5 = list5 + 1
            list4 = list4 + 1
        if (names_ch[i - 1].iloc[1]).tolist() == [1, 1, 0, 0] :
            list11 = list11 + 1
        if (names_ch[i - 1].iloc[1]).tolist() == [0, 1, 1, 0] :
            list4 = list4 + 1
        if (names_ch[i - 1].iloc[1]).tolist() == [0, 1, 0, 1] :
            list5 = list5 + 1
        # Third index
        if (names_ch[i - 1].iloc[2]).tolist() == [1, 1, 1, 1] :
            list6 = list6 + 1
            list22 = list22 + 1
            list33 = list33 + 1
        if (names_ch[i - 1].iloc[2]).tolist() == [1, 1, 1, 0] :
            list22 = list22 + 1
            list33 = list33 + 1
        if (names_ch[i - 1].iloc[2]).tolist() == [1, 0, 1, 1] :
            list22 = list22 + 1
            list6 = list6 + 1
        if (names_ch[i - 1].iloc[1]).tolist() == [0, 1, 1, 1] :
            list33 = list33 + 1
            list6 = list6 + 1
        if (names_ch[i - 1].iloc[2]).tolist() == [1, 0, 1, 0] :
            list22 = list22 + 1
        if (names_ch[i - 1].iloc[2]).tolist() == [0, 1, 1, 0] :
            list33 = list33 + 1
        if (names_ch[i - 1].iloc[2]).tolist() == [0, 0, 1, 1] :
            list6 = list6 + 1
        # Fourth index
        if (names_ch[i - 1].iloc[3]).tolist() == [1, 1, 1, 1] :
            list44 = list44 + 1
            list55 = list55 + 1
            list66 = list66 + 1
        if (names_ch[i - 1].iloc[3]).tolist() == [0, 1, 1, 1] :
            list55 = list55 + 1
            list66 = list66 + 1
        if (names_ch[i - 1].iloc[3]).tolist() == [1, 0, 1, 1] :
            list44 = list44 + 1
            list66 = list66 + 1
        if (names_ch[i - 1].iloc[3]).tolist() == [1, 1, 0, 1] :
            list44 = list44 + 1
            list55 = list55 + 1
        if (names_ch[i - 1].iloc[3]).tolist() == [0, 0, 1, 1] :
            list66 = list66 + 1
        if (names_ch[i - 1].iloc[3]).tolist() == [0, 1, 0, 1] :
            list55 = list55 + 1
        if (names_ch[i - 1].iloc[3]).tolist() == [1, 0, 0, 1] :
            list44 = list44 + 1

    # Формирование матрицы Кемени
    kemeni = pd.DataFrame(0, index, columns)
    np.fill_diagonal(kemeni.values, 1)
    if list1 > list11 :
        kemeni = kemeni + np.array([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    else :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    if list2 > list22 :
        kemeni = kemeni + np.array([[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    else :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]])
    if list3 > list33 :
        kemeni = kemeni + np.array([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    else :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
    if list4 > list44 :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    else :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
    if list5 > list55 :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    else :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
    if list6 > list66 :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
    else :
        kemeni = kemeni + np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]])
    print("-----------------------------------------------------------")
    print("Медиана Кемени:")
    print(kemeni)

    # расчёт расстояний между матрицами бинарных отношений
    ranges = []
    l = 0
    ranges_one = []
    for i in range(k) :
        range_ = abs(final_matr[i - 1] - final_matr[i])
        range_ = range_.tolist()

        for j in range_ :
            l += sum(j)
            ranges.append(l)

    print('----------------------------------------------')
    print('Значение целевой функции:', sum(ranges))


if __name__ == '__main__' :
    binary_rel()
