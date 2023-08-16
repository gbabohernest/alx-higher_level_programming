#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - Print basic list info about Python list
* @p: list object
* Return: void (nothing)
*/

void print_python_list_info(PyObject *p)
{
	if (p == NULL || !PyList_Check(p))
	{
		printf("Expected a list");
		return;
	}

	Py_ssize_t sizeOfList = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t i;

	printf("[*] Size of the Python List = %ld\n", sizeOfList);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < sizeOfList; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		if (item == NULL)
		{
			printf("Element %ld: Unable to get element\n", i);
			continue;
		}
		const char *type_name = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type_name);
	}
}
