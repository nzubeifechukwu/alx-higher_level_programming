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
	//struct _typeobject *item_type = p->ob_type

	l = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", l->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %ld: %s\n", i, l->ob_item[i]->ob_type->tp_name);
	}
}
