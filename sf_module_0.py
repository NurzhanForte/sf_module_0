def game_core_v4(number):
    count = 0
    predict = np.random.randint(1,100) # генерируем случ число
    if number > predict:               # если, загадали число большее чем сгенерировано, то predict увеличиваем приблизим максимально близко к number 
        x = number // predict 
        predict = predict * x
    elif number < predict:             # если, загадали число меньшее чем сгенерировано, то predict уменьшаем приблизим максимально близко к number
        x = predict // number
        predict = predict / x
    while number != predict: #условие выхода
        count+=1 #счетчик
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    print('otvet = ', predict)        
    return(count) # выход из цикла, если угадали
    
# в итоге: сокращаем максимально шаги отгадывания числа    