#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - a C function that prints some
 * basic info about Python lists
 * @p: the input
 */
void print_python_list_info(PyObject *p)
{
	unsigned int i;
	unsigned int size;
	unsigned int allocated;
	PyTypeObject *type;
	const char *name;

	if (p == NULL)
		return;

	size = (unsigned int) PyList_Size(p);
	allocated = (unsigned int) ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		type = PyList_GET_ITEM(p, i)->ob_type;
		name = type->tp_name;
		printf("Element %d: %s\n", i, name);
	}
}
