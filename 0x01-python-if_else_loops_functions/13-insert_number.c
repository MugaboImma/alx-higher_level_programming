#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into
 * a sorted singly linked list.
 * @head: the list head
 * @number: the number to store
 * Return: A pointer that points to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *run_test;
	listint_t *new_list;

	run_test = *head;

	new_list = malloc(sizeof(listint_t));
	if (new_list == NULL)
		return (NULL);
	new_list->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_list->next = *head;
		*head = new_list;
		return (new_list);
	}
	while(run_test->next != NULL)
	{
		if ((run_test->next)->n >= number)
		{
			new_list->next = run_test->next;
			run_test->next = new_list;
			return (new_list);
		}
		run_test = run_test->next;
	}
	new_list->next = NULL;
	run_test->next = new_list;
	return (new_list);

}
