#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the head of a linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	const listint_t *placeholder;
	int length, ite1, ite2;
	int array[5000];

	if (*head == NULL)
		return (1);

	placeholder = *head;
	for (length = 0; placeholder != NULL; length++)
	{
		array[length] = placeholder->n;
		placeholder = placeholder->next;
	}
	if (length == 1)
		return (1);

	length--;
	for (ite2 = 0, ite1 = length; ite1 >= (length / 2); ite1--, ite2++)
	{
		if (array[ite1] != array[ite2])
			return (0);
	}
	return (1);
}
