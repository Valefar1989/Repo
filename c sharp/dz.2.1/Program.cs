{
    Console.WriteLine("Введите число:");
    long n = Convert.ToInt64(Console.ReadLine());
    long result = Math.Abs(n);
    long test1 = (result / 100);

    while (result > 1000)
    {
        result /= 10;
    }

    if (test1 == 0)
    {
        Console.WriteLine("третьей цифры нет");
    }
    else
    {
        Console.WriteLine($"{n} -> {result % 10}");
    }

}