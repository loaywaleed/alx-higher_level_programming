#include "lists.h"
/**
 * check_cycle - checks if there is a cycle in the linked list
 * @list: linked list
 * Return: 0 if none, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (hare == tortoise)
		{
			return (1);
		}
	}
	return (0);
}
