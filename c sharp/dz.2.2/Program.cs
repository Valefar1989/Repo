﻿Console.WriteLine ("Введите число: ");
    int number = Convert.ToInt32(Console.ReadLine());
    if (number < 1)
    {
        Console.WriteLine ("Введено неверное число");
    }
    while (number > 7)
    {
        number = number - 7;
    }
    if (number == 1)
    {
        Console.WriteLine("Понедельник");
    }
    if (number == 2)
    {
        Console.WriteLine("Вторник");
    }
    if (number == 3)
    {
        Console.WriteLine("Среда");
    }
    if (number == 4)
    {
        Console.WriteLine("Четверг");
    }
    if (number == 5)
    {
        Console.WriteLine("Пятница");
    }
    if (number == 6)
    {
        Console.WriteLine("Суббота");
        Console.WriteLine("Выходной");
    }
    if (number == 7)
    {
        Console.WriteLine("Воскресенье");
        Console.WriteLine("Выходной");
    }