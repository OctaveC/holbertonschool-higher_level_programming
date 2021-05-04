#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - checks if a singly linked list is a palindrome.
 * @p: a python object
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int ite;
	int size = Py_SIZE(p);
	int allocation = ((PyListObject *)p)->allocated;
	char *name;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);
	for (ite = 0; ite < size; ite++)
	{
		name = (char *)Py_TYPE(PyList_GetItem(p, ite))->tp_name;
		printf("Element %d: %s\n", ite, name);
	}
}
