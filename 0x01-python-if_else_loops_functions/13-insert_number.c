#include "lists.h"

/**
 * insert_node - Adds a node in an ordered linked list
 * @head: The head of the list
 * @number: The int to be inserted into the list
 *
 * Return: The address of the new element, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h;
	listint_t *placeholder;

	h = malloc(sizeof(listint_t));
	if (h == NULL)
		return (NULL);

	placeholder = *head;

	if (*head == NULL)
		h = add_nodeint_end(head, number);
	else if (placeholder->n > number)
	{
		h->next = placeholder->next;
		placeholder->next = h;
		h->n = number;
	}
	else
	{
		while (placeholder->next != NULL)
		{
			if (placeholder->next->n > number)
			{
				h->next = placeholder->next;
				placeholder->next = h;
				h->n = number;
				return (h);
			}
			placeholder = placeholder->next;
		}
		h = add_nodeint_end(head, number);
	}
	return (h);
}
