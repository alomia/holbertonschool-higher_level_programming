#include "lists.h"
/**
 * check_cycle -  function in C that checks if a singly
 * linked list has a cycle in it
 * @lists: variable
 *
 * Return: 0
 */
int check_cycle(listint_t *lists)
{

listint_t *doud = lists;
listint_t *reg = lists;

if (lists == NULL)
{

return (0);
}

while (doud && doud->next)
{

reg = reg->next;
doud = doud->next->next;

if (reg == doud)
{

return (1);
}

}

return (0);

}
