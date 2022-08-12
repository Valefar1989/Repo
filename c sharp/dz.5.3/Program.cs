int size = 8;
double raznica = 0.0;
double [] array = new double[size];

Random random = new Random();

for (int i = 0; i < size; i++)
{
    array[i] = 5 - random.Next(11) + random.NextDouble();
}

for (int i = size - 1; i > 0; i--)
{
    for (int k = 0; k < i; k++)
    {
        if(array[k] > array[k+1])
        {
            double element = array[k];
            array[k] = array[k+1];
            array[k+1] = element;
        }
    }
}

for (int i = 0; i < size; i++)
{
    Console.Write(array[i] + " ");
}
raznica = array[size-1]-array[0];
Console.Write(raznica);