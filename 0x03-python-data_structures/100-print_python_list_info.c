#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print list info about Python
 *
 * @p: Pyobjext pointer
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t count;
	long int length = PyList_Size(p);
	PyListObject *pObj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated %ld\n", pObj->allocated);

	for (count = 0; count < length; count++)
	{
		printf("Element %d: %s\n", count, Py_TYPE(pObj->ob_item[count])->tp_name);
	}

}
