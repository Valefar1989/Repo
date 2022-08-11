string numberStr = Console.ReadLine();
int number = Convert.ToInt32(numberStr);
int n = 1;
int result;
while (n <= number)
{
    result = n % 2;
    if(result == 0)
    {
        Console.WriteLine(n);
    }

n = n + 1;
}
