#include "lists.h"

/**
 *  check_cycle - Checks if ll has a cycle
 *
 *  @list: listint_
 *
 *  Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list->next;

	while (slow && fast->next && fast->next->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
