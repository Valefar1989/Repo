int size = 10;
int even = 0;
int[] array = new int[size];

Random random = new Random();

for (int i = 0; i < size; i++)
{
    array[i] = random.Next(100, 1000);
}
for (int i = 0; i < size; i++)
{
    Console.Write(array[i] + " ");
}
for (int i = 0; i < size; i++)
{
    if(array[i]%2==0)
    {
        even = even+1;
    }
}
Console.Write(even);