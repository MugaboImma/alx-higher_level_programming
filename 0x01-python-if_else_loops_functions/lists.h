#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - The singly linked list
 * @n: an integer n
 * @next: A pointer that points to the next node
 *
 * Description: Thew singly linked list node structure
 *
 */
typedef struct listint_s
{
	struct listint_s *next;
	int n;
} listint_t;

void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
