#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer
 * @number: number to insert.
 * Return:  NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *n;

	n = malloc(sizeof(listint_t));
	if (n == NULL)
		return (NULL);
	n->nn = number;

	if (node == NULL || node->nn >= number)
	{
		n->next = node;
		*head = n;
		return (n);
	}

	while (node && node->next && node->next->nn < number)
		node = node->next;

	n->next = node->next;
	node->next = n;

	return (n);
}

