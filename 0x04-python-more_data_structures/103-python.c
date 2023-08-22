#include <Python.h>
#include <stdlib.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);

/**
* print_python_list - print basic info about a python list
* @p: a pointer to the list object
* return: nothing
*/

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf(" [ERROR] Invalid  List Object\n");
		return;
	}

	Py_ssize_t sizeOfList = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t counter;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sizeOfList);
	printf("[*] Allocated = %ld\n", allocated);

	counter = 0;

	while (counter < sizeOfList)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[counter];
		const char *typeName = item->ob_type->tp_name;

		printf("Element %ld: %s\n", counter, typeName);
		if (!strcmp(((PyListObject *)p)->ob_item
			[counter]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[counter]);

		counter++;
	}
}


/**
* print_python_bytes - print basic info about python bytecode
* @p: a pointer to the bytecode object
* return: nothing
*/

void print_python_bytes(PyObject *p)
{
	char *s_value;
	Py_ssize_t sizeOfObj, length, counter;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid  Bytes Object\n");
		return;
	}

	sizeOfObj = ((PyVarObject *)p)->ob_size;
	s_value = ((PyBytesObject *)p)->ob_sval;
	length = sizeOfObj + 1 > 10 ? 10 : sizeOfObj + 1;

	printf("  size: %ld\n", sizeOfObj);
	printf("  trying string: %s\n", s_value);

	printf("  first %ld bytes: ", length);

	counter = 0;

	while (counter < length)
	{
		printf("%02hhx", s_value[counter]);
		if (counter + 1 < length)
			printf(" ");
		counter++;
	}
	printf("\n");
}
