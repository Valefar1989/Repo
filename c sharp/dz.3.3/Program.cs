string numberStr = Console.ReadLine();
int number = Convert.ToInt32(numberStr);
int n = 1;
int result;

while (n <= number)
{
    result = n*n*n;
    
        Console.WriteLine(result);
    

n = n + 1;
}