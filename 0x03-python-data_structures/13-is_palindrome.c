#include "lists.h"
#include <stdio.h>

int comparato(listin_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (comparator(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

int is_palindrome(listint_t **head)
{
	if (!head || !(**head))
		return (1);
	return (comparator(head, *head));
}

