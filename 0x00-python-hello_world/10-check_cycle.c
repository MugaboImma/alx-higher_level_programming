#include <stdlib.h>
#include "lists.h"

/**
 * _realloc - A function that reallocates a memory block
 * @ptr: A pointer that points to the prev memory
 * @old_size: The size of old memory
 * @new_size: The size of new memory
 *
 * Return: A pointer to the new memory, otherwise NULL
 */
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	void *new_pointer;
	unsigned int min_size = old_size < new_size ? old_size : new_size;
	unsigned int n;

	if (new_size == old_size)
		return (ptr);
	if (ptr != NULL)
	{
		if (new_size == 0)
		{
			free(ptr);
			return (NULL);
		}
		new_pointer = malloc(new_size);
		if (new_pointer != NULL)
		{
			for (n = 0; n < min_size; n++)
				*((char *)new_pointer + n) = *((char *)ptr + n);
			free(ptr);
			return (new_pointer);
		}
		free(ptr);
		return (NULL);
	}
	else
	{
		new_pointer = malloc(new_size);
		return (new_pointer);
	}
}

/**
 * check_cycle - a function in C that checks if a singly linked list has a cycle in it
 * @list: the list head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *f, *s = list;

	if (list == NULL)
		return (0);

	f = list->next;
	while (s != NULL && f != NULL && f->next != NULL)
	{
		if (s == f)
			return (1);
		f = f->next->next;
		s = s->next;
	}
	return (0);
}
