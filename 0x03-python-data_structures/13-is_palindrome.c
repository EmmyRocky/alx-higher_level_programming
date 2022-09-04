#include "lists.h"

/**
 * comparator - compare the beginning and end positions
 * @head: linked list
 * @last: end of list
 * Return:1 true, 0 false
 */

int comparator(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (comparator(head, last->next) && (*head)-> == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * the function is_palindrome - confirms if a singly linked list is a palindrome
 * @head: linked list itself
 * Return: 1 true, 0 false
 */

int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (comparator(head, *head));
}
