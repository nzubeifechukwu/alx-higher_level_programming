#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to an object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *l;

	l = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", l->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %ld: \n", i/*, typeof(p[i])*/);
	}
}
