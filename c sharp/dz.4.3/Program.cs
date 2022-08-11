int size = 8;
int[] array = new int[size];

Random random = new Random();

for (int i = 0; i < size; i++)
{
    array[i] = random.Next(-5, 15);
}

for (int i = size - 1; i > 0; i--)
{
    for (int k = 0; k < i; k++)
    {
        if(array[k] > array[k+1])
        {
            int element = array[k];
            array[k] = array[k+1];
            array[k+1] = element;
        }
    }
}

for (int i = 0; i < size; i++)
{
    Console.Write(array[i] + " ");
}

