#include "lists.h"

/**
* insert_node - inserts a number into a sorted
*		singly linked list
*
* @head: a pointer to the head node
* @number: value to be inserted into the list
*
* Return: newnode address, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *tempNode;

	newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	tempNode = *head;

	while (tempNode->next != NULL && tempNode->next->n <= number)
	{
		tempNode = tempNode->next;
	}
	newNode->next = tempNode->next;
	tempNode->next = newNode;

	return (newNode);
}
