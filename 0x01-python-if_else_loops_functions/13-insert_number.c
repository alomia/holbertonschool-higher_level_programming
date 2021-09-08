#include "lists.h"
/**
 * listint_t -  inserts a number into a sorted singly linked list
 * @head: variable
 * @number: variable
 * 
 * Return: new
 */

listint_t *insert_node(listint_t **head, int number)
{

listint_t *new;
listint_t *h;
listint_t *h_prev;

h = *head;
new = malloc(sizeof(listint_t));

if (new == NULL)
return (NULL);

while (h != NULL)
{
if (h->n > number)
break;
h_prev = h;
h = h->next;
}

new->n = number;

if (*head == NULL)
{
new->next = NULL;
*head = new;
}
else
{
new->next = h;
if (h == *head)
*head = new;
else
h_prev->next = new;
}

return (new);
}