#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Finds out if there's a loop in a linked list.
 * @list: The head of the list we're going to search
 *
 * Return: 1 if loop or 0 if no loop
 */
int check_cycle(listint_t *list)
{
	listint_t *search1, *search2;

	if (list == NULL || list->next == NULL)
		return (0);

 	search1 = list;
	search2 = list->next;

	while (search1 != NULL && search2 != NULL && search2->next != NULL)
	{
		search2 = search2->next->next;
		search1 = search1->next;
		if (search1 == search2)
			return (1);
	}
	return (0);
}
