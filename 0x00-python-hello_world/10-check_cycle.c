#include "lists.h"

/**
* check_cycle - checks if a circle is found
*		in a singly linked list
*
* @list: head of the linked list
* Return: 0 if no cylce is found, 1 if there is
*
*/

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
