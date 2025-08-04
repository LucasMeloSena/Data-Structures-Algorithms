// push - redimencionamento automatico

#include <stdio.h>
#include <stdlib.h>

typedef struct
{
  int *data;
  int capacity;
  int size;
} Array;

void initArray(Array *arr, int capacity)
{
  arr->data = (int *)malloc(capacity * sizeof(int));
  arr->capacity = capacity;
  arr->size = 0;

  for (int i = 0; i < capacity; i++)
  {
    *(arr->data + i) = 0;
  }
}

void push(Array *arr, int value)
{
  if (arr->size >= arr->capacity)
  {
    int new_capacity = arr->capacity * 2;
    int *new_data = (int *)realloc(arr->data, new_capacity * sizeof(int));

    if (new_data == NULL)
    {
      printf("Alocating memory error");
      return;
    }

    arr->data = new_data;

    for (int i = arr->capacity; i < new_capacity; i++)
    {
      *(arr->data + i) = 0;
    }

    arr->capacity = new_capacity;
  }

  *(arr->data + arr->size) = value;
  arr->size += 1;
}

int get(Array *arr, int index)
{
  if (index >= arr->capacity || index < 0)
  {
    printf("Key Error");
    return -1;
  }

  return *(arr->data + index);
}

void freeMemory(Array *arr)
{
  free(arr->data);
}

int main()
{
  Array arr;
  initArray(&arr, 2);

  push(&arr, 10);
  push(&arr, 20);
  push(&arr, 30);
  push(&arr, 40);
  push(&arr, 50);

  for (int i = 0; i < arr.capacity; i++)
  {
    printf("Index %d: %d\n", i, *(arr.data + i));
  }

  printf("Value at index 0: %d\n", get(&arr, 0));

  freeMemory(&arr);
}
