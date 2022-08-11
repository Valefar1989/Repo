int number = 54645;
int summa = 0;
while(number > 0)
{
    summa += number % 10;
    number = number / 10;
}
Console.WriteLine(summa);

