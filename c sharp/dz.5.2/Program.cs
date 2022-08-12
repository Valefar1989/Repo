int size = 10;
int summa = 0;
int[] array = new int[size];

Random random = new Random();

for (int i = 0; i < size; i++)
{
    array[i] = random.Next(1, 9);
}
for (int i = 0; i < size; i++)
{
    Console.Write(array[i] + " ");
}
for (int i = 0; i < size; i=i+2)
{
    //Console.Write(array[i] + " ");
    summa = summa+array[i];

}
Console.Write(summa);