string numberStr = Console.ReadLine();
int number = Convert.ToInt32(numberStr);
int numberOne = number / 10000;
int numberTwo = (number / 1000) % 10;
int numberFour = (number % 100) / 10;
int numberFive = number % 10;

if((numberOne == numberFive) && (numberTwo == numberFour))
{
    Console.WriteLine("да");
}
else
{
    Console.WriteLine("нет");
}