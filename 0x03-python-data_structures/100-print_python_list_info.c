#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to an object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;

	printf("[*] Size of the Python List = %d\n", PyList_Size(p));
	printf("[*] Allocated = %d\n", PyList_Size(p));

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, typeof(p[i]));
	}
}
