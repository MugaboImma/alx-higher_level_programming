#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - A C function that prints some basic info
 * about Python lists.
 * @p:PyObject list
 *
 */
void print_python_list_info(PyObject *p)
{
	int n, size, alloc;
	PyObject *object;

	size = Py_SIZE(p);
	alloc = ((PyObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (n = 0; n < size; n++)
	{
		printf("Element %d: ", n);
		object = PyList_GetItem(p, n);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
