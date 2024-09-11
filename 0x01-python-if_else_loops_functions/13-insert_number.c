#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node;
    listint_t *current;
    listint_t *previous;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;
    }

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || (*head)->n >= number) {
        new_node->next = *head;
        *head = new_node;
    } else {
        current = *head;
        previous = NULL;

        while (current != NULL && current->n < number) {
            previous = current;
            current = current->next;
        }

        new_node->next = current;
        previous->next = new_node;
    }

    return new_node;
}
