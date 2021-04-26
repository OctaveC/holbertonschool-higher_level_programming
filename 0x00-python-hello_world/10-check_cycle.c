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
	listint_t *search1 = list, *search2 = list;

	while (search1 != NULL && list != NULL)
	{
		if (search1 == search1->next)
			return (1);
		for (search2 = list; search2 != search1; search2 = search2->next)
		{
			if (search2 == search1->next)
				return (1);
		}
		search1 = search1->next;
	}
	return (0);
}
