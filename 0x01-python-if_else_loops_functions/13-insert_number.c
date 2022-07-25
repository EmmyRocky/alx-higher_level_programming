#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - adds a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new mode
 *
 * Return: address of the new mode, or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *prev;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (tmp)
	{
		if (tmp->n > number)
		{
			break;
		}
		prev = tmp;
		tmp = tmp->next;
	}
	new->next = tmp;
	prev->next = new;
	return (*head);
}
