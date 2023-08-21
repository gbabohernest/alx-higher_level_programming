#include "lists.h"

/**
* middle_of_list - finds the middle of a linked list
* @head: pointer to the head node
* Return: middle node in the list
*/

listint_t *middle_of_list(listint_t **head)
{
	listint_t *fast, *slow;

	fast = slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	return (slow);
}


/**
* reverse_list - reverse a single linked list
* @head: pointer to the head node
* Return: reversed list
*/

listint_t *reverse_list(listint_t **head)
{
	listint_t *prev, *current, *nextNode;

	prev = NULL;
	current = nextNode = *head;

	while (nextNode != NULL)
	{
		nextNode = nextNode->next;
		current->next = prev;
		prev = current;
		current = nextNode;
	}
	*head = prev;

	return (prev);
}

/**
* is_palindrome - checks if a single linked list is a palindrome
* @head: a pointer to the head node
* Return: 0 if NOT a Palindrome, or 1 if it is
*/

int is_palindrome(listint_t **head)
{
	listint_t *middleNode, *sub_list, *tmp;

	middleNode = middle_of_list(head);
	sub_list = reverse_list(&middleNode);
	tmp = *head;

	while (tmp != NULL && sub_list != NULL)
	{
		if (tmp->n != sub_list->n)
		{
			return (0);
		}
		tmp = tmp->next;
		sub_list = sub_list->next;
	}
	return (1);
}
